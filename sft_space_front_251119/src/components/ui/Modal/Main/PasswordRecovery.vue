<template>
  <div class="win win-reg" id="win-reg">
    <div class="win_cont">
      <div class="win_title">{{$lang.auth.recoveryPassword}}</div>
      <div class="win_form">
        <form @submit.prevent="recovery()">
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
          <div class="form_btn"><input type="submit" class="btn btn-bord" :value="$lang.auth.recoveryPass"/></div>
        </form>
      </div>

    </div>
    <a href="#" class="win_close" @click.prevent="closeAllModal"><span class="icon-cab7"></span></a>
  </div>
</template>

<script>
import { mapActions, mapMutations } from 'vuex'

export default {
  name: 'ForgotPassword',

  props: ['modal'],

  data() {
    return {
      form: {
        password: '',
        re_password: '',
        token: null,
      },

      formBusy: false,

      validation: {
        token: false,
        password: false,
        re_password: false
      }
    }
  },

  mounted() {
    let token = null
    try {
      token = window.location.search
        .trim()
        .split('?')[1]
        .split('=')[1]
    } catch (e) {
      token = null
    }

    this.form.token = token
  },

  methods: {
    ...mapActions('modal', ['addModal', 'closeModal']),
    ...mapMutations('modal', ['closeAllModal']),
    ...mapMutations('auth', ['login']),

    checkValidation() {
      let result = false

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

      result = true

      return result
    },

    recovery() {
      if (!this.checkValidation())
        return false

      this.formBusy = true

      let form = new FormData()
      form.append('password', this.form.password)
      form.append('token', this.form.token)

      this.$axios.post('/access/password/reset', form, {
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'multipart/form-data',
        }
      }).then((result) => {
        this.login(result.data)
        this.$store.commit('openDialog', { type: 'success', message: this.$lang.auth.recoveryPasswordSuccess })
        this.$router.push('/')
      }).catch((e) => {
        console.log(e)
        this.$store.commit('openDialog', this.$lang.auth.recoveryPasswordError)
      }).finally(() => {
        this.formBusy = false
        this.closeModal(this.modal.name)
      })
    }
  }
}
</script>

<style scoped>

</style>
