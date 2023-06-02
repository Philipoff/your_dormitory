<template>
  <div class="dormReviewCard item-card">
    <div class="card-header-inner">
      <div class="card-info">
        <div class="userCard">
          <img class="userCard-img" src="../assets/img/user2.png" alt="">
          <div class="userCard-fioDate">
            <div class="usercard-name">Сергей</div>
            <div class="usercard-surname">Кириллов</div>
            <div class="userCard-date">27.05.23</div>
          </div>
        </div>
        <div class="review-rate">3.2</div>
      </div>
      <div class="review-text">
        <div>Просто ужасно... Я не знаю, как тут живут люди, это просто клоповник какой-то.</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "DormReviewCard"
}
</script>

<style scoped>
.dormReviewCard{
  padding: 40px;

}
.userCard {
  display: flex;
  align-items: center;
}
.card-info{
  display: flex;
  justify-content: space-between;
}
.userCard-fioDate{
  display: flex;
  flex-direction: column;
  font-size: 24px;
  line-height: 24px;
  margin-left: 40px;
  color: #000000;
  font-weight: 400;
}
.userCard-date{
  color: #878787;
  font-weight: 300;
  margin-top: 10px;
}
.userCard-img {
  width: 100px;
  height: 100px;
}
.review-rate{
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100px;
  width: 100px;
  font-size: 32px;
  font-weight: 500;
  background-image: url("../assets/icons/rate.svg");
  background-size: 100px 100px;
  background-repeat: no-repeat;
}
.review-text {
  margin-top: 20px;
  font-size: 22px;
}
</style>