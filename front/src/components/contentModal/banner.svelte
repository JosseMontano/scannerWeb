<script lang="ts">
  import Form from "../../global/form.svelte";
  import Loader from "../../global/loader.svelte";
  import { fetchData } from "../../utilities/fetch";

  let version = "";
  let loading = false;
  let ipInput = "";

  function handleChange(event: Event) {
    const target = event.target as HTMLSelectElement;
    ipInput = target.value;
  }

  const handleGetVersion = async () => {
    loading = true;
    const res = await fetchData("bannerGrabing/" + ipInput);
    version = res.message;
    loading = false;
  };
</script>

<div>
  <Form
    {handleChange}
    btnTxt={"Obtener informacion"}
    title={"Ip"}
    handleGetSubdomines={handleGetVersion}
    subdomineInput={ipInput}
    example={"192.168.1.9"}
  />

  {#if loading}
    <Loader />
  {/if}

  {#if version != "" && !loading}
    <div class="container_btn">
      <a class="button_url" target="_blank" href="/">{version}</a>
    </div>
  {/if}
</div>

<style>
  .container_btn {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
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
    overflow-y: auto;
    max-height: 140px;
  }
</style>
