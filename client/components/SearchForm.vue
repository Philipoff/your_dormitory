<template>
  <div class="searchForm">
    <div class="serachForm-content">
      <div class="searchForm-header">Поиск общежития</div>

      <div class="searchForm-input__inner">
        <input class="searchForm-input-item" placeholder="Город"/>
        <input class="searchForm-input-item" placeholder="Вуз"/>
      </div>
    </div>
  </div>
</template>

<script>

</script>

<style scoped>
  .searchForm {
    background: #FF990025;
    border-radius: 10px;
    max-width: 1413px;
    padding-top: 56px;
    padding-bottom: 75px;
    padding-left: 98px;
    transition: background .3s ease-in-out;
  }
  .searchForm:hover {
    background: #FF99002D;
    transition: background .3s ease-in-out;
  }
  .searchForm-header {
    font-size: 32px;
    margin-bottom: 39px;
  }
  .searchForm-input-item {
    width: 461px;
    padding: 15px;
    font-size: 20px;
    line-height: 20px;
    margin-right: 76px;
    padding-left: 61px;
    border: 1px solid rgba(255, 153, 0, 0.5);
    border-radius: 5px;
    background-repeat: no-repeat;
    background-position: 15px 15px;
  }
  .searchForm-input-item:hover {
    /*box-shadow: inset 1px 1px 1px 1px rgba(0, 0, 0, 0.05);*/
    /*background-color: #fDfDfD;*/
    box-shadow: inset 1px 1px 3px rgba(0, 0, 0, 0.07), inset -1px -1px 3px rgba(0, 0, 0, 0.07);
    transition: box-shadow .1s ease-in-out;
  }
  .searchForm-input-item:focus {
    outline-color: rgba(255, 153, 0, 0.5);
    outline-offset: 1.5px;
  }
  .searchForm-input-item:nth-child(1){
    background-image: url("../assets/icons/town.svg");
    background-size: 25px 24px;
  }
  .searchForm-input-item:nth-child(2){
    background-image: url("../assets/icons/university.svg");
    background-size: 25px 24px;
  }
</style>