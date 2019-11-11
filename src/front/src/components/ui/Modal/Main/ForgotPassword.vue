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
          <div class="win_account">{{$lang.auth.backTo}}<a href="#" @click.prevent="addModal({name: 'Register'})">{{$lang.auth.reg}}</a></div>
        </form>
      </div>

    </div>
    <a href="#" class="win_close" @click.prevent="closeAllModal"><span class="icon-cab7"></span></a>
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
    }
  },

  methods: {
    ...mapActions('modal', ['addModal', 'closeModal']),
    ...mapMutations('modal', ['closeAllModal']),

    forgot () {
      alert('check console')
      console.log({email: this.email})
      this.closeModal(this.modal.name)
    }
  }
}
</script>

<style scoped>

</style>
