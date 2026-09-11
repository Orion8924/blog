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
   categoria: fe          # fe | libertad | tecnologia | historia | personal
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
