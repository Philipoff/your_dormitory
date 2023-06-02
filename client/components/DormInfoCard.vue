<template>
  <div class="dorm-info-card">
    <div class="flex-wrapper-one">
      <div class="flex-wrapper-four">
        <p class="dorm-title">{{dorm.title}}</p>
        <p class="dorm-university">{{dorm.university}}</p>
        <div class="dorm-address-inner">
          <AddressSvg class="basic-home-house"></AddressSvg>
          <div class="dorm-address">{{dorm.address}}</div>
        </div>
        <div class="dorm-subway-inner">
          <SubwaySvg
              class="free-icon-paris-transport-metro-logo-508"
          />
          <div class="dorm-subway">{{dorm.subway}}</div>
        </div>
        <a class="dorm-map-link" href="https://yandex.ru/maps" target="_blank">Посмотреть на карте...</a>
        <p class="dorm-phone">&#43;7 (812) 295-42-30</p>
        <VkLogo class="vk-1-logo-svgrepo-com-1" />
      </div>
      <div class="flex-wrapper-two">
        <img
            alt=""
            class="dorm-image"
            src="../assets/img/dorm2.png"
        />
      </div>
      <div class="dorm-widget">
        <p class="rate">3,8/5</p>
        <p class="rate-description">12 оценок</p>
        <div class="flex-wrapper-three">
          <button class="write-review-button"
                  type="button"
                  data-bs-toggle="modal"
                  data-bs-target="#reviewModal"
          >
            <svg width="35" height="35" viewBox="0 0 35 35" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd" clip-rule="evenodd" d="M29.3749 0.744556C30.3084 1.19247 31.4103 1.84106 32.2864 2.71718C33.1643 3.5951 33.8129 4.69518 34.2572 5.62864C34.818 6.80039 34.4543 8.15131 33.5387 9.06864L20.6137 21.9919C20.0582 22.5473 19.381 22.9612 18.6339 23.2013L11.0695 25.6254C10.8342 25.7009 10.5827 25.71 10.3425 25.6518C10.1024 25.5937 9.88295 25.4704 9.70833 25.2956C9.53371 25.1208 9.41067 24.9012 9.35273 24.661C9.29479 24.4208 9.3042 24.1693 9.37992 23.9341L11.804 16.3715C12.0433 15.6249 12.4573 14.9461 13.0116 14.3917L25.9367 1.4666C26.854 0.549265 28.205 0.187348 29.3767 0.746348L29.3749 0.744556ZM29.753 5.25239C29.3104 4.8343 28.8109 4.48084 28.2695 4.20247L15.7385 16.7334C15.6112 16.8605 15.5037 17.0061 15.4196 17.1652L12.7375 22.2661L17.8366 19.5857C17.9978 19.5015 18.143 19.394 18.2702 19.2668L30.8011 6.73589C30.5227 6.19444 30.171 5.69501 29.753 5.25239ZM3.95654 6.85414C3.95616 6.62528 4.04337 6.40496 4.2003 6.23837C4.35722 6.07179 4.57195 5.97158 4.80042 5.95831L14.7083 5.96726C15.1835 5.96726 15.6392 5.7785 15.9752 5.4425C16.3112 5.10649 16.5 4.65078 16.5 4.1756C16.5 3.70042 16.3112 3.2447 15.9752 2.9087C15.6392 2.5727 15.1835 2.38393 14.7083 2.38393L4.85417 2.37497C3.66622 2.37497 2.52692 2.84688 1.68692 3.68689C0.846911 4.5269 0.375 5.66619 0.375 6.85414V29.3879C0.375 30.7496 0.521917 31.5111 0.946542 32.303C1.34787 33.0537 1.94629 33.6539 2.697 34.0552C3.48892 34.4781 4.24858 34.625 5.61204 34.625H27.388C28.7496 34.625 29.5111 34.4781 30.303 34.0552C31.0555 33.6539 31.6539 33.0537 32.0552 32.303C32.4781 31.5111 32.625 30.7514 32.625 29.3879V20.2916C32.625 19.8165 32.4362 19.3607 32.1002 19.0247C31.7642 18.6887 31.3085 18.5 30.8333 18.5C30.3582 18.5 29.9024 18.6887 29.5664 19.0247C29.2304 19.3607 29.0417 19.8165 29.0417 20.2916V29.3879C29.0417 30.2103 29.004 30.411 28.8947 30.6134C28.8326 30.7342 28.7342 30.8325 28.6135 30.8947C28.411 31.0022 28.2103 31.0416 27.388 31.0416H5.61204C4.78967 31.0416 4.59079 31.0022 4.38654 30.8947C4.2657 30.8326 4.16733 30.7343 4.10525 30.6134C3.99775 30.411 3.95833 30.2103 3.95833 29.3879L3.95654 6.85414Z" fill="#212121"/>
            </svg>
          </button>
          <FavButton :dorm-id="dormId" :is-needed-btn-text="false" :is-bigger-size="true"></FavButton>
        </div>
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
    dormId: {
      type: String,
      required: true
    },
    dorm: {
      title: String,
      id: String,
      university: String,
      address: String,
      subway: String,
      rate: String
    }
  }
  // review: {userId, rate, reviewText} POST
  //
}
</script>

<style scoped>

.dorm-info-card {
  margin-top: 120px;
  padding: 0;
  position: relative;
  font-size: 24px;
}
.dorm-widget {
  /*padding: 105px 300px 300px 113px;*/
  padding-right: 70px;
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
  line-height: 100%;
  /*//@include rubik-32-medium;*/
}
.rate-description {
  width: 114px;
  color: #FF9900;
  margin-bottom: 14px;
  line-height: 100%;
  /*include rubik-24-regular;*/
}
.flex-wrapper-three {
  margin-bottom: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
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
}
.dorm-university {
  width: 456px;
  color: #FF9900;
  font-size: 24px;
  line-height: 100%;
  margin-bottom: 50px;
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
}
.dorm-map-link {
  width: 315px;
  color: #FF9900;
  margin-bottom: 66px;
}
.dorm-phone {
  margin-bottom: 20px;
  margin-left: 1px;
}
.vk-1-logo-svgrepo-com-1 {
  padding: 1.06px 1.07px 1.07px 1.06px;
  position: relative;
}
.flex-wrapper-two {
  border-radius: 0px 9px 9px 0px;
  display: flex;
  align-items: flex-start;
}
.dorm-image {
  width: 957px;
  height: 591px;
  border-radius: 0px 9px 9px 0px;
}
.write-review-button { margin-right: 20px;}
</style>