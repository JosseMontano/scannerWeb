<script lang="ts">
  //amplía el alcance de la evaluación de seguridad

  // ======== IMG ========
  import SubdominesImg from "./assets/subdomines.png";
  import ServerImg from "./assets/server.jpg";
  import TechnologiesImg from "./assets/technologies.jpg";
  import ScannerPortImg from "./assets/scannerPorts.jpg";
  import NmapImg from "./assets/nmap.jpg";
  import type { cardsType, titleCards } from "./types/cards";

  // ======== COMPONENTS ========
  import Card from "./components/card.svelte";
  import Modal from "./global/modals.svelte";
  import SubdomineContent from "./components/contentModal/subdomines.svelte";
  import BannerContent from "./components/contentModal/banner.svelte";
  import TechnologiesContent from "./components/contentModal/technologies.svelte";

  // ======== DATA CARDS ========
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

  // ======== MODAL ========

  let modalVisible = false;
  let contentModal;

  function toggleModal(v?: titleCards) {
    modalVisible = !modalVisible;
    //save the children in a variable to the modal
    if (v == "Identificar subdominios") contentModal = SubdomineContent;
    if (v == "Banner Grabbing") contentModal = BannerContent;
    if (v == "Herramientas") contentModal = TechnologiesContent;
  }
</script>

<main>
  <div>
    <h1 class="title">Escaner Web</h1>
    <div class="container_card">
      {#each cards as v}
        <Card {v} {toggleModal} />
      {/each}
    </div>
    <Modal {modalVisible} {toggleModal} children={contentModal} />
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
