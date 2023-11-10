<script lang="ts">
  import Loader from "../../global/loader.svelte";
  import { PostData } from "../../utilities/fetch";

  let formData = {
    ip: "",
    portStart: "",
    portEnd: "",
  };

  const handleChange = (event) => {
    const { name, value } = event.target;
    formData = { ...formData, [name]: value };
  };

  let portsOpen: string[] = [];
  let loading = false;
  const handleGetPorts = async (e: Event) => {
    e.preventDefault();
    loading = true;
    const obj = {
      ip: formData.ip,
      portStart: parseFloat(formData.portStart),
      portEnd: parseFloat(formData.portEnd),
    };
    const data = await PostData("scannerPorts", obj);
    portsOpen = data;
    loading = false;
  };
</script>

<div>
  <form class="container_header" on:submit={(e) => handleGetPorts(e)}>
    <div>
      <label for="">Ip</label>
      <input
        placeholder={"192.168.1.9"}
        bind:value={formData.ip}
        on:input={(e) => handleChange(e)}
      />
    </div>

    <div>
      <input
        placeholder={"Desde: 1"}
        bind:value={formData.portStart}
        on:input={(e) => handleChange(e)}
      />
      <input
        placeholder={"Hasta: 81"}
        bind:value={formData.portEnd}
        on:input={(e) => handleChange(e)}
      />
    </div>
    <button class="btn">Obtener puertos</button>
  </form>

  {#if loading}
    <Loader />
  {/if}

  {#if portsOpen.length > 0 && !loading}
    <div class="container_btn">
      {#each portsOpen as v}
        <p class="button_url">{v}</p>
      {/each}
    </div>
  {/if}
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
    width: 160px;
  }

  .container_btn {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
    overflow-y: auto;
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
