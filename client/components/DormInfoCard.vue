<template>
  <div class="dorm-info-card">
    <div class="dorm-widget">
      <p class="rate">3,8/5</p>
      <p class="rate-description">12 оценок</p>
      <div class="flex-wrapper-three">
        <div class="write-svgrepo-com-1">
          <img
              alt=""
              class="vector"
              src="https://static.overlay-tech.com/assets/ff0c3ecc-2dab-42ef-8584-910be805a80d.svg"
          />
        </div>
        <FavButton>Добавить</FavButton>
      </div>
    </div>
    <div class="flex-wrapper-one">
      <div class="flex-wrapper-four">
        <p class="dorm-title">Общежитие №4</p>
        <p class="dorm-university">СПбГЭТУ “ЛЭТИ”</p>
        <div class="dorm-address-inner">
          <AddressSvg class="basic-home-house"></AddressSvg>
          <div class="dorm-address">Студенческая улица, 3</div>
        </div>
        <div class="dorm-subway-inner">
          <SubwaySvg
              class="free-icon-paris-transport-metro-logo-508"
          />
          <div class="dorm-subway">Лесная</div>
        </div>
        <a class="dorm-map-link" href="https://yandex.ru/maps" target="_blank">Посмотреть на карте...</a>
        <p class="dorm-phone">&#43;7 (812) 295-42-30</p>
        <VkLogo class="vk-1-logo-svgrepo-com-1" />
      </div>
      <div class="flex-wrapper-two">
        <img
            alt=""
            class="dorm-image"
            src="https://static.overlay-tech.com/assets/553080f8-f35a-4fa0-8557-fa9b1a5f2da4.png"
        />
      </div>
    </div>
  </div>
</template>

<script>
import AddressSvg from "./icons/AddressSvg";
import FavButton from "./ui/FavButton";
import SubwaySvg from "./icons/SubwaySvg";
import VkLogo from "./icons/VkLogo";
export default {
  name: "DormInfoCard",
  components: {VkLogo, SubwaySvg, FavButton, AddressSvg},
  props: {
    dorm: Object
  }
}
</script>

<style scoped>
/*.dormInfoCard{*/
/*  margin-top: 120px;*/
/*  border: 1px solid rgba(255, 153, 0, 0.5);*/
/*  padding: 83px;*/
/*  background-color: white;*/
/*  width: 100%;*/

/*}*/
/*.dorm-info-card__columns{*/
/*  display: flex;*/

/*}*/
/*.card-columns-item:nth-child(1){*/
/*  width: 40%;*/
/*}*/
/*.card-columns-item:nth-child(2) {*/
/*  width: 60%;*/
/*  background-image: url("../assets/img/dorm.png"), linear-gradient(90deg, #FFFFFF 0%, rgba(255, 255, 255, 0) 50%);;*/
/*  background-size: 949px 591px;*/
/*  background-repeat: no-repeat;*/
/*}*/

.dorm-info-card {
  margin-top: 120px;
  padding: 0;
  position: relative;
  font-size: 24px;
}
.dorm-widget {
  background-size: 100% 100%;
  background-position: center;
  background: url("https://static.overlay-tech.com/assets/acd09052-6179-43e9-9553-5c330a3e42dd.svg"),
  url("https://static.overlay-tech.com/assets/f92cf727-c429-4ad3-9ff8-6774ee7291b1.svg");
  padding: 105px 300px 300px 113px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  position: absolute;
  right: 0;
  bottom: 0;
}
.rate {
  width: 86px;
  color: #000000;
  text-align: center;
  margin-bottom: 10px;
  margin-left: 14px;
  font-weight: 500;
  font-size: 32px;
  /*//@include rubik-32-medium;*/
}
.rate-description {
  width: 114px;
  color: #FF9900;
  margin-bottom: 19px;
  /*include rubik-24-regular;*/
}
.flex-wrapper-three {
  margin-bottom: 36px;
  display: flex;
  align-items: center;
}
.write-svgrepo-com-1 {
  margin-right: 28px;
  padding: 3.48px 3.47px 5.38px 5.38px;
  display: flex;
  align-items: center;
}
.vector {
  flex: 1;
  align-self: stretch;
  object-fit: cover;
}
.flex-wrapper-one {
  background-color: #FFF;
  border-radius: 10px;
  padding: 0 0 0 82px;
  display: flex;
  align-items: flex-start;
  position: relative;
  border: 1px solid #FFCC7F;
}
.flex-wrapper-four {
  margin-right: 83px;
  padding: 82px 0 0;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}
.dorm-title {
  width: 456px;
  margin-bottom: 30px;
  font-weight: 500;
  font-size: 32px;
  line-height: 100%;
  /*//@include rubik-32-medium;*/
}
.dorm-university {
  width: 456px;
  color: #FF9900;
  font-size: 24px;
  line-height: 100%;
  margin-bottom: 50px;
  /*//@include rubik-24-regular;*/
}
.dorm-address-inner {
  margin-bottom: 30px;
  display: flex;
  align-items: center;
}
.basic-home-house {
  width: 35px;
  height: 35px;
  margin-right: 15px;
}
.dorm-address {
  width: 401px;
  /*//@include rubik-24-regular;*/
}
.dorm-subway-inner {
  margin-bottom: 30px;
  margin-left: 1px;
  display: flex;
  align-items: center;
}
.free-icon-paris-transport-metro-logo-508 {
  width: 32px;
  height: 32px;
  margin-right: 17px;
}
.dorm-subway {
  width: 310px;
  /*//@include rubik-24-regular;*/
}
.dorm-map-link {
  width: 315px;
  color: #FF9900;
  margin-bottom: 66px;
  /*//@include rubik-24-regular;*/
}
.dorm-phone {
  margin-bottom: 20px;
  margin-left: 1px;
  /*//@include rubik-24-regular;*/
}
.vk-1-logo-svgrepo-com-1 {
  padding: 1.06px 1.07px 1.07px 1.06px;
  position: relative;
}
.flex-wrapper-two {
  background: linear-gradient(
  90deg,
  #FFF 0%,
  #FFF 50%
  );
  border-radius: 0px 9px 9px 0px;
  display: flex;
  align-items: flex-start;
}
.dorm-image {
  width: 949px;
  height: 591px;
  border-radius: 0px 9px 9px 0px;
}
</style>