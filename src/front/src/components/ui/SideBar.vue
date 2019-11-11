<template>
  <aside class="sidebar">
    <div class="cab">

      <div @click="openLoginModal" v-if="!auth.id" class="cab_top">
        <a href="#" class="cab_top_create">
          <div class="cab_top_icon"><span class="icon-user"></span></div>
          <div class="cab_top_txt">Создать личный кабинет</div>
        </a>
      </div>

      <div v-else class="cab_top">
        <router-link to="/profile/settings" class="cab_top_sett">
          <span class="icon-settings"></span>
        </router-link>

        <router-link :to="'/profile/' + auth.id" class="cab_top_prof">
          <div class="cab_top_icon">
            <img v-if="auth.avatar_url" :src="$baseUrl+auth.avatar_url" :key="renderKeyAvatar" :alt="auth.fullname" style="border-radius: 50%;">
            <span v-else class="icon-user"></span>
          </div>
          <div class="cab_top_txt">
            <div class="cab_top_name">{{auth.fullname}}</div>
            <div class="cab_top_mail">{{auth.email}}</div>
          </div>
        </router-link>
        <a href="#" class="cab_top_opener" @click.prevent="openUserMenu()"></a>
      </div>
      <div class="cab_drop" v-show="userMenuOpened">
        <ul class="cab_list">
          <li :class="{ 'active': activePage === 'MainEducation' }">
            <router-link to="/profile/education"><span class="icon-cab1"></span><span class="cab_list_txt">{{$lang.main.edu}}</span></router-link>
          </li>
          <li :class="{ 'active': activePage === 'Favorites' }">
            <router-link to="/profile/favorites"><span class="icon-fav2"></span><span class="cab_list_txt">{{$lang.main.fav}}</span></router-link>
          </li>
          <!-- <li :class="{ 'active': activePage === 'History' }">
            <router-link to="/profile/history"><span class="icon-cab3"></span><span class="cab_list_txt">{{$lang.main.visited}}</span></router-link>
          </li> -->
          <li :class="{ 'active': activePage === 'Rewards' }">
            <router-link to="/profile/rewards"><span class="icon-cab4"></span><span class="cab_list_txt">{{$lang.main.achiv}}</span></router-link>
          </li>
          <li :class="{ 'active': activePage === 'MainAreasOfKnowledge' }">
            <router-link to="/profile/areas-of-knowledge"><span class="icon-cab5"></span><span class="cab_list_txt">{{$lang.main.obl}}</span></router-link>
          </li>
          <li :class="{ 'active': activePage === 'Delete' }">
            <router-link to="/profile/delete"><span class="icon-cab7"></span><span class="cab_list_txt">{{$lang.main.del}}</span></router-link>
          </li>
          <li :class="{ 'active': activePage === 'Logout' }">
            <router-link to="/profile/logout"><span class="icon-cab8"></span><span class="cab_list_txt">{{$lang.main.signOut}}</span></router-link>
          </li>
        </ul>
      </div>
    </div>
    <div class="sidebar-themes m-hid">
      <div class="add_link"  @click.prevent="toggle">
        <div class="circ_grad"><span class="icon-plus" ></span></div>
        <span v-if="discussionButton" >{{$lang.main.add}}</span>
        <span v-else>cancel</span>
      </div>
      <ul class="sidebar-themes_list">
        <li>
          <router-link to="/" v-scroll-to="'#theme-day'"><span class="icon-arrow_down"></span>{{$lang.main.dayTheme}}</router-link>
        </li>
        <li>
          <router-link to="/" v-scroll-to="'#theme-disc-top'"><span class="icon-arrow_down"></span>{{$lang.main.discTopTheme}}</router-link>
        </li>
        <li>
          <router-link to="/" v-scroll-to="'#top-authors'"><span class="icon-arrow_down"></span>{{$lang.main.topAuthors}}</router-link>
        </li>
        <li>
          <router-link to="/about"><span class="icon-arrow_down"></span>{{$lang.main.about}}</router-link>
        </li>
        <!-- <li>
          <router-link to="/archive"><span class="icon-arrow_down"></span>{{$lang.main.archiveDisc}}</router-link>
        </li> -->
        <li>
          <router-link to="/" v-scroll-to="'#feedback'"><span class="icon-arrow_down"></span>{{$lang.main.feedback}}</router-link>
        </li>
      </ul>
    </div>
    <section class="sidebar-top-discuss m-hid">
      <h3>{{$lang.main.discTopTheme}}</h3>
      <div class="cloud">
        <!-- <a href="#" class="cloud_link"><span class="icon-point"></span>Планета Земля</a>
        <a href="#" class="cloud_link"><span class="icon-point"></span>Космос</a>
        <a href="#" class="cloud_link"><span class="icon-point"></span>Психология</a>

        <a href="#" class="cloud_link"><span class="icon-point"></span>Кулинария</a>
        <a href="#" class="cloud_link"><span class="icon-point"></span>Животные</a>
        <a href="#" class="cloud_link"><span class="icon-point"></span>Кант</a>
        <a href="#" class="cloud_link"><span class="icon-point"></span>Конфеты</a>

        <a href="#" class="cloud_link"><span class="icon-point"></span>Планета Земля</a>
        <a href="#" class="cloud_link"><span class="icon-point"></span>Космос</a>
        <a href="#" class="cloud_link"><span class="icon-point"></span>Психология</a>

        <a href="#" class="cloud_link"><span class="icon-point"></span>Кулинария</a>
        <a href="#" class="cloud_link"><span class="icon-point"></span>Животные</a>
        <a href="#" class="cloud_link"><span class="icon-point"></span>Кант</a> -->
        <a href="#" class="cloud_link" @click.prevent="allDiscusion()" ><span class="icon-point"></span>Все</a>
      </div>
    </section>
  </aside>
</template>

<script>

import { mapState, mapActions } from 'vuex'
export default {
  name: 'SideBar',

  data () {
    return {

    }
  },

  methods: {
    ...mapActions('modal', ['openLoginModal']),
    ...mapActions('modal', ['openLoginModal']),
    openUserMenu () {
      this.$store.commit('auth/toggleUserMenuOpened', null, { root: true })
    },
    toggle(){
      if(this.discussionButton){
        this.$store.commit('discussion/toggleDiscussionButton', false)
        this.$router.push('/discussion/add')
      } else {
        this.$store.commit('discussion/toggleDiscussionButton', true)
        this.$router.go(-1)
      }
    },
    allDiscusion(){
      this.$router.push('/all')
    }
  },

  computed: {
    ...mapState('auth', ['auth','userMenuOpened', 'renderKeyAvatar','permission']),
    ...mapState('discussion', ['discussionButton']),
    activePage () {
      return this.$route.name
    }
  },

}
</script>

<style scoped>
.cab_drop {
  display: block;
}
</style>
