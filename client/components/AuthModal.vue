<script setup >
// defineProps({
//   isAuthorized: {
//     type: Boolean,
//   }
// });
//
// defineEmits(['changeAuth:isAuthorized']);
</script>

<template>
  <!-- Modal -->
  <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-body">
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          <div class="auth-header">Авторизация</div>

          <ul class="nav mb-3" id="pills-tab" role="tablist">
            <li class="nav-item" role="presentation">
              <a class="nav-link" id="pills-sign-up-tab" data-bs-toggle="pill" href="#pills-sign-up" role="tab" aria-controls="pills-sign-up" aria-selected="false">Регистрация</a>
            </li>
            <li class="nav-item" role="presentation">
              <a class="nav-link active" id="pills-sign-in-tab" data-bs-toggle="pill" href="#pills-sign-in" role="tab" aria-controls="pills-sign-in" aria-selected="true">Вход</a>
            </li>
          </ul>
          <div class="tab-content" id="pills-tabContent">
            <div class="tab-pane fade" id="pills-sign-up" role="tabpanel" aria-labelledby="pills-sign-up-tab">
              <div class="tab__inner">
                <div class="tab-form">
                  <input class="form-input" type="text" id="sign-up-name" placeholder="Иванов Иван" v-model="formSignUp.fio">
                  <input class="form-input" type="text" id="sign-up-login" placeholder="Email" v-model="formSignUp.email">
                  <input class="form-input" type="password" id="sign-up-password" placeholder="Пароль" v-model="formSignUp.password">
                </div>
                <button class="tab-btn sign-up" @click="signUp">Зарегистрироваться</button>
              </div>
            </div>

            <div class="tab-pane fade show active" id="pills-sign-in" role="tabpanel" aria-labelledby="pills-sign-in-tab">
              <div class="tab__inner">
                <div class="tab-form">
                  <input class="form-input" type="text" id="sign-in-login" placeholder="Email" v-model="formSignIn.email">
                  <input class="form-input" type="password" id="sign-in-password" placeholder="Пароль" v-model="formSignIn.password">
                </div>
                <button class="tab-btn sign-in" @click="signIn">Войти</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {useFetch, useRuntimeConfig} from "nuxt/app";

export default {
  name: "AuthModal",
  data(){
    return {
      formSignUp: {
        fio: '',
        email: '',
        password: ''
      },
      formSignIn: {
        email: '',
        password: ''
      }
    }
  },
  methods: {
    async signUp(){
      let data = {email: this.formSignUp.email, login: this.formSignUp.fio, password: this.formSignUp.password }
      console.log('dataSignUp: ', data)

      const config = useRuntimeConfig();
      let url = config.public.baseURL + '/api/auth/register'
      //let url = "https://run.mocky.io/v3/ffb1d08c-9ffc-455e-966d-9255f5d6f19c" // статус 200
      //let url = "https://run.mocky.io/v3/0b05314b-5dbd-4e32-be63-9469a6ebcfbf" // статус 401
      try{
        const res = await $fetch(url, {
          method: 'POST',
          body: data,
          headers: {
            'Content-Type': 'application/json'
          }
        })
        this.cleanFormSignIn()
        console.log('Регистрация пользователя прошла успешно.')
        alert('Регистрация пользователя прошла успешно.')
        this.closeAuthModal()

      } catch(error){
          alert('При регистрации что-то пошло не так... \nStatus-code: ' + error.status)
          console.log(error.message)
      }
    },

    async signIn(){
      let data = {email: this.formSignIn.email, password: this.formSignIn.password }
      console.log('dataSignIn: ', data)

      const config = useRuntimeConfig();
      let url = config.public.baseURL + '/api/auth/login'
      //let url = "https://run.mocky.io/v3/9ab21fd6-c962-487b-8dd0-28d0aef8ee93"
      try{
        const res = await $fetch(url, {
          method: 'POST',
          body: data,
          headers: {
            'Content-Type': 'application/json'
          }
        })
        // res = {access_token: "", refresh_token: ""}
        if(res){
          this.cleanFormSignIn()
          localStorage.setItem('access_token', `Bearer ${res['access_token']}`)
          localStorage.setItem('refresh_token', res['refresh_token'])
          console.log('Авторизация пользователя прошла успешно.')
          alert('Авторизация пользователя прошла успешно.')
          this.$emit('authorized')
          this.closeAuthModal()
        } else {
          console.log('Пустой список токенов.')
        }
      } catch(error){
        if(error.status === 401){
          alert('Неверный логин или пароль')
        } else {
          alert('При авторизации что-то пошло не так... \nStatus-code: ' + error.status)
          console.log(error.message)
        }
      }
    },
    cleanFormSignIn(){
      this.formSignIn.email = ''
      this.formSignIn.password = ''
    },
    closeAuthModal(){
      let myModalEl = document.getElementById('exampleModal')
      let myModal = bootstrap.Modal.getInstance(myModalEl)
      myModal.hide();
    }
  }
}
</script>

<style scoped>
  .modal-dialog{width:700px;}
  .modal-content {
    border-radius: 10px;
    border: none;
  }
  .modal-body{
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 28px 40px 40px 40px;
    width: 100%;
  }
  .auth-header{font-size: 20px;}
  .btn-close {
    align-self: flex-end;
  }
  .btn-close:active{border: none;}
  /* ---------- */
  /* switch для выбора режима формы авторизации Регистрация / Вход ----- */
  .nav {
    margin-top: 10px;
    display: flex;
    justify-content: center;
    background-color: #10101010;
    width: 100%;
    border-radius: 30px;
    transition: background-color .3s ease;
  }
  .nav-item{
    width: 50%;
    text-align: center;
    border-radius: 30px;
  }
  .nav-link {
    /*color: #00003030;*/
    color: #FF990080;
    border-radius: 30px;
  }

  .nav-link.active{
    border-radius: 30px;
    background-color: #FF9900;
    color: #FFFFFF;
    transition: background-color .4s ease;
  }
  .tab-pane, .tab-content, .tab-form{width: 100%;}
  .tab-content{
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 40px;
    font-size: 20px;
    line-height: 100%;
  }

  .form-input{
    width: 100%;
    border: 1px solid rgba(255, 153, 0, 0.5);
    border-radius: 5px;
    font-size: 20px;
    line-height: 100%;
    padding: 15px 25px;
    margin-bottom: 20px;
  }
  .form-input::placeholder{color:#21212160}

  .form-input:focus{
    border: 2px solid rgba(255, 153, 0, 0.5);
    outline: none;
  }

  .tab__inner{
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .tab-btn{
    background: #FF9900;
    border-radius: 6px;
    padding: 10px;
    width: max-content;
    color: #FFFFFF;
  }
  .tab-btn.sign-in{
    padding: 10px 60px;
  }
  .tab-btn.sign-up{
    padding: 10px 30px;
  }

</style>