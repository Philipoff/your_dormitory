<template>
  <div class="dormReviews">
    <div class="dormReviews-header section-header">
      <div class="header-text">Отзывы</div>

    </div>
    <div class="dormReviews-cards">
      <DormReviewCard class="dormReviews-cards__item"></DormReviewCard>
      <DormReviewCard class="dormReviews-cards__item"></DormReviewCard>
      <DormReviewCard class="dormReviews-cards__item"></DormReviewCard>
    </div>
  </div>
</template>

<script>
import DormReviewCard from "./DormReviewCard";
export default {
  name: "DormReviews",
  components: {DormReviewCard}
}
</script>

<style scoped>
.dormReviews-cards__item{
  margin-bottom: 20px;
}
.dormReviews {width: 100%;}
.dormReviews-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;

}
</style>