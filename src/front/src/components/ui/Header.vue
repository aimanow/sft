<template>
  <header class="header">
    <a href="#" @click.prevent="openMenu(!menu)" class="mobile-button" :class="{'open': menu}"><span></span></a>
    <div class="header_top">
      <div class="wrapper">
        <div class="header_logo">
          <router-link to="/">
            <img src="@/assets/img/logo.png" alt=""/>
          </router-link>
        </div>
        <div class="header_link header_lang m-hid">
          <a href="#" class="header_lang_selected">{{activeLang}}</a>
          <ul class="header_lang_list">
            <li v-for="lang in langs" v-show="lang.name !== activeLang" :key="lang.name"><a href="#" @click.prevent="changeLang(lang)">{{lang.name}}</a></li>
          </ul>
        </div>
        <div class="header_link header_link_long header_search_opener m-show">
            <router-link to="search">
              <span class="icon-search" @click.prevent="search"></span>
              <div class="header_link_txt">Поиск</div>
            </router-link>
        </div>
        <!--* <div class="header_link header_arch">
          <router-link to="/archive" href="#">
            <span class="icon-arch"></span>
            <div class="header_link_txt">{{$lang.header.archive}}</div>
          </router-link>
        </div> *-->
        <nav class="header_nav">
          <ul>
            <li>
              <router-link to="/aspects">
                <span class="icon-ico8"></span>
                <div class="header_link_txt">{{$lang.header.aspects}}</div>
              </router-link>
            </li>
            <li :class="{'disabled': !auth.id}">
              <router-link to="/profile/favorites">
                <span class="icon-fav"></span>
                <div class="header_link_txt">{{$lang.header.favorites}}</div>
              </router-link>
            </li>
            <li v-if="!auth.id">
              <a href="#" @click.prevent="openLoginModal()">
                <span class="icon-user"></span>
                <div class="header_link_txt">{{$lang.header.login}}</div>
              </a>
            </li>
            <!-- <li v-else>
              <router-link :to="'/profile/' + auth.id" href="#">
                <span class="icon-user"></span>
                <div class="header_link_txt">Профиль</div>
              </router-link>
            </li> -->
          </ul>
          <div class="header_nav_circ" @click="getRendomDisc">
            <span class="circ_grad"><span class="icon-reload"></span></span>
          </div>
        </nav>
        <div class="header_search m-hid">
          <div class="header_search_wr">
            <form @submit.prevent="search">
              <input type="text" :placeholder="$lang.header.searchPlaceHolder" class="t-inp" v-model="searchDiscussion">
              <button class="search-btn"><span class="icon-search"></span></button>
            </form>
          </div>
        </div>
      </div>
    </div>
    <aside class="mob-side" :class="{'open' : menu}">
      <div class="mob-side_top">
        <div class="header_logo">
          <router-link to="/">
            <img src="@/assets/img/logo.png" alt=""/>
            <span>Search For Truth</span>
          </router-link>
        </div>
      </div>
      <div class="mob-side_cont">
        <div class="mob-side_btns" @click.prevent="toggle">
          <div class="mob-side_add"><a href="#" class=""><span class="circ_grad"><span class="icon-plus"></span></span></a></div>
          <a href="#" class="btn btn-bord" @click.prevent="openModal" v-if="auth.id == null">Войти</a>
          <a href="#" class="btn btn-bord" @click.prevent="logout" v-else>Выход</a>
        </div>
        <ul class="mob-side_nav sidebar-themes_list">
          <li><router-link  @click.native="openMenu(false)" v-scroll-to="'#theme-day'" to="/"><span class="icon-arrow_down"></span>Тема дня</router-link></li>
          <li><router-link @click.native="openMenu(false)" v-scroll-to="'#theme-disc-top'" to="/"><span class="icon-arrow_down"></span>Топ тем дискуссий</router-link></li>
          <li><router-link @click.native="openMenu(false)" v-scroll-to="'#top-authors'" to="/"><span class="icon-arrow_down"></span>Топ авторов</router-link></li>
          <li><router-link  @click.native="openMenu(false)" to="/about"><span class="icon-arrow_down"></span>О проекте</router-link></li>
          <!-- <li><router-link to="/"><span class="icon-arrow_down"></span>Архив тем дискуссий</router-link></li> not API-->
          <li><router-link to="/"  @click.native="openMenu(false)"  v-scroll-to="'#feedback'" ><span class="icon-arrow_down"></span>Обратная связь</router-link></li>
          <!-- <li class="li-prof"><a href="#"><span class="icon-user"></span>Мой профиль</a></li> not API-->
        </ul>
        <div class="mob-side_lang">
          <a href="#" class="lang_link">Рус</a> / <a href="#" class="lang_link ative">Eng</a> / <a href="#" class="lang_link">Deu</a>
        </div>
        <div class="soc mob-side_soc">
          <a href="#" class="soc_link"><span class="icon-fb"></span></a>
          <a href="#" class="soc_link"><span class="icon-inst"></span></a>
          <a href="#" class="soc_link"><span class="icon-vk"></span></a>
          <a href="#" class="soc_link"><span class="icon-tw"></span></a>
          <a href="#" class="soc_link"><span class="icon-youtube"></span></a>
        </div>
        <a href="#" class="mob-side_link">Политика конфиденциальности</a>
      </div>
      <div class="mob-side_right">
        <div class="mob-side_bg"><a href="#" @click.prevent="openMenu(false)" class="mob-side_close"><span class="icon-arrow_down"></span></a></div>
      </div>
    </aside>
    <div class="header_overlay" :class="{'openSide': menu}"></div>
  </header>
</template>

<script>
import { mapState, mapActions, mapMutations } from 'vuex'
import {GetFilteredDiscussion} from '@/api'
export default {
  name: 'Header',
  data () {
    return {
      langs: [
        {
          key: 'ru',
          name: 'Рус'
        }, {
          key: 'en',
          name: 'Eng'
        }, {
          key: 'de',
          name: 'Deu'
        }
      ],
      activeLang: 'Рус',
      searchDiscussion: '',
    }
  },

  computed: {
    ...mapState(['menu']),
    ...mapState('auth', ['auth']),
    ...mapState('discussion', ['discussionButton']),
  },

  methods: {
    ...mapActions('modal', ['openLoginModal']),
    ...mapMutations(['openMenu']),
    ...mapActions('auth', ['logout']),
    getRendomDisc(){
      this.$axios.get('/discussions/random').then(res=>{
        this.$router.push('/discussion/' + res.data.id)
      })
    },
    toggle(){
      if(this.discussionButton){
        this.$store.commit('discussion/toggleDiscussionButton', false)
        this.$router.push('/discussion/add')
      } else {
        this.$store.commit('discussion/toggleDiscussionButton', true)
        this.$router.go(-1)
      }
      this.openMenu(false)
    },
    search(){
      GetFilteredDiscussion(this.searchDiscussion).then(res =>{
          this.$store.commit('discussion/setFilteredDiscusion', res.data.items)
          this.$router.push('/search')
        })
    },
    openModal () {
      this.openLoginModal()
    },

    changeLang (lang) {
      this.activeLang = lang.name
      this.$lang.setLang(lang.key)
    }
  }
}
</script>

<style lang="scss">
.header_nav_circ{
  cursor: pointer;
}
</style>
