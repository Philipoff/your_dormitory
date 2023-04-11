<template>
  <div class="dormCard">
    <img class="dorm-img" src="../assets/img/dorm.png" alt="Dormitory photo">

    <div class="dorm-info">
      <div class="dorm-info-describe">
        <div class="dorm-info-item dorm-university">СПбГЭТУ "ЛЭТИ"</div>
        <div class="dorm-info-item dorm-title">Общежитие №1</div>
        <div class="dorm-address">
          <svg class="dorm-address__svg" width="35" height="35" viewBox="0 0 35 35" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M29.1665 14.5834V28.6251C29.1665 29.7297 28.2711 30.6251 27.1665 30.6251H7.83317C6.7286 30.6251 5.83317 29.7297 5.83317 28.6251V14.5834M32.0832 17.5001L17.4998 2.91675L2.9165 17.5001" stroke="#212121" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M13.125 30.625V17.5H21.875V30.625" stroke="#212121" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M23.3335 8.75V4.375H27.7085V13.125" stroke="#212121" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          <div class="dorm-address__title">1-й Муринский пр., д. 1</div>
        </div>
        <div class="dorm-info-item dorm-subway">ст.м. Лесная</div>
        <button class="dorm-add-fav-button">
          <svg class="dorm-add-fav-button__svg" width="35" height="35" viewBox="0 0 35 35" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6.49073 20.2827L16.8155 29.9817C17.1399 30.2865 17.3021 30.4389 17.5002 30.4389C17.6982 30.4389 17.8604 30.2865 18.1848 29.9817L28.5096 20.2827C31.3624 17.6029 31.7088 13.1929 29.3095 10.1004L28.8583 9.51896C25.9881 5.81951 20.2267 6.43994 18.2099 10.6657C17.925 11.2626 17.0753 11.2626 16.7904 10.6657C14.7736 6.43994 9.01226 5.81952 6.142 9.51896L5.69086 10.1004C3.29155 13.1929 3.63797 17.6029 6.49073 20.2827Z" stroke="#212121" stroke-width="2"/>
          </svg>
          <div class="dorm-add-fav-button__title">Добавить в Избранное</div>
        </button>

      </div>
      <div class="dorm-info-rate">
        <div class="circle-rate">4,8</div>
        <button class="reviews-button un">Посмотреть отзывы&emsp;></button>
      </div>
    </div>
  </div>
</template>

<script>

</script>

<style scoped>
  .dormCard {
    max-width: 1187px;
    background: #FFFFFF;
    border: 1px solid #E0E0E0;
    border-radius: 5px;
    padding: 40px 53px 40px 40px;
    margin-bottom: 20px;
    display: flex;
    box-shadow: none;
    transition: box-shadow .3s ease-in-out;
  }
  .dormCard:hover {
    box-shadow: inset 1px 1px 5px rgba(0, 0, 0, 0.05), inset -1px -1px 5px rgba(0, 0, 0, 0.05);
    transition: box-shadow .3s ease-in-out;
  }
  .dorm-img{
    width: 356px;
    height: 220px;
    margin-right: 40px;
  }
  .dorm-info{
    display: flex;
    justify-content: space-between;
    width:100%;
    font-size: 24px;
  }
  .dorm-university {
    margin-bottom: 11px;
    font-weight: 500;
    line-height: 100%;
  }
  .dorm-title{margin-bottom: 39px;line-height: 100%;}
  .dorm-subway {margin-bottom: 18px;}
  .dorm-subway  {
    padding-left: 48px;
  }

  .dorm-add-fav-button, .dorm-address {
    font-size: inherit;
    display: flex;
    align-items: center;
  }
  .dorm-add-fav-button__svg, .dorm-address__svg{
    margin-right: 13px;
  }
  .dorm-address:hover > svg{
    /*fill: #c9c9c950;*/
  }
  button:hover > svg{
    /*fill: #C4C4C4A0;*/
    fill: #FF9900;
  }

  .dorm-info-rate {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
  }
  .circle-rate {
    margin-top: 35px;
    margin-bottom: 54px;
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
  .reviews-button {
    font-size: inherit;
    text-decoration: none;
    transition: text-decoration .5s ease-in-out;
  }
</style>