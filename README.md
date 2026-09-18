# Blog "Emilio Ávila"

Astro + GitHub Pages. Publicado en https://orion8924.github.io/blog/

## Publicar un artículo
1. Crea `src/content/blog/mi-articulo.md` (el nombre del archivo es la URL).
2. Cabecera:
   ```
   ---
   titulo: "Título"
   resumen: "Una o dos frases."
   fecha: 2026-09-11
   categoria: fe          # fe | libertad | tecnologia | historia | rusia | ciencia | personal
   imagen: /images/mi-foto.jpg
   imagenAlt: "Descripción de la foto"
   imagenCredito: "Foto: ..."   # opcional
   borrador: false              # true para que no se publique
   ---
   ```
3. Guarda la foto en `public/images/`.
4. `git push` a `main` → en un par de minutos está en internet.

## Categorías
Se cambian en `src/content.config.ts` (lista `CATEGORIAS` y nombres visibles).

## Local
`npm install` · `npm run dev` · `npm run build`

## Idiomas

- Los artículos viven en `src/content/blog/<idioma>/<slug>.md`, con `<idioma>` = `es`, `en` o `ru`.
- El español se publica en la raíz (`/blog/<slug>/`); inglés y ruso en `/blog/en/<slug>/` y `/blog/ru/<slug>/`.
- Una traducción es un archivo con **el mismo slug** en otra carpeta. El selector de idioma de la cabecera y las etiquetas `hreflang` se generan solos a partir de eso; si no existe traducción, no se muestra.
- Las imágenes se comparten entre idiomas (`public/images/`); solo cambian `imagenAlt` e `imagenCredito` en el frontmatter.
- Los textos de la plantilla y los nombres de categoría por idioma están en `src/i18n.ts`.

## Fotos automáticas

Al subir una rama `articulo-<algo>`, la acción `fotos.yml` ejecuta `scripts/fotos.py` (sin IA, sin dependencias), coloca las fotos, comprueba que el blog compila, fusiona en `main` y despliega. Una rama `prueba-fotos-<algo>` hace lo mismo sin fusionar.

**Portada** (en la cabecera del `.md` en español, en lugar de `imagen:`):
```
imagenFuente: wikimedia        # wikimedia | wikipedia | unsplash
imagenBuscar: "Drosophila brain connectome"
imagenPlanB: "Drosophila melanogaster"
imagenUrl: "https://commons.wikimedia.org/wiki/File:…"   # opcional: foto elegida a mano
imagenAutor: "EC - Audiovisual Service"                  # solo si imagenUrl es una imagen directa
imagenAlt: "Descripción"
```

**Fotos del cuerpo** (una línea donde deba ir la foto):
```
<!-- foto: id=cables | fuente=unsplash | buscar="server cables" | plan_b="network" | alt="Descripción" -->
```
En las traducciones basta `<!-- foto: id=cables | alt="Description" -->` y no poner `imagen:`; se reutiliza la misma foto con el crédito en su idioma.

- `wikimedia`: busca en Commons (lugares, objetos, eventos, ciencia). `wikipedia`: foto principal del artículo de Wikipedia con ese título (personas). `unsplash`: fotos conceptuales; se enlazan desde su servidor, como piden sus normas.
- Solo se aceptan dominio público, CC0, CC BY y CC BY-SA, con autor conocido. El crédito se escribe solo.
- Si no aparece la portada, la acción falla y no publica. Si falta una foto del cuerpo, se quita el hueco y se avisa en el resumen de la ejecución.
- `scripts/fotos-registro.json` guarda qué foto se usó en cada hueco (origen, autor, licencia) y evita repetir fotos entre artículos.
- Necesita el secreto `UNSPLASH_ACCESS_KEY` (Settings → Secrets and variables → Actions).
