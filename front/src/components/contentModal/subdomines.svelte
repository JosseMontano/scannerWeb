<script lang="ts">
  import Form from "../../global/form.svelte";
  import Loader from "../../global/loader.svelte";
  import { fetchData } from "../../utilities/fetch";

  let subdominesData: string[] = [];
  let loading = false;
  let subdomineInput = "";

  function handleChange(event: Event) {
    const target = event.target as HTMLSelectElement;
    subdomineInput = target.value; //guardar el valor digitado en el input
  }

  const handleGetSubdomines = async () => {
    loading = true;
    const res = await fetchData("subdomine/" + subdomineInput); //obtener el dato que devuelve el servidor
    subdominesData = res.data; //guardar en un vector el valor
    loading = false;
  };
</script>

<div>
  <!-- Mostrar el formulario -->
  <Form
    {handleChange}
    btnTxt={"Encontrar subdominios"}
    title={"Dominio"}
    {handleGetSubdomines}
    {subdomineInput}
    example={"unifranz.edu.bo"}
  />

  <!-- SI LA PETICION ESTA CARGANDO QUE MUESTE UN CARGANDO -->
  {#if loading}
    <Loader />
  {/if}
  <!-- Mostrar los datos del vector -->
  {#if subdominesData.length > 0 && !loading}
    <div class="container_btn">
      {#each subdominesData as v}
        <a class="button_url" target="_blank" href={v}>{v}</a>
      {/each}
    </div>
  {/if}
</div>

<!-- ESTILOS CSS -->
<style>
  * {
    color: #242424;
  }

  .container_btn {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
    overflow-y: scroll;
    height: 130px;
  }

  .button_url {
    background-color: #04aa73; /* Green */
    border: none;
    color: white;
    padding: 7px 20px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    transition-duration: 0.4s;
    border-radius: 12px;
    box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2),
      0 6px 20px 0 rgba(0, 0, 0, 0.19);
  }
</style>
