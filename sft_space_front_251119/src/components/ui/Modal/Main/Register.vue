<template>
  <div class="win win-reg" id="win-reg">
    <div class="win_cont">
      <div class="win_title">{{$lang.auth.register}}</div>
      <div class="win_form">
        <form @submit.prevent="registerUser()">
          <div class="form_row form_shift">
            <div class="form_ico"><span class="icon-user"></span></div>
            <div class="form_el">
              <input type="text" v-model="form.fullname" class="t-inp" :placeholder="$lang.auth.name"/>
              <transition name="fade">
                <div v-if="validation.fullname" style="color: #FF7052">{{$lang.error.registerValidName}}</div>
              </transition>
            </div>
          </div>
          <div class="form_row form_shift">
            <div class="form_ico"><span class="icon-mail"></span></div>
            <div class="form_el">
              <input type="text" v-model="form.email" class="t-inp" placeholder="Email"/>
              <transition name="fade">
                <div v-if="validation.email" style="color: #FF7052">{{$lang.error.registerValidEmail}}</div>
              </transition>
            </div>

          </div>
          <div class="form_row form_shift">
            <div class="form_ico"><span class="icon-pass"></span></div>
            <div class="form_el">
              <input type="password" v-model="form.password" class="t-inp" :placeholder="$lang.auth.password"/>
              <transition name="fade">
                <div v-if="validation.password" style="color: #FF7052">{{$lang.error.registerValidPassword}}</div>
              </transition>
            </div>
          </div>
          <div class="form_row form_shift">
            <div class="form_ico"><span class="icon-pass2"></span></div>
            <div class="form_el">
              <input type="password" v-model="form.re_password" class="t-inp" :placeholder="$lang.auth.rePassword"/>
              <transition name="fade">
                <div v-if="validation.re_password" style="color: #FF7052">{{$lang.error.registerValidPasswordDouble}}</div>
              </transition>
            </div>
          </div>
          <div class="form_shift">
            <div class="agreement_check">
              <label class="checkbox"><input type="checkbox" v-model="form.terms" checked="">
                <div class="checkbox_text" style="">{{$lang.auth.iAccept}} <a href="#">{{$lang.auth.terms}}</a></div>
              </label>
            </div>
          </div>
          <div class="win_soc">
            <div class="win_soc_title">{{$lang.auth.orSign}}</div>
            <div class="soc">
              <a href="#" class="soc_link" @click="addModal({ name: 'OAuthGoogle' })"><span class="icon-google"></span></a>
              <a href="#" class="soc_link" @click="addModal({ name: 'OAuthFacebook' })"><span class="icon-fb"></span></a>
              <a href="#" class="soc_link" @click="addModal({ name: 'OAuthVK' })"><span class="icon-vk"></span></a>
            </div>
          </div>
          <div class="form_btn"><input :disabled="formBusy" type="submit" class="btn btn-bord" :value="$lang.auth.register"/></div>
          <div class="win_account">{{$lang.auth.haveAcc}} <a href="#" @click.prevent="addModal({name: 'Login'})">{{$lang.auth.signIn}}</a>
          </div>
        </form>
      </div>

    </div>
    <a href="#" @click.prevent="closeAllModal()" class="win_close"><span class="icon-cab7"></span></a>
  </div>
</template>

<script>
import { mapActions, mapMutations } from 'vuex'

export default {
  name: 'Login',

  props: ['modal'],

  data() {
    return {
      form: {
        email: '',
        fullname: '',
        password: '',
        re_password: '',
        terms: true,
      },

      formBusy: false,

      validation: {
        fullname: false,
        email: false,
        password: false,
        re_password: false
      }
    }
  },

  methods: {
    ...mapActions('modal', ['addModal', 'closeModal']),
    ...mapMutations('modal', ['closeAllModal', 'add']),
    ...mapMutations('profile', ['setUserData']),
    ...mapMutations(['openDialog']),
    ...mapActions('auth', ['register', 'login']),

    validateEmail(email) {
      const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
      return re.test(email)
    },

    checkValidation() {
      let result = false

      if (!this.form.fullname || this.form.fullname.length < 2) {
        this.validation.fullname = true
        return result
      } else
        this.validation.fullname = false

      if (!this.form.email || !this.validateEmail(this.form.email)) {
        this.validation.email = true
        return result
      } else
        this.validation.email = false

      if (!this.form.password || this.form.password.length < 6) {
        this.validation.password = true
        return result
      } else
        this.validation.password = false

      if (this.form.password !== this.form.re_password) {
        this.validation.re_password = true
        return result
      } else
        this.validation.re_password = false

      if (!this.form.terms) {
        this.openDialog(this.$lang.error.registerTermsError)
        return result
      }

      result = true

      return result
    },

    registerUser() {
      if (!this.checkValidation())
        return false

      this.formBusy = true
      this.register({
        email: this.form.email,
        fullname: this.form.fullname,
        password: this.form.password
      }).then(() => {
        this.login({
          email: this.form.email,
          password: this.form.password
        }).then(() => {
          this.closeAllModal()
        }).catch(() => {
        }).finally(() => {
          this.formBusy = false
        })
      }).catch((err) => {
        if (err.message === 'Request failed with status code 409') {
          this.openDialog(this.$lang.error.registerEmailError)
        } else
          this.openDialog(this.$lang.error.registerPlainError)
        this.formBusy = false
      })
    }
  }
}
</script>


<style>
  .win_account {
    cursor: pointer;
  }

  .fade-enter-active, .fade-leave-active {
    transition: opacity .3s;
  }

  .fade-enter, .fade-leave-to {
    opacity: 0;
  }
</style>
