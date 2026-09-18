#!/usr/bin/env python3
"""Busca y coloca las fotos de los artículos. Sin IA y sin dependencias.

Lee marcadores en los .md de src/content/blog/<idioma>/ y los sustituye por
fotos con licencia libre de Wikimedia Commons o Unsplash. Ver README.
"""
import html, json, os, re, sys, urllib.parse, urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CONTENIDO = RAIZ / "src/content/blog"
IMAGENES = RAIZ / "public/images"
REGISTRO = RAIZ / "scripts/fotos-registro.json"
IDIOMAS = ["es", "en", "ru"]
UA = "BlogEmilioAvila/1.0 (https://orion8924.github.io/blog/)"
CLAVE_UNSPLASH = os.environ.get("UNSPLASH_ACCESS_KEY", "").strip()
ANCHO = 1600
MARCADOR = re.compile(r"<!--\s*foto:(.*?)-->", re.S)
CLAVES_PORTADA = ["imagenFuente", "imagenBuscar", "imagenPlanB", "imagenUrl", "imagenAutor"]

avisos = []


def log(*a):
    print(*a, flush=True)


# ---------------------------------------------------------------- red
def pedir(url, cabeceras=None, binario=False):
    req = urllib.request.Request(url, headers={"User-Agent": UA, **(cabeceras or {})})
    with urllib.request.urlopen(req, timeout=40) as r:
        datos = r.read()
    return datos if binario else json.loads(datos.decode("utf-8"))


def limpiar(texto, maximo=70):
    texto = re.sub(r"<[^>]+>", "", texto or "")
    texto = re.sub(r"\s+", " ", html.unescape(texto)).strip()
    if len(texto) <= maximo:
        return texto
    corte = texto[:maximo]
    for sep in (" / ", ","):  # créditos larguísimos: quedarse con la primera parte
        if sep in corte[15:]:
            return corte[: 15 + corte[15:].index(sep)].strip()
    return corte[:-1].rstrip() + "…"


def licencia_valida(nombre):
    s = (nombre or "").lower().strip()
    if s.startswith("cc0") or "public domain" in s or s.startswith("pd"):
        return True
    return s.startswith("cc by") and "nc" not in s and "nd" not in s


# ---------------------------------------------------------------- Wikimedia
def _candidata_commons(pagina, horizontal=True, permitir_png=False):
    ii = (pagina.get("imageinfo") or [{}])[0]
    meta = ii.get("extmetadata") or {}
    lic = limpiar(meta.get("LicenseShortName", {}).get("value", ""))
    # Solo JPEG: en Commons los PNG suelen ser gráficos y diagramas, no fotos.
    if ii.get("mime") != "image/jpeg" and not (permitir_png and ii.get("mime") == "image/png"):
        return None
    if not licencia_valida(lic):
        return None
    ancho, alto = ii.get("width", 0), ii.get("height", 0)
    if ancho < 1000 or (horizontal and ancho < alto):
        return None
    autor = limpiar(meta.get("Artist", {}).get("value", "")) or limpiar(meta.get("Credit", {}).get("value", ""))
    es_pd = lic.lower().startswith(("public", "pd", "cc0"))
    if not autor and not es_pd:
        return None
    return {
        "fuente": "wikimedia",
        "id": pagina["title"],
        "descarga": ii.get("thumburl") or ii["url"],
        "ext": ".png" if ii.get("mime") == "image/png" else ".jpg",
        "autor": autor,
        "licencia": lic,
        "origen": ii.get("descriptionurl", ""),
    }


def _info_commons(params, horizontal=True, permitir_png=False):
    base = {
        "action": "query", "format": "json", "prop": "imageinfo",
        "iiprop": "url|size|mime|extmetadata", "iiurlwidth": str(ANCHO),
    }
    url = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode({**base, **params})
    paginas = list((pedir(url).get("query") or {}).get("pages", {}).values())
    paginas.sort(key=lambda p: p.get("index", 0))
    return [c for c in (_candidata_commons(p, horizontal, permitir_png) for p in paginas) if c]


