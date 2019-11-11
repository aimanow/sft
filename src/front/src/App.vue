<template>
<v-app>
  <div class="main-wrapper">
    <div v-if="showPreloader" class="preloader">
      <div class="preloader_lays">
        <div class="preloader_para">
          <img src="@/assets/img/par.png" alt="" />
        </div>
      </div>
      <div class="preloader_cntr">
        <div class="logo_img"><img src="@/assets/svg/logo.svg" alt="" /></div>
        <div class="logo_txt">Search For Truth</div>
      </div>
      <div class="preloader_mouse">
        <img src="@/assets/img/mouse.png" alt="" />
      </div>
    </div>
    <!-- BEGIN CONTENT -->
    <main class="content">
      <div class="content_cols">
        <div class="wrapper">
          <SideBar />
          <router-view :key="$route.path"/>

        </div>
      </div>
    </main>
    <!-- CONTENT EOF  -->
    <!-- BEGIN HEADER -->
    <Header />
    <!-- HEADER EOF   -->
    <!-- BEGIN footer -->
    <Footer />
    <!-- footer EOF   -->
    <Modal />
    <!-- <div class="donate-btn">
      <a href="#">Donate</a>
    </div> -->
  </div>
</v-app>
</template>

<script>
import Header from '@/components/ui/Header'
import Footer from '@/components/ui/Footer'
import SideBar from '@/components/ui/SideBar'
import Modal from '@/components/ui/Modal'

import { mapMutations } from 'vuex'

export default {
  name: 'App',

  data () {
    return {
      showPreloader: false,
    }
  },
  methods: {
    ...mapMutations('auth', ['login', 'setPermission'])
  },

  mounted() {
    let auth;
      this.$axios.get('/profiles/current')
        .then(res => {
            if(res.status == 200){
              auth = res.data;
              this.login(auth)
              return auth.id
            }
        })
        .then(id =>{
            return this.$axios.get(`/profiles/${id}/permissions`)
        })
        .then((res) => {
          console.log(res.data)
          this.setPermission(res.data);

        })
        .catch(err => console.log(err.message))


    if(this.$route.path == "/discussion/add"){
      this.$store.commit('discussion/toggleDiscussionButton', false)
    }else{this.$store.commit('discussion/toggleDiscussionButton', true)}

  //   this.$nextTick(function() {
  //     let self = this;
  //     setTimeout(() => {
  //       self.showPreloader = false
	// }, 1000)
  },

  components: { Header, Footer, SideBar, Modal }
}
</script>

<style lang="scss">
.donate-btn {
  position: fixed;
  bottom: 30px;
  right: 20px;
  z-index: 9999;
  a {
    border-radius: 20px;
    padding: 10px;
    background: linear-gradient(64.85deg, #284dc0 32.48%, #ff441d 84.02%);
    color: #fff;
    font-size: 15px;
    box-shadow: 0px 8px 12px rgba(0, 0, 0, 0.22);
    text-align: center;
    transition: all 0.2s ease;
  }
}
</style>
