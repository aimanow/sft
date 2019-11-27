<template>
  <div class="win win-reg" id="win-reg">
    <div class="win_cont">
      <div class="win_title">{{$lang.header.login}}</div>
      <div class="win_form">
        <form>
          <div class="form_row form_shift">
            <div class="form_ico"><span class="icon-mail"></span></div>
            <div class="form_el"><input type="text" class="t-inp" placeholder="Email" v-model="email"/></div>
          </div>
          <div class="form_row form_shift">
            <div class="form_ico"><span class="icon-pass"></span></div>
            <div class="form_el"><input type="password" class="t-inp" :placeholder="$lang.auth.password" v-model="password"/></div>
          </div>
         <div class="win_soc">
            <div class="win_soc_title">{{$lang.auth.orSign}}</div>
            <div class="soc">
              <a href="#" class="soc_link" @click="addModal({ name: 'OAuthGoogle' })"><span class="icon-google"></span></a>
              <a href="#" class="soc_link" @click="addModal({ name: 'OAuthFacebook' })"><span class="icon-fb"></span></a>
              <a href="#" class="soc_link" @click="addModal({ name: 'OAuthVK' })"><span class="icon-vk"></span></a>
            </div>
          </div>
          <div class="form_btn"><input type="submit" class="btn btn-bord" :value="$lang.auth.signIn" @click.prevent="loginUser()"/></div>
          <div class="forgot_link"><a href="#" @click.prevent="addModal({name : 'ForgotPassword'})">{{$lang.auth.forgotPassword}}</a></div>
          <div class="win_account">{{$lang.auth.noAcc}} <a @click.prevent="addModal({name: 'Register'})">{{$lang.auth.register}}</a></div>
        </form>
      </div>

    </div>
    <a @click.prevent="closeAllModal()" class="win_close"><span class="icon-cab7"></span></a>
  </div>
</template>

<script>
import { mapActions, mapMutations } from 'vuex'

export default {
  name: 'Login',

  props: ['modal'],

  data() {
    return {
      email: '',
      password: ''
    }
  },

  methods: {
    ...mapActions('modal', ['addModal', 'closeModal', 'openForgotPassword']),
    ...mapMutations('modal', ['closeAllModal']),
    ...mapMutations('profile', ['setUserData']),
    ...mapActions('auth', ['login']),
    ...mapMutations(['openDialog']),

    loginUser() {
      this.login({
        email: this.email,
        password: this.password
      })
        .then(success => {
          if (success) {
            this.closeAllModal()
          }
        }).catch((err) => {
          if (err.message === 'Request failed with status code 403') {
            this.openDialog(this.$lang.error.authEmailError)
          } else
            this.openDialog(this.$lang.error.authPlainError)
        })

    }
  }
}
</script>

<style scoped>

</style>
