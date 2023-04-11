<template>
  <div class="main">
    <div class="content">
      <div class="bg"></div>
      <div class="main-content">
        <div class="main-content__header" id="header">
          Поможем найти <span class="gradient-text">идеальное</span> общежитие
        </div>
        <SearchForm @loadedDormitories="updateCatalog"></SearchForm>
        <div class="main-content__blocks">

          <div class="main-content-block-item">
            <Catalog :dormitories="dormitories"></Catalog>
          </div>
          <div class="main-content-block-item">
            <LastReviews></LastReviews>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  export default {
    mounted() {
      const h = document.getElementById('header')
      h?.classList.add('smoothAppearance')
    },
    data(){
      return {
        dormitories: []
      }
    },
    methods: {
      updateCatalog(res){
        this.dormitories = res
      }
    }
  }
</script>
<style scoped>
  .main-content {
    margin-top: 120px;
    margin-bottom: 238px;
  }
  .main {
    background-image: url('../assets/bg/bg_up.svg'), url('../assets/bg/bg_down.svg');
    background-size:  1753px 1739px, 1353px 1339px;
    background-repeat: no-repeat, no-repeat;
    background-position: top -390px left 205px, bottom -595px left 15px;
  }
  .main-content__header{
    font-weight: 500;
    font-size: 96px;
    width: 900px;
    line-height: 96px;
    margin-bottom: 75px;
    opacity: 0;
    padding-left: 20px;
  }
  .main-content__blocks {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    width: 100%;
    margin-top: 100px;
  }
  .main-content-block-item:nth-child(1) {
    margin-right: 84px;
    width:79%;
    justify-self: flex-start;
  }
  .main-content-block-item:nth-child(2) {
    width: 21%;
    justify-self: flex-end;
  }
  .smoothAppearance {
    display: block;
    opacity: 1;
    padding-left: 0;
    transition: opacity .5s ease-in, padding-left .7s ease-in-out;
  }


  @media screen and (max-width: 680px) {
    .main-content {
      width: 90%;
      margin: 0 auto;
      margin-top: 25px;
      margin-bottom: 25px;
    }
  }
</style>
