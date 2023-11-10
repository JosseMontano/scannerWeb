<script lang="ts">
  import type { titleCards } from "../types/cards";

  export let toggleModal: () => void;
  export let modalVisible: boolean;
  export let children: any;
</script>

<div>
  {#if modalVisible}
    <div class="modal-overlay" role="button" on:click={toggleModal}>
      <div class="modal-content" on:click={(e) => e.stopPropagation()}>
        <!-- Contenido del modal -->

        {#if children}
          <svelte:component this={children} />
        {/if}
      </div>
    </div>
  {/if}
</div>

<style>
  .modal-overlay {
    display: flex;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    justify-content: center;
    align-items: center;
  }

  .modal-content {
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    width: 380px;
    height: 50%;
  }
</style>
