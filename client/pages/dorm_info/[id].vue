<template>
  <div class="main">
    <div class="content">
      <div class="main-content">
        <DormInfoCard :dorm="getDorm"></DormInfoCard>

        <div class="main-content__blocks">

          <div class="main-content-block-item">
            <DormReviews></DormReviews>
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
import DormInfoCard from "../../components/DormInfoCard";
import DormReviews from "../../components/DormReviews";
export default {
  name: "index.vue",
  components: {DormReviews, DormInfoCard},
  computed: {
    getDorm(){
      return {
        id:"1",
        university:"СПбГЭТУ 'ЛЭТИ'",
        title:"Общежитие №1",
        address:"1-й Муринский пр., д. 1",
        subway:"ст. м. Лесная",
        rate:"4.8",
      }
    }
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