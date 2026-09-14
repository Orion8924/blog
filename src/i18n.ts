import type { CATEGORIAS } from './content.config';

export const IDIOMAS = ['es', 'en', 'ru'] as const;
export type Idioma = (typeof IDIOMAS)[number];
export const IDIOMA_DEFECTO: Idioma = 'es';
export const IDIOMAS_SECUNDARIOS = IDIOMAS.filter((i) => i !== IDIOMA_DEFECTO) as Exclude<Idioma, 'es'>[];

type Categoria = (typeof CATEGORIAS)[number];

export const NOMBRES_IDIOMA: Record<Idioma, string> = { es: 'Español', en: 'English', ru: 'Русский' };
export const LOCALES: Record<Idioma, string> = { es: 'es-ES', en: 'en-GB', ru: 'ru-RU' };

export const CATEGORIAS_I18N: Record<Idioma, Record<Categoria, string>> = {
  es: { fe: 'Fe', libertad: 'Libertad', tecnologia: 'Tecnología', historia: 'Historia', rusia: 'Rusia', personal: 'Personal' },
  en: { fe: 'Faith', libertad: 'Liberty', tecnologia: 'Technology', historia: 'History', rusia: 'Russia', personal: 'Personal' },
  ru: { fe: 'Вера', libertad: 'Свобода', tecnologia: 'Технологии', historia: 'История', rusia: 'Россия', personal: 'Личное' },
};

export const TEXTOS: Record<Idioma, { descripcion: string; sinArticulos: string; sinArticulosIdioma: string; hechoCon: string; categorias: string; idiomas: string }> = {
  es: { descripcion: 'Artículos de Emilio Ávila', sinArticulos: 'Todavía no hay artículos en esta categoría.', sinArticulosIdioma: 'Todavía no hay artículos en español.', hechoCon: 'Hecho con Astro', categorias: 'Categorías', idiomas: 'Idiomas' },
  en: { descripcion: 'Articles by Emilio Ávila', sinArticulos: 'There are no articles in this category yet.', sinArticulosIdioma: 'There are no articles in English yet.', hechoCon: 'Built with Astro', categorias: 'Categories', idiomas: 'Languages' },
  ru: { descripcion: 'Статьи Эмилио Авилы', sinArticulos: 'В этой категории пока нет статей.', sinArticulosIdioma: 'Статей на русском пока нет.', hechoCon: 'Сделано на Astro', categorias: 'Категории', idiomas: 'Языки' },
};

/** Prefijo de ruta de un idioma, relativo a BASE_URL: '' para español, 'en/' o 'ru/' para los demás. */
export function prefijo(idioma: Idioma): string {
  return idioma === IDIOMA_DEFECTO ? '' : `${idioma}/`;
}

/** Separa el id de la colección ('en/mi-articulo') en idioma y slug. */
export function partirId(id: string): { idioma: Idioma; slug: string } {
  const [idioma, ...resto] = id.split('/');
  return { idioma: idioma as Idioma, slug: resto.join('/') };
}

export function formatearFecha(d: Date, idioma: Idioma): string {
  return d.toLocaleDateString(LOCALES[idioma], { day: 'numeric', month: 'long', year: 'numeric' });
}