def buscar_wikimedia(consulta):
    return _info_commons({
        "generator": "search", "gsrnamespace": "6", "gsrlimit": "20",
        "gsrsearch": f"{consulta} filemime:image/jpeg filew:>1200",
    })


def buscar_wikipedia(titulo):
    """Foto principal del artículo de Wikipedia (ideal para personas)."""
    for wiki in ("es", "en"):
        url = f"https://{wiki}.wikipedia.org/w/api.php?" + urllib.parse.urlencode({
            "action": "query", "format": "json", "redirects": "1", "titles": titulo,
            "prop": "pageimages", "piprop": "name",
        })
        for p in (pedir(url).get("query") or {}).get("pages", {}).values():
            if p.get("pageimage"):
                c = _info_commons({"titles": "File:" + p["pageimage"]}, horizontal=False)
                if c:
                    return c
    return []


# ---------------------------------------------------------------- Unsplash
def _candidata_unsplash(f):
    if f.get("premium") or f.get("plus"):
        return None
    return {
        "fuente": "unsplash",
        "id": f["id"],
        "url": f["urls"]["raw"] + f"&w={ANCHO}&q=80&auto=format&fit=crop",
        "aviso_descarga": f.get("links", {}).get("download_location", ""),
        "autor": f["user"]["name"],
        "licencia": "Unsplash",
        "origen": f.get("links", {}).get("html", ""),
    }


def buscar_unsplash(consulta):
    if not CLAVE_UNSPLASH:
        avisos.append("Falta el secreto UNSPLASH_ACCESS_KEY: se ha saltado Unsplash.")
        return []
    url = "https://api.unsplash.com/search/photos?" + urllib.parse.urlencode({
        "query": consulta, "orientation": "landscape", "per_page": "15", "content_filter": "high",
    })
    datos = pedir(url, {"Authorization": f"Client-ID {CLAVE_UNSPLASH}", "Accept-Version": "v1"})
    return [c for c in (_candidata_unsplash(f) for f in datos.get("results", [])) if c]


def desde_url(url, autor):
    """Foto elegida a mano: página de Commons, página de Unsplash o imagen directa."""
    m = re.search(r"commons\.wikimedia\.org/wiki/(File:[^?#]+)", url)
    if m:
        return _info_commons({"titles": urllib.parse.unquote(m.group(1))}, horizontal=False, permitir_png=True)
    m = re.search(r"unsplash\.com/(?:[a-z]{2}/)?(?:photos|fotos)/(?:[^/?#]*-)?([A-Za-z0-9_-]{11})(?:[/?#]|$)", url)
    if m and CLAVE_UNSPLASH:
        f = pedir(f"https://api.unsplash.com/photos/{m.group(1)}",
                  {"Authorization": f"Client-ID {CLAVE_UNSPLASH}", "Accept-Version": "v1"})
        c = _candidata_unsplash(f)
        return [c] if c else []
    if not autor:
        avisos.append(f"URL manual sin crédito (añade autor=\"…\"): {url}")
        return []
    ext = ".png" if url.lower().split("?")[0].endswith(".png") else ".jpg"
    return [{"fuente": "manual", "id": url, "descarga": url, "ext": ext,
             "autor": autor, "licencia": "", "origen": url}]


BUSCADORES = {"wikimedia": buscar_wikimedia, "wikipedia": buscar_wikipedia, "unsplash": buscar_unsplash}


