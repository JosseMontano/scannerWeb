<script lang="ts">
  //amplía el alcance de la evaluación de seguridad
  import Card from "./components/card.svelte";
  // ======== IMG ========
  import SubdominesImg from "./assets/subdomines.png";
  import ServerImg from "./assets/server.jpg";
  import TechnologiesImg from "./assets/technologies.jpg";
  import ScannerPortImg from "./assets/scannerPorts.jpg";
  import NmapImg from "./assets/nmap.jpg";
  import type { cardsType } from "./types/cards";

  const cards: cardsType[] = [
    {
      img: SubdominesImg,
      title: "Identificar subdominios",
      description: `Es clave en la fase inicial de un pentesting,
       porque aumenta las oportunidades para descubrir vulnerabilidades.`,
    },
    {
      img: ServerImg,
      title: "Banner Grabbing",
      description:
        "Exponen detalles sobre software y sistemas operativos, facilitando a los actores de amenazas encontrar vulnerabilidades.",
    },
    {
      img: TechnologiesImg,
      title: "Herramientas",
      description:
        "Comprendiendo las tecnologías y las herramientas, los hackers desarrollan ataques específicos para aprovechar debilidades conocidas.",
    },
    {
      img: ScannerPortImg,
      title: "Puertos abiertos",
      description:
        "Cada servicio en un sistema utiliza un puerto específico. Conocer los puertos abiertos indica los servicios en ejecución (servicios susceptibles a explotación).",
    },
    {
      img: NmapImg,
      title: "Escanear vulnerabilidades",
      description:
        "Detectar y corregir vulnerabilidades en los puertos es crucial para fortalecer la seguridad y prevenir ataques.",
    },
  ];
</script>

<main>
  <div>
    <h1 class="title">Escaner Web</h1>

    <div class="container_card">
      {#each cards as v}
        <Card {v} />
      {/each}
    </div>
  </div>
</main>

<style>
  .title {
    font-size: 32px;
    text-align: center;
    text-transform: uppercase;
  }

  .container_card {
    display: grid;
    grid-gap: 20px;
    justify-content: center;
    grid-template-columns: repeat(3, 320px);
    margin-bottom: 10px;
  }
</style>
