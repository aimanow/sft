<template>
  <div class="win win-reg" id="win-reg">
    <div class="win_cont">
      <div class="win_title">{{$lang.auth.forgotPassword}}</div>
      <div class="win_form">
        <form @submit.prevent="forgot()">
          <div class="form_row form_shift">
            <div class="form_ico"><span class="icon-mail"></span></div>
            <div class="form_el"><input type="text" class="t-inp" v-model="email" placeholder="Email"/></div>
          </div>
          <div class="form_btn"><input type="submit" class="btn btn-bord" :value="$lang.auth.sendEmail"/></div>
          <div class="win_account">{{$lang.auth.backTo}}<a href="#" @click.prevent="addModal({name: 'Register'})">{{$lang.auth.reg}}</a>
          </div>
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
      email: '',
    }
  },

  methods: {
    ...mapActions('modal', ['addModal', 'closeModal']),
    ...mapMutations('modal', ['closeAllModal']),

    validateEmail(email) {
      const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
      return re.test(email)
    },

    forgot() {
      if (!this.email || !this.validateEmail(this.email)) {
        this.$store.commit('openDialog', this.$lang.main.emailValidationError)
        return
      }
      let form = new FormData()
      form.append('email', this.email)
      this.$axios.post('/access/password/recovery', form, {
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'multipart/form-data',
        }
      }).then(() => {
        this.$store.commit('openDialog', { type: 'success', message: this.$lang.main.forgotPasswordSuccess })
      }).catch(() => {
        this.$store.commit('openDialog', this.$lang.main.forgotPasswordError)
      }).finally(() => {
        this.closeModal(this.modal.name)
      })


    }
  }
}
</script>

<style scoped>

</style>
