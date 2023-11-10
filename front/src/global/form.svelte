<script lang="ts">
  export let subdomineInput: string;
  export let handleChange: (event: Event) => void;
  export let handleGetSubdomines: () => Promise<void>;
  export let title: string;
  export let example: string;
  export let btnTxt: string;
</script>

<div class="container_header">
  <label for="">{title} </label>
  <input
    placeholder={example}
    bind:value={subdomineInput}
    on:input={(e) => handleChange(e)}
  />
  <button class="btn" on:click={handleGetSubdomines}>{btnTxt}</button>
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
  }
</style>
