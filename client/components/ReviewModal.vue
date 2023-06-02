<template>
  <div class="modal fade" id="reviewModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-body">
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          <div >
            <form id="ratingForm" action="#" @submit.prevent="onClickSendReview()">
              <div class="rating-header">Оцените общежитие по пятибалльной шкале</div>
              <div class="rating__inner">
                <div class="rating-area" >

                  <input type="radio" id="star-5" name="rating" value="5" v-model="rate">
                  <label for="star-5" title="Оценка «5»"></label>
                  <input type="radio" id="star-4" name="rating" value="4" v-model="rate">
                  <label for="star-4" title="Оценка «4»"></label>
                  <input type="radio" id="star-3" name="rating" value="3" v-model="rate">
                  <label for="star-3" title="Оценка «3»"></label>
                  <input type="radio" id="star-2" name="rating" value="2" v-model="rate">
                  <label for="star-2" title="Оценка «2»"></label>
                  <input type="radio" id="star-1" name="rating" value="1" v-model="rate">
                  <label for="star-1" title="Оценка «1»"></label>
                </div>
              </div>
              <textarea v-model="text" placeholder="Добавьте описание к отзыву... (необязательно)"></textarea>
              <div class="btnsArea">
                <button class="sendReviewButton" type="submit">Отправить отзыв</button>
              </div>

            </form>


          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {useRuntimeConfig} from "nuxt/app";

export default {
  name: "ReviewModal",
  data(){
    return {
      isOpenReviewModal: false,
      text: '',
      rate: ''
    }
  },
  props: {
    dormId: String
  },
  methods: {
    async onClickSendReview(){

      if (this.rate) {
        let data = {userId: 1, rate: this.rate, text: this.text}
        console.log('On server sent dataForReview: ', data)

        //const config = useRuntimeConfig();
        //let url = config.public.baseURL + `/api/reviews/${this.$props.dormId}`
        let url = "https://run.mocky.io/v3/8f4d5831-0bbd-4579-a6e0-6eabab22fea0"

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
              "rate": "5",
              "userId": "1",
              "text": ""
            }
          ]*/
          if(res){
            this.$emit('addedReview', data)
            console.log('Добавление отзыва прошло успешно')
          }
        } catch(error){
          alert('При отправке отзыва что-то пошло не так... \nStatus-code: ' + error.status)
          console.log(error.message)
        }
        this.closeReviewModal()
      } else{
        alert('Перед тем, как отправить отзыв, поставьте оценку общежитию.')
        return
      }
    },
    closeReviewModal(){
      let myModalEl = document.getElementById('reviewModal')
      let myModal = bootstrap.Modal.getInstance(myModalEl)
      myModal.hide();
    }
  }
}
</script>

<style scoped>
.modal-dialog{width:700px;}
.modal-content {
  border-radius: 10px;
  border: none;
}
.modal-body{
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 40px 40px 25px 40px;
  width: 100%;
}
.btn-close {
  align-self: flex-end;
}
.btn-close:active{border: none;}
/* -------Для отрисовки звезд и применения стилей-------*/
.rating-header {
  font-size: 24px;
  text-align: center;
  margin-top: 20px;
}
#ratingForm {width: 100%;}
.rating__inner {
  display: flex;
  justify-content: center;
}
.rating-area {
  overflow: hidden;
  margin: 0 auto;
}
.rating-area:not(:checked) > input {
  display: none;
}
.rating-area:not(:checked) > label {
  float: right;
  width: 54px;
  padding: 0;
  cursor: pointer;
  font-size: 48px;
  line-height: 48px;
  color: lightgrey;
  text-shadow: 1px 1px #bbb;
}
.rating-area:not(:checked) > label:before {
  content: '★';
}
.rating-area > input:checked ~ label {
  color: gold;
  text-shadow: 1px 1px #c60;
}
.rating-area:not(:checked) > label:hover,
.rating-area:not(:checked) > label:hover ~ label {
  color: gold;
}
.rating-area > input:checked + label:hover,
.rating-area > input:checked + label:hover ~ label,
.rating-area > input:checked ~ label:hover,
.rating-area > input:checked ~ label:hover ~ label,
.rating-area > label:hover ~ input:checked ~ label {
  color: gold;
  text-shadow: 1px 1px goldenrod;
}
.rate-area > label:active {
  position: relative;
}
/* ---------------------------------------------*/
textarea {
  width:100%;
  resize: vertical;
  padding:15px;
  border-radius:15px;
  border:0;
  box-shadow:4px 4px 10px rgba(0,0,0,0.06);
  height:150px;
  margin-top: 20px;
}
textarea:focus {
  outline: none !important;
  border:1px solid #FF990090;
  box-shadow: 0 0 10px #FFCC7F50;
}
.sendReviewButton {
  background: #FF9900;
  border-radius: 6px;
  padding: 10px 20px;
  width: max-content;
  color: #FFFFFF;
}
.btnsArea {
  width: 100%;
  display: flex;
  justify-content: center;
  margin-top: 20px;
}
</style>