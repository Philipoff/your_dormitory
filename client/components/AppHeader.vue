<template>
  <header>
    <div class="content">
      <div class="header-inner">
        <div class="header__logo">
          <NuxtLink to="/" class="header__logo">
            <img src="~/assets/logo/logo.svg" height="67px" alt="logo" />
          </NuxtLink>
        </div>

        <nav class="header__nav">
          <div class="nav__menu">
            <button class="menu-item" @click="">

              <svg class="menu-item__svg" width="25" height="25" viewBox="0 0 25 25" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M4.63596 14.4877L11.8783 21.2911L11.8783 21.2911C12.1416 21.5385 12.2733 21.6622 12.4306 21.6842C12.4765 21.6906 12.5232 21.6906 12.5691 21.6842C12.7264 21.6622 12.8581 21.5385 13.1214 21.2911L20.3637 14.4877C22.4014 12.5736 22.6488 9.42356 20.9351 7.21467L20.6128 6.79934C18.5626 4.15687 14.4474 4.60003 13.0068 7.61841C12.8033 8.04477 12.1964 8.04477 11.9929 7.61841C10.5523 4.60003 6.43705 4.15688 4.38686 6.79934L4.06462 7.21468C2.35082 9.42356 2.59827 12.5736 4.63596 14.4877Z" stroke="#212121" stroke-width="2"/>
              </svg>
              <div class="menu-item__title" >Избранное</div>
            </button>

            <!-- Button trigger AuthModal -->

            <button type="button" class="menu-item" data-bs-toggle="modal"
                    data-bs-target="#exampleModal"
                    v-if="!isAuthorized">
              <svg class="menu-item__svg" width="25" height="25" viewBox="0 0 25 25" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M7.2915 7.42908V6.69535C7.2915 4.54946 7.2915 3.47651 7.9811 2.87842C8.6707 2.28034 9.73286 2.43208 11.8572 2.73555L16.7234 3.43072C19.1795 3.7816 20.4076 3.95704 21.1412 4.80293C21.8748 5.64882 21.8748 6.88935 21.8748 9.37042V15.6295C21.8748 18.1106 21.8748 19.3511 21.1412 20.197C20.4076 21.0429 19.1795 21.2184 16.7234 21.5692L11.8572 22.2644C9.73286 22.5679 8.6707 22.7196 7.9811 22.1215C7.2915 21.5235 7.2915 20.4505 7.2915 18.3046V17.777" stroke="#212121" stroke-width="2"/>
                <path d="M16.6665 12.5L17.4474 11.8753L17.9471 12.5L17.4474 13.1247L16.6665 12.5ZM4.1665 13.5C3.61422 13.5 3.1665 13.0523 3.1665 12.5C3.1665 11.9477 3.61422 11.5 4.1665 11.5V13.5ZM13.2807 6.66699L17.4474 11.8753L15.8856 13.1247L11.719 7.91638L13.2807 6.66699ZM17.4474 13.1247L13.2807 18.333L11.719 17.0837L15.8856 11.8753L17.4474 13.1247ZM16.6665 13.5H4.1665V11.5H16.6665V13.5Z" fill="#212121"/>
              </svg>
              <div class="menu-item__title" id="loginBtnText">Войти</div>
            </button>

            <button type="button" class="menu-item"
                    @click="unauthorized"
                    v-if="isAuthorized">
              <svg class="menu-item__svg" width="25" height="25" viewBox="0 0 25 25" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M7.2915 7.42908V6.69535C7.2915 4.54946 7.2915 3.47651 7.9811 2.87842C8.6707 2.28034 9.73286 2.43208 11.8572 2.73555L16.7234 3.43072C19.1795 3.7816 20.4076 3.95704 21.1412 4.80293C21.8748 5.64882 21.8748 6.88935 21.8748 9.37042V15.6295C21.8748 18.1106 21.8748 19.3511 21.1412 20.197C20.4076 21.0429 19.1795 21.2184 16.7234 21.5692L11.8572 22.2644C9.73286 22.5679 8.6707 22.7196 7.9811 22.1215C7.2915 21.5235 7.2915 20.4505 7.2915 18.3046V17.777" stroke="#212121" stroke-width="2"/>
                <path d="M16.6665 12.5L17.4474 11.8753L17.9471 12.5L17.4474 13.1247L16.6665 12.5ZM4.1665 13.5C3.61422 13.5 3.1665 13.0523 3.1665 12.5C3.1665 11.9477 3.61422 11.5 4.1665 11.5V13.5ZM13.2807 6.66699L17.4474 11.8753L15.8856 13.1247L11.719 7.91638L13.2807 6.66699ZM17.4474 13.1247L13.2807 18.333L11.719 17.0837L15.8856 11.8753L17.4474 13.1247ZM16.6665 13.5H4.1665V11.5H16.6665V13.5Z" fill="#212121"/>
              </svg>
              <div class="menu-item__title" id="loginBtnText">Выйти</div>
            </button>

            <AuthModal @authorized="authorized"></AuthModal>
          </div>

          <div class="nav__options">
            <button class="options-item" title='Язык' @click="">
              <svg class="options-lang" width="25" height="25" viewBox="0 0 25 25" fill="none" xmlns="http://www.w3.org/2000/svg">
                <g clip-path="url(#clip0_380_662)">
                  <path d="M12.4609 0.78125C7.38281 0.78125 3.04688 4.0625 1.44531 8.59375H23.5547C21.9141 4.0625 17.5781 0.78125 12.4609 0.78125Z" fill="#F9F9F9"/>
                  <path d="M12.4609 24.2188C17.5781 24.2188 21.9141 20.9375 23.5156 16.4062H1.44531C3.04688 20.9766 7.38281 24.2188 12.4609 24.2188Z" fill="#ED4C5C"/>
                  <path d="M1.44531 8.59375C1.01563 9.80469 0.78125 11.1328 0.78125 12.5C0.78125 13.8672 1.01563 15.1953 1.44531 16.4062H23.5547C23.9844 15.1953 24.2188 13.8672 24.2188 12.5C24.2188 11.1328 23.9844 9.80469 23.5547 8.59375H1.44531Z" fill="#428BC1"/>
                </g>
                <defs>
                  <clipPath id="clip0_380_662">
                    <rect width="25" height="25" fill="white"/>
                  </clipPath>
                </defs>
              </svg>
            </button>
            <button class="options-item" title='Темная тема' @click="">
              <svg class="options-theme" width="25" height="25" viewBox="0 0 25 25" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M21.8748 13.3229C21.7109 15.096 21.0455 16.7858 19.9563 18.1946C18.8671 19.6033 17.3992 20.6727 15.7245 21.2776C14.0497 21.8826 12.2373 21.998 10.4993 21.6105C8.76125 21.223 7.16956 20.3485 5.91043 19.0893C4.65129 17.8302 3.7768 16.2385 3.38926 14.5005C3.00173 12.7625 3.11719 10.9501 3.72213 9.27531C4.32707 7.60053 5.39647 6.13267 6.80521 5.04349C8.21394 3.95431 9.90373 3.28886 11.6769 3.125C10.6387 4.52945 10.1392 6.25984 10.2691 8.00147C10.399 9.7431 11.1496 11.3803 12.3846 12.6152C13.6195 13.8501 15.2567 14.6008 16.9983 14.7307C18.7399 14.8606 20.4703 14.361 21.8748 13.3229Z" stroke="#212121" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </button>
          </div>
        </nav>
      </div>
    </div>
  </header>
