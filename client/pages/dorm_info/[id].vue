<template>
  <div class="main">
    <div class="content">
      <div class="main-content">
        <DormInfoCard :dorm="infoDorm" :dorm-id="dormId"></DormInfoCard>

        <div class="main-content__blocks">

          <div class="main-content-block-item">
            <DormReviews></DormReviews>
          </div>
          <div class="main-content-block-item">
            <LastReviews :reviews="reviews"></LastReviews>
          </div>
        </div>
        <ReviewModal @addedReview="addNewReview()" :dormId="dormId"></ReviewModal>
      </div>
    </div>
  </div>
</template>

<script>
import DormInfoCard from "../../components/DormInfoCard";
import DormReviews from "../../components/DormReviews";
import {useFetch, useRuntimeConfig} from "nuxt/app";
import ReviewModal from "../../components/ReviewModal";
export default {
  name: "index.vue",
  components: {ReviewModal, DormReviews, DormInfoCard},
  computed: {
    dormId(){
      return this.$route.params.id
    }
  },
  data(){
    return {
      infoDorm: {},
      reviews: []
    }
  },
  methods: {
    async loadInfoDorm() {
      const config = useRuntimeConfig();
      //let url1 = config.public.baseURL + `/api/dormitories/${this.dormId}`
      let url;
      //let url = "https://run.mocky.io/v3/8f4d5831-0bbd-4579-a6e0-6eabab22fea0";
      //если с сервером будет всё плохо
      switch(this.dormId){
        case '1':
          url = "https://run.mocky.io/v3/55401b2d-1c17-46ea-b075-60c1b828b09f"
          //url ="https://run.mocky.io/v3/c568be24-0f34-404e-85d7-f95529ccc2c1"
          break;
        case '2':
          url = "https://run.mocky.io/v3/4ff3c9b1-b061-4fc7-8a9d-2215bded1c9e"
          break;
        case '3':
          url = "https://run.mocky.io/v3/42a194c8-5147-4365-b73b-49dde4123f5b"
          break;
        case '4':
          url = "https://run.mocky.io/v3/78e50d69-a8ca-40aa-920b-f991b951d0a0"
          break;
        case '5':
          url = "https://run.mocky.io/v3/2b0a7492-a9b0-41d0-a779-d786f273a032"
          break;
      }

      const {data: gotInfoDorm} = await useFetch(url)
      this.infoDorm = gotInfoDorm
      this.reviews = gotInfoDorm.reviews
      // return {
      //   id:"1",
      //   university:"СПбГЭТУ 'ЛЭТИ'",
      //   title:"Общежитие №1",
      //   address:"1-й Муринский пр., д. 1",
      //   subway:"ст. м. Лесная",
      //   rate:"4.8",
      //   reviews: "[]"
      // }
    },
    addNewReview(reviewObj){
      this.reviews.push(reviewObj)
    }
  },
  created() {
    this.loadInfoDorm()
  }
}
</script>

<style scoped>
.main-content {
  margin-bottom: 238px;
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
</style>