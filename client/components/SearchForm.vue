<script setup>
  const emit = defineEmits(['loadedDormitories'])
</script>

<template>
  <div class="searchForm">
    <div class="serachForm-content">
      <div class="searchForm-header">Поиск общежития</div>

      <div class="searchForm-input__inner">
        <input class="searchForm-input-item" placeholder="Город" v-model="searchForm.city"/>
        <input class="searchForm-input-item" placeholder="Вуз" v-model="searchForm.university"/>

        <button class="searchForm-button" @click="loadCatalog()">Найти</button>
      </div>
    </div>
  </div>
</template>

<script>
import {useFetch, useRuntimeConfig} from "nuxt/app";

export default {
  data(){
    return {
      searchForm: {
        city: "",
        university: ""
      }
    }
  },
  methods: {
    async loadCatalog(){
      let data = {city: this.searchForm.city, university: this.searchForm.university}
      console.log('dataSearchForCatalog: ', data)

      const config = useRuntimeConfig();
      //let url1 = config.public.baseURL + '/api/dormitories'
      let url = "https://run.mocky.io/v3/f5dfc5b8-fdce-49da-9153-226e019f264e"


      try{

        const res = await $fetch(url, {
          method: 'POST',
          body: data,
          headers: {
            'Content-Type': 'application/json'
          }
        })
          /*[
            {
              "university": "СПбГЭТУ 'ЛЭТИ'",
              "title": "Общежитие 1",
              "address": "1-й Муринский пр., д. 1",
              "subway": "ст. м. Лесная",
              "rate": "4.8"
            }
          ]*/
        if(res){
          this.$emit('loadedDormitories', res)
          console.log('Загрузка общежитий прошла успешно')
        } else {
          console.log('Пустой список общежитий.')
        }
      } catch(error){
        alert('При загрузке общежитий что-то пошло не так... \nStatus-code: ' + error.status)
        console.log(error.message)
      }
    }
  },
  created() {
    this.loadCatalog()
  }
}
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
    width: 420px;
    padding: 15px;
    font-size: 20px;
    line-height: 20px;
    margin-right: 66px;
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
  .searchForm-button {
    line-height: 20px;
    background-color: #FF9900;
    color: #FFFFFF;
    font-weight: 400;
    border-radius: 5px;
    padding: 15px 75px;
    margin-left: -30px;
    font-size: 20px;
    box-shadow: none;
  }
  .searchForm-button:hover {
    background-color: #FF9900F0;
    box-shadow: inset 1px 1px 5px rgba(0, 0, 0, 0.03), inset -1px -1px 5px rgba(0, 0, 0, 0.03);
    transition: box-shadow .3s ease-in-out;
  }
</style>