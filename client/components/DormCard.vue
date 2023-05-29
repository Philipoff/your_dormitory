<template>
  <div class="dormCard item-card">
    <img class="dorm-img" src="../assets/img/dorm.png" alt="Dormitory photo">

    <div class="dorm-info">
      <div class="dorm-info-describe">
        <div class="dorm-info-item dorm-university">{{$props.dormitory.university}}</div>
        <div class="dorm-info-item dorm-title">{{$props.dormitory.title}}</div>
        <div class="dorm-address">
          <AddressSvg></AddressSvg>
          <div class="dorm-address__title">{{$props.dormitory.address}}</div>
        </div>
        <div class="dorm-info-item dorm-subway">{{$props.dormitory.subway}}</div>
        <button class="dorm-add-fav-button" @click.stop="onClickFav($event, $props.dormitory.id)">
          <svg class="dorm-add-fav-button__svg" width="35" height="35" viewBox="0 0 35 35" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6.49073 20.2827L16.8155 29.9817C17.1399 30.2865 17.3021 30.4389 17.5002 30.4389C17.6982 30.4389 17.8604 30.2865 18.1848 29.9817L28.5096 20.2827C31.3624 17.6029 31.7088 13.1929 29.3095 10.1004L28.8583 9.51896C25.9881 5.81951 20.2267 6.43994 18.2099 10.6657C17.925 11.2626 17.0753 11.2626 16.7904 10.6657C14.7736 6.43994 9.01226 5.81952 6.142 9.51896L5.69086 10.1004C3.29155 13.1929 3.63797 17.6029 6.49073 20.2827Z" stroke="#212121" stroke-width="2"/>
          </svg>
          <div class="dorm-add-fav-button__title">Добавить в Избранное</div>
        </button>

      </div>
      <div class="dorm-info-rate">
        <div class="circle-rate">{{$props.dormitory.rate}}</div>
        <button class="reviews-button un">Посмотреть отзывы&emsp;></button>
      </div>
    </div>
  </div>
</template>

<script>
import RateCircleSvg from "./ui/RateCircleSvg";
import AddressSvg from "./icons/AddressSvg";
export default{
  components: {AddressSvg, RateCircleSvg},
  props: {
    dormitory: {
      id: String,
      title: String,
      university: String,
      address: String,
      subway: String,
      rate: String
    }
  },
  methods: {
    onClickFav(event, dormId){
      console.log(event, dormId)
      event.stopPropagation()
      console.log('on click fav button!')
    }
  },
  mounted(){
    console.log(this.$props.dormitory)
  }
}
</script>

<style scoped>
  .dormCard {
    max-width: 1187px;
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