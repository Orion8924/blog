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
