<script lang="ts">
  import Loader from "../../global/loader.svelte";
  import { PostFormData } from "../../utilities/fetch";

  let file = null;

  let users: string[] = [];
  let loading = false;

  const handleAttack = async (e: Event) => {
    e.preventDefault();
    loading = true;
    let formData = new FormData();
    formData.set("archivo", file);

    const res: any = await PostFormData("bruteForce", formData);
    users = res.mensaje;
    loading = false;
  };
</script>

<div>
  <form class="container_header" on:submit={(e) => handleAttack(e)}>
    <div>
      <label for="">Archivo</label>
      <input
        type="file"
        on:change={(e) => {
          const event = e.target;
          //@ts-ignore
          file = event.files[0];
        }}
      />
    </div>
    <button class="btn">Lanzar ataque</button>
  </form>

  {#if loading}
    <Loader />
  {/if}

  {#if users.length > 0 && !loading}
    <div class="container_btn">
      {#each users as v}
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
  }
</style>