# ---------------------------------------------------------------- resolución
def resolver(espec, nombre, registro):
    """Devuelve la entrada de registro de la foto elegida, o None."""
    usadas = {v.get("id") for v in registro.values()}
    fuente = (espec.get("fuente") or "unsplash").lower()
    intentos = []
    if espec.get("url"):
        intentos.append(("url", espec["url"]))
    if espec.get("buscar"):
        intentos.append((fuente, espec["buscar"]))
    if espec.get("plan_b"):
        intentos.append((fuente, espec["plan_b"]))
        otra = "unsplash" if fuente != "unsplash" else "wikimedia"
        intentos.append((otra, espec["plan_b"]))
    for donde, consulta in intentos:
        try:
            cands = desde_url(consulta, espec.get("autor", "")) if donde == "url" else BUSCADORES.get(donde, buscar_unsplash)(consulta)
        except Exception as e:  # red, límites, JSON raro…
            avisos.append(f"Fallo consultando {donde} «{consulta}»: {e}")
            continue
        cands = [c for c in cands if c["id"] not in usadas] or (cands if donde == "url" else [])
        for c in cands[:4]:
            try:
                return materializar(c, nombre)
            except Exception as e:
                avisos.append(f"No se pudo descargar {c['id']}: {e}")
        log(f"   sin resultados válidos en {donde} para «{consulta}»")
    return None


def materializar(c, nombre):
    if c["fuente"] == "unsplash":
        # Unsplash pide enlazar a su servidor y avisar de la «descarga».
        if c.get("aviso_descarga"):
            try:
                pedir(c["aviso_descarga"], {"Authorization": f"Client-ID {CLAVE_UNSPLASH}"})
            except Exception:
                pass
        imagen = c["url"]
    else:
        datos = pedir(c["descarga"], binario=True)
        if len(datos) < 20_000:
            raise ValueError("archivo demasiado pequeño")
        IMAGENES.mkdir(parents=True, exist_ok=True)
        (IMAGENES / (nombre + c["ext"])).write_bytes(datos)
        imagen = f"/images/{nombre}{c['ext']}"
    log(f"   ✓ {c['fuente']}: {c['id']} — {c['autor'] or 's/a'} [{c['licencia']}]")
    return {"imagen": imagen, "fuente": c["fuente"], "id": c["id"], "autor": c["autor"],
            "licencia": c["licencia"], "origen": c["origen"]}


def credito(e, idioma):
    a, lic = e.get("autor", ""), e.get("licencia", "")
    if e["fuente"] == "unsplash":
        return {"es": f"Foto de {a} en Unsplash", "en": f"Photo by {a} on Unsplash", "ru": f"Фото: {a}, Unsplash"}[idioma]
    if e["fuente"] == "wikimedia":
        via = {"es": "vía Wikimedia Commons", "en": "via Wikimedia Commons", "ru": "Wikimedia Commons"}[idioma]
        return ", ".join(x for x in (a, lic, via) if x)
    return a


# ---------------------------------------------------------------- Markdown
def parsear(texto):
    espec = {}
    for trozo in texto.split("|"):
        if "=" in trozo:
            k, v = trozo.split("=", 1)
            espec[k.strip().lower()] = v.strip().strip('"“”').strip()
    return espec


