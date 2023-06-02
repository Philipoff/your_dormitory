<template>
  <div class="favBtn__inner">
    <button class="dorm-add-fav-button" @click.stop="onClickFav()">
      <svg class="dorm-add-fav-button__svg" :id="htmlBtnId" :width="isBiggerSize? 50:35" :height="isBiggerSize? 50:35" viewBox="0 0 35 35" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M6.49073 20.2827L16.8155 29.9817C17.1399 30.2865 17.3021 30.4389 17.5002 30.4389C17.6982 30.4389 17.8604 30.2865 18.1848 29.9817L28.5096 20.2827C31.3624 17.6029 31.7088 13.1929 29.3095 10.1004L28.8583 9.51896C25.9881 5.81951 20.2267 6.43994 18.2099 10.6657C17.925 11.2626 17.0753 11.2626 16.7904 10.6657C14.7736 6.43994 9.01226 5.81952 6.142 9.51896L5.69086 10.1004C3.29155 13.1929 3.63797 17.6029 6.49073 20.2827Z" stroke="#212121" stroke-width="2"/>
      </svg>
      <div class="dorm-add-fav-button__title" v-if="$props.isNeededBtnText">
        {{this.isFavourite? 'Удалить из Избранного' : 'Добавить в Избранное' }}
      </div>
    </button>
  </div>
</template>

<script>
export default {
  name: "FavButton",
  data(){
    return {
      isFavourite: false,
    }
  },
  props: {
    dormId: {
      type: String,
      required: true
    },
    isNeededBtnText: {
      type: Boolean,
      required: true
    },
    isBiggerSize: {
      type: Boolean,
      required: false
    }
  },
  computed: {
    htmlBtnId(){
      return `favSvg${this.$props.dormId}`
    },
  },
  mounted() {
    const favs = localStorage.getItem('favs')
    let isInLocalStorage = -1;
    if(favs){
      isInLocalStorage = favs.indexOf(this.$props.dormId)
    }
    this.isFavourite = isInLocalStorage !== -1;
    if (this.isFavourite){
      const favSvg = document.getElementById(this.htmlBtnId)
      favSvg.classList.add('fav-filled')
    }



  },
  methods: {
    onClickFav(){
      const favSvg = document.getElementById(this.htmlBtnId)
      let favList = localStorage.getItem('favs')
      // const authText = document.getElementById('loginBtnText')
      // if(authText.innerText === 'Выйти'){
      if (!this.isFavourite) {
        favSvg.classList.add('fav-filled')

        if (!favList){
          favList = ''
          favList += this.$props.dormId + '-'
        } else {
          if(favList.indexOf(this.$props.dormId) === -1)
            favList += this.$props.dormId + '-'
        }

      } else {
        favSvg.classList.remove('fav-filled')
        if (favList){
          let ind = favList.indexOf(this.$props.dormId)
          if( ind !== -1) {
            favList = favList.replace(this.$props.dormId + '-', '')
          }
        }
      }
      this.isFavourite = !this.isFavourite
      localStorage.setItem('favs', favList)
    } /*else {
      this.$emit('authModalNeeded')
    }*/
    // }
  }
}
</script>

<style scoped>
.dorm-add-fav-button {
  font-size: inherit;
  display: flex;
  align-items: center;
}
.dorm-add-fav-button__svg {
  margin-right: 13px;
}

button:hover > svg, .fav-filled{
  fill: #FF9900;
}
.favBtn__inner:active{
  transform: scale(103%);
}
.favBtn__inner{
  transform: scale(100%);
  transition: transform 0.5ms ease-in;
}
</style>