</template>
<script>
import AuthModal from "~/components/AuthModal.vue";

export default {
  components: {AuthModal},
  data(){
    return {
      isAuthorized: false
    }
  },
  methods: {
    authorized() {
      this.isAuthorized = true
    },
    unauthorized(){
      let ans = confirm('Вы уверены, что хотите выйти из профиля?')
      if(ans){
        this.isAuthorized = false
        localStorage.setItem('access_token', '')
        localStorage.setItem('refresh_token', '')
      }
    }
  }
}
</script>
<style scoped>
header {
  background: #ff990026;
  box-shadow: 0 4px 5px 0px rgba(0, 0, 0, 0.05);
  font-size: 18px;
}
.header-inner {
  padding: 16px 0;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}
.menu-item {
  height: 25px;
  transition: height .3s ease-in-out;
}
.header__nav, .nav__menu, .nav__options, .menu-item {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.options-item:last-child, .menu-item:nth-child(2) {
  margin-left: 32px;
}
.menu-item__svg {
  margin-right: 10px;
}
.nav__options {
  margin-left: 58px;
}
.main-content__header {
  font-size: 96px;
  font-weight: 500;
}
a.menu-item:hover {
  color: inherit;
}

button:hover > .menu-item__svg, button:hover > .options-theme{
  /*fill: #FF9900CC;*/
  fill: #FF9900;
}



@media screen and (max-width: 680px) {
  .header-inner {
    flex-direction: column;
    padding-bottom: 0;
  }
  nav {
    display: flex;
    justify-content: space-between;
  }
  .header__nav{
    max-width: 100%;
    padding: 10px 15px;
  }
  .options-item:last-child, .menu-item:last-child {
    margin-left: 22px;
  }
}
</style>