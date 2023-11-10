<script lang="ts">
  import Form from "../../global/form.svelte";
  import Loader from "../../global/loader.svelte";
  import { fetchData } from "../../utilities/fetch";

  let urlInput = "";
  function handleChange(event: Event) {
    const target = event.target as HTMLSelectElement;
    urlInput = target.value;
  }

  let tecnolgoies: string[] = [];
  let loading = false;
  const handleGetTechnologies = async () => {
    loading = true;
    const res = await fetchData("technologies/" + urlInput);
    tecnolgoies = res.data;
    loading = false;
  };
</script>

<div>
  <Form
    {handleChange}
    btnTxt={"Buscar las tecnologias"}
    title={"Url"}
    handleGetSubdomines={handleGetTechnologies}
    subdomineInput={urlInput}
    example={"unifranz.edu.bo"}
  />

  {#if loading}
    <Loader />
  {/if}

  {#if tecnolgoies.length > 0 && !loading}
    <div class="container_btn">
      {#each tecnolgoies as v}
        <p class="button_url">{v}</p>
      {/each}
    </div>
  {/if}
</div>

<style>
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
    transition-duration: 0.4s;
    border-radius: 12px;
    box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2),
      0 6px 20px 0 rgba(0, 0, 0, 0.19);
  }
</style>
