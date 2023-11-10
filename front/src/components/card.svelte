<script lang="ts">
  import SubdominesImg from "../assets/subdomines.png";
  import type { cardsType } from "../types/cards";

  export let v: cardsType;
</script>

<div class="card">
  <div class="card_container">
    <img src={v.img} class="card_img" alt="img" />
  </div>
  <h3 class="card_title">{v.title}</h3>
  <p class="card_description">
    {v.description}
  </p>
  <button class="btn">Probar</button>
</div>

<style>
  .card {
    width: 320px;
    height: 320px;
    border-radius: 24px;
    background-color: rgba(255, 255, 255, 0.87);
    padding: 15px;

    /* structure */
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-top: 80px;
  }

  .card_container {
    height: 100px;
    align-self: center;
    /* structure */
    position: relative;
    bottom: 30%;
  }
  .card_img {
    width: 200px;
    height: 170px;
    object-fit: cover;
  }

  .card_title {
    color: #242424;
  }

  .card_description {
    overflow: hidden;
    min-height: 100px;
    max-height: 120px;
    color: #242424;
    font-weight: 500;
  }

  .btn {
    border: none;
    background-color: #4974a7;
    color: #242424;
    padding: 7px;
    border-radius: 14px;
    width: 140px;
    align-self: flex-end;
    cursor: pointer;
    font-size: 16px;
    font-weight: bold;
  }
</style>
