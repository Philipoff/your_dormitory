<template>
  <div class="lastReview-card">
    <div class="card-header-inner">
      <div class="header__titles">
        <div class="card-university">СПбГЭТУ "ЛЭТИ"</div>
        <div class="card-title">Общежитие №4</div>
      </div>
      <div class="header__date">23.02.23</div>
    </div>
    <div class="card-info">
      <div class="userCard">
        <img class="userCard-img" src="../assets/img/user.png" alt="">
        <div class="userCard-fio">
          <div class="usercard-name">Иван</div>
          <div class="usercard-surname">Андреев</div>
        </div>
      </div>
      <div class="review-rate">3,9</div>
    </div>
    <div class="review-text">
      <div>Если собираетесь провести студенческие годы здесь, то это хороший выбор! В общежитии сделан ремонт... Если собираетесь провести студенческие годы здесь, то это хороший выбор! В общежитии сделан ремонт...
      </div>
      <button class="un">Читать далее..</button>

    </div>

  </div>
</template>

<script>
</script>

<style scoped>
  .lastReview-card{
    background: #FFFFFF;
    border: 1px solid #E0E0E0;
    border-radius: 10px;
    padding: 25px 20px;
    margin-bottom: 20px;
    display: flex;
    flex-direction: column;
    width: 100%;
    font-size: 16px;
    transition: background .3s ease-in-out;
  }
  .lastReview-card:hover {
    box-shadow: inset 1px 1px 5px rgba(0, 0, 0, 0.03), inset -1px -1px 5px rgba(0, 0, 0, 0.03);
    transition: box-shadow .3s ease-in-out;
  }
  .card-header-inner {
    display: flex;
    justify-content: space-between;
  }
  .card-university{font-weight: 500; margin-bottom: 6px;}
  .card-info{
    display: flex;
    justify-content: space-between;
    margin-top: 19px;
  }
  .header__date {
    font-weight: 300;
    font-size: 14px;
    line-height: 14px;
  }
  .userCard {
    display: flex;
    align-items: center;
  }
  .userCard-fio{
    display: flex;
    flex-direction: column;
    line-height: 16px;
    margin-left: 10px;
    color: #000000;
    font-weight: 400;
  }
  .userCard-img {
    width: 60px;
    height: 60px;
  }
  .review-rate{
    display: flex;
    justify-content: center;
    align-items: center;
    height: 60px;
    width: 60px;
    font-size: 20px;
    font-weight: 500;
    background-image: url("../assets/icons/rate.svg");
    background-size: 60px 60px;
    background-repeat: no-repeat;
  }
  .review-text {
    margin-top: 18px;
  }
  .review-text > div {
    height: 65px;
    width: 261px;
    line-height: 16px;
    text-overflow: ellipsis;
    overflow: hidden;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
  }
  .review-text > button {
    color: #FF9900;
    font-size: inherit;
  }
  .un::after{
    background: #FF990080;
    transition: 200ms ease-in-out;
  }
</style>