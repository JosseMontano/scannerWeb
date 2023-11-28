export type titleCards =
  | "Identificar subdominios"
  | "Banner Grabbing"
  | "Herramientas"
  | "Puertos abiertos"
  | "Escanear vulnerabilidades"
  | "Fuerza bruta";

export interface cardsType {
  img: string;
  title: titleCards;
  description: string;
}
