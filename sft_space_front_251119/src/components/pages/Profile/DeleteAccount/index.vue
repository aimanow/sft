<template>
  <div class="center">
    <section class="section-form">
      <div class="h2 m-hid"><h1>{{$lang.profile.delTitle}}</h1></div>
      <div class="form_block">
        <div class="form_block_title block_title"><span class="icon-cab7"></span>{{$lang.profile.delTitle}}</div>
        <div class="form_block_txt">{{$lang.profile.delDesc}}</div>
        <div class="form_btn">
          <a href="#" class="btn" @click.prevent="userDelete">{{$lang.profile.accept}}</a>
          <a href="#" @click.prevent="$router.go(-1)" class="btn btn-gray" >{{$lang.profile.cancel}}</a>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
  name: 'DeleteAccount',
  computed: {
    ...mapState('auth', ['auth'])
  },
  methods: {
    ...mapActions('profile', ['deleteUser']),
    ...mapActions('auth', ['logout']),
    userDelete () {
      this.deleteUser(this.auth.id)
        .then(() => this.logout())
    }
  }
}
</script>

<style scoped>

</style>