def yaml_str(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def leer_cabecera(cab):
    datos = {}
    for linea in cab.splitlines():
        m = re.match(r"^([A-Za-z]+):\s*(.*)$", linea)
        if m:
            v = m.group(2).strip()
            if len(v) >= 2 and v[0] == v[-1] == '"':
                v = v[1:-1].replace('\\"', '"').replace("\\\\", "\\")
            datos[m.group(1)] = v
    return datos


def poner(cab, clave, valor):
    linea = f"{clave}: {yaml_str(valor)}"
    if re.search(rf"^{clave}:.*$", cab, re.M):
        return re.sub(rf"^{clave}:.*$", lambda _: linea, cab, count=1, flags=re.M)
    return cab.rstrip("\n") + "\n" + linea + "\n"


def quitar(cab, claves):
    for c in claves:
        cab = re.sub(rf"^{c}:.*\n?", "", cab, flags=re.M)
    return cab


def figura(e, alt, idioma):
    src = e["imagen"] if e["imagen"].startswith("http") else "/blog" + e["imagen"]
    return (f'<figure>\n  <img src="{html.escape(src)}" alt="{html.escape(alt)}" loading="lazy" />\n'
            f"  <figcaption>{html.escape(credito(e, idioma), quote=False)}</figcaption>\n</figure>")


def procesar(ruta, idioma, slug, registro):
    texto = ruta.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", texto, re.S)
    if not m:
        return True
    cab, cuerpo = m.group(1) + "\n", m.group(2)
    datos = leer_cabecera(cab)
    ok = True

    # Portada
    clave = f"{slug}/portada"
    pide = any(datos.get(k) for k in ("imagenBuscar", "imagenUrl"))
    if pide or not datos.get("imagen"):
        log(f"· {ruta.relative_to(RAIZ)} — portada")
        if pide and idioma == "es" or clave not in registro:
            if pide:
                e = resolver({"fuente": datos.get("imagenFuente"), "buscar": datos.get("imagenBuscar"),
                              "plan_b": datos.get("imagenPlanB"), "url": datos.get("imagenUrl"),
                              "autor": datos.get("imagenAutor")}, f"{slug}-portada", registro)
                if e:
                    registro[clave] = e
        e = registro.get(clave)
        if e:
            cab = poner(cab, "imagen", e["imagen"])
            cab = poner(cab, "imagenCredito", credito(e, idioma))
            cab = quitar(cab, CLAVES_PORTADA)
        else:
            avisos.append(f"SIN PORTADA: {ruta.relative_to(RAIZ)}")
            ok = False

    # Fotos del cuerpo
    def sustituir(mm):
        espec = parsear(mm.group(1))
        ident = espec.get("id") or re.sub(r"\W+", "-", (espec.get("buscar") or "foto").lower())[:30].strip("-")
        clave = f"{slug}/{ident}"
        log(f"· {ruta.relative_to(RAIZ)} — foto «{ident}»")
        if clave not in registro and (espec.get("buscar") or espec.get("url")):
            e = resolver(espec, f"{slug}-{ident}", registro)
            if e:
                registro[clave] = e
        e = registro.get(clave)
        if not e:
            avisos.append(f"Foto «{ident}» no encontrada en {ruta.relative_to(RAIZ)}: se ha quitado el hueco.")
            return ""
        return figura(e, espec.get("alt", ""), idioma)

    cuerpo = MARCADOR.sub(sustituir, cuerpo)
    nuevo = f"---\n{cab.rstrip()}\n---\n{cuerpo}"
    if nuevo != texto:
        ruta.write_text(nuevo, encoding="utf-8")
    return ok


def main():
    registro = json.loads(REGISTRO.read_text(encoding="utf-8")) if REGISTRO.exists() else {}
    todo_ok = True
    slugs = sorted({p.stem for p in CONTENIDO.glob("*/*.md")})
    for slug in slugs:
        for idioma in IDIOMAS:  # el español primero: es el que lleva las búsquedas
            ruta = CONTENIDO / idioma / f"{slug}.md"
            if not ruta.exists():
                continue
            t = ruta.read_text(encoding="utf-8")
            if MARCADOR.search(t) or re.search(r"^imagen(Buscar|Url):", t, re.M) or not re.search(r"^imagen:\s*\S", t, re.M):
                todo_ok &= procesar(ruta, idioma, slug, registro)
    REGISTRO.write_text(json.dumps(registro, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if avisos:
        log("\nAVISOS:")
        for a in dict.fromkeys(avisos):
            log(" -", a)
        resumen = os.environ.get("GITHUB_STEP_SUMMARY")
        if resumen:
            with open(resumen, "a", encoding="utf-8") as f:
                f.write("### Avisos de fotos\n" + "\n".join(f"- {a}" for a in dict.fromkeys(avisos)) + "\n")
    sys.exit(0 if todo_ok else 1)


if __name__ == "__main__":
    main()
