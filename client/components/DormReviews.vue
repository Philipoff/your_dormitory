<template>
  <div class="dormReviews">
    <div class="dormReviews-header section-header">Отзывы</div>
    <div class="dormReviews-cards">
      <DormReviewCard class="dormReviews-cards__item"></DormReviewCard>
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
</style>