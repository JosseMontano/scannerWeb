<script lang="ts">
  import Loader from "../../global/loader.svelte";
  import { fetchData } from "../../utilities/fetch";

  let subdominesData: string[] = [];
  let loading = false;
  let subdomineInput = "";

  function handleChange(event: Event) {
    const target = event.target as HTMLSelectElement;
    subdomineInput = target.value;
  }

  const handleGetSubdomines = async () => {
    loading = true;
    const res = await fetchData("subdomine/unifranz.edu.bo");
    subdominesData = res.data;
    loading = false;
  };
</script>

<div>
  <div class="container_header">
    <label for="">Subdominio: </label>
    <input
      placeholder="unifranz.edu.bo"
      bind:value={subdomineInput}
      on:input={(e) => handleChange(e)}
    />
    <button class="btn" on:click={handleGetSubdomines}
      >Encontrar subdominios</button
    >
  </div>

  {#if loading}
    <div class="container_loader">
      <Loader />
    </div>
  {/if}

  <div class="container_btn">
    {#each subdominesData as v}
      <a class="button_url" target="_blank" href={v}>{v}</a>
    {/each}
  </div>
</div>

<style>
  * {
    color: #242424;
  }

  .container_header {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 10px;
  }

  .container_loader {
    display: flex;
    justify-content: center;
  }

  .container_header label {
    font-weight: bold;
    font-size: 18px;
  }

  input {
    padding: 12px 20px;
    margin: 8px 0;
    display: inline-block;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
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
