<template>
  <div class="win win-reg" id="win-reg">
    <div class="win_cont">
      <div class="win_title">{{$lang.auth.register}}</div>
      <div class="win_form">
        <form @submit.prevent="registerUser()">
          <div class="form_row form_shift">
            <div class="form_ico"><span class="icon-user"></span></div>
            <div class="form_el"><input type="text" v-model="fullname" class="t-inp" :placeholder="$lang.auth.name"/></div>
          </div>
          <div class="form_row form_shift">
            <div class="form_ico"><span class="icon-mail"></span></div>
            <div class="form_el"><input type="text" v-model="email" class="t-inp" placeholder="Email"/></div>
          </div>
          <div class="form_row form_shift">
            <div class="form_ico"><span class="icon-pass"></span></div>
            <div class="form_el"><input type="password" v-model="password" class="t-inp" :placeholder="$lang.auth.password"/></div>
          </div>
          <div class="form_row form_shift">
            <div class="form_ico"><span class="icon-pass2"></span></div>
            <div class="form_el"><input type="password" v-model="re_password" class="t-inp" :placeholder="$lang.auth.rePassword"/></div>
          </div>
          <div class="form_shift">
            <div class="agreement_check">
              <label class="checkbox"><input type="checkbox" v-model="terms" checked=""><div class="checkbox_text">{{$lang.auth.iAccept}} <a href="#">{{$lang.auth.terms}}</a></div></label>
            </div>
          </div>
          <!-- <div class="win_soc">
            <div class="win_soc_title">{{$lang.auth.orSign}}</div>
            <div class="soc">
              <a href="#" class="soc_link"><span class="icon-google"></span></a>
              <a href="#" class="soc_link"><span class="icon-fb"></span></a>
              <a href="#" class="soc_link"><span class="icon-vk"></span></a>
            </div>
          </div> -->
          <div class="form_btn"><input type="submit" class="btn btn-bord" :value="$lang.auth.register" /></div>
          <div class="win_account">{{$lang.auth.haveAcc}} <a href="#" @click.prevent="addModal({name: 'Login'})">{{$lang.auth.signIn}}</a></div>
        </form>
      </div>

    </div>
    <a href="#" @click.prevent="closeAllModal()" class="win_close"><span class="icon-cab7"></span></a>
  </div>
</template>

<script>
import { mapActions, mapMutations } from 'vuex'
export default {
  name: "Login",

  props: ['modal'],

  data () {
    return {
      email: '',
      fullname: '',
      password: '',
      re_password: '',
      terms: false
    }
  },

  methods: {
    ...mapActions('modal', ['addModal', 'closeModal']),
    ...mapMutations('modal', ['closeAllModal']),
    ...mapMutations('profile', ['setUserData']),
    ...mapActions('auth', ['register','login']),

    registerUser () {
      if (!this.terms) return false;
      if (this.password !== this.re_password) return false
      this.register({
        email: this.email,
        fullname: this.fullname,
        password: this.password
      })
        .then(() => {
          this.login({
            email: this.email,
            password: this.password
          }).then(()=>{
            this.closeAllModal()
            this.$router.push('/')
          })
        })
    }
  }
}
</script>


<style>
.win_account{
	cursor: pointer;
}
</style>
