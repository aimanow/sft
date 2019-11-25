<template>
  <div class="center">
    <section class="section-form">
      <div class="h2 m-hid"><h1>{{$lang.profile.logoutTitle}}</h1></div>
      <div class="form_block">
        <div class="form_block_title block_title"><span class="icon-cab8"></span>{{$lang.profile.logoutDesc}}</div>
        <div class="form_btn">
          <a href="#" class="btn" @click.prevent="Logout">{{$lang.profile.accept}}</a>
          <a href="#" class="btn btn-gray" @click.prevent="$router.go(-1)">{{$lang.profile.cancel}}</a>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import {mapActions} from 'vuex'
export default {
  name: 'Logout',

  methods: {
    ...mapActions('auth', ['logout']),
    Logout(){
      this.logout()
    }
  }
}
</script>

<style scoped>

</style>
