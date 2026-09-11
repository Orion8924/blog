import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

export const CATEGORIAS = ['fe', 'libertad', 'tecnologia', 'historia', 'personal'] as const;

export const NOMBRES_CATEGORIA: Record<(typeof CATEGORIAS)[number], string> = {
  fe: 'Fe',
  libertad: 'Libertad',
  tecnologia: 'Tecnología',
  historia: 'Historia',
  personal: 'Personal',
};

const blog = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/blog' }),
  schema: z.object({
    titulo: z.string(),
    resumen: z.string(),
    fecha: z.coerce.date(),
    categoria: z.enum(CATEGORIAS),
    imagen: z.string(),          // ruta dentro de /public, p. ej. /images/foto.jpg
    imagenAlt: z.string().default(''),
    imagenCredito: z.string().optional(),
    borrador: z.boolean().default(false),
  }),
});

export const collections = { blog };
