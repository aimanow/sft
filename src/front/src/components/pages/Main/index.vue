<template>
  <div class="center center_main-page">
    <section class="section-themes" id="theme-day">
      <div class="h2"><h2>{{$lang.main.dayTheme}}</h2></div>
      <Slick
        ref="slick1"
        class="posts slider-posts"
        :options="postsSlickOptions">
        <PostItem
          :key="item.id"
          v-for="item in discussionsLast"
          :item="item"
          />
      </Slick>
    </section>
    <section class="section-discuss" id="theme-disc-top">
      <div class="h2"><h2>{{$lang.main.discTheme}}</h2></div>
      <Slick
        ref="slick2"
        class="posts posts-sm"
        :options="themesSlickOptions">
        <!-- <v-container grid-list-lg class="pa-0">
          <v-layout row wrap >
            <v-flex xs6 sm3 md4>
            </v-flex>
          </v-layout >
        </v-container> -->
        <ThemeItem
          v-for="item in discussionsTop" :key="item.id"
          :item="item"
          />
      </Slick>
    </section>
    <section class="section-top-discuss m-show">
      <div class="h2"><h2>{{$lang.main.discTopTheme}}</h2></div>
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
        <a href="#" class="cloud_link"  @click.prevent="allDiscusion()"><span class="icon-point"></span>Все</a>
      </div>
    </section>
    <section class="section-top-author" id="top-authors">
      <div class="h2">
        <h2>{{$lang.main.topAuthors}}</h2>
        <div class="sort">
          <span>{{$lang.main.sort}}:</span>
          <a href="#" class="sort_link sort_link1"><span class="icon-like"></span></a>
          <a href="#" class="sort_link sort_link2"><span class="icon-comm"></span></a>
        </div>
      </div>
      <Slick
        ref="slick-3"
        class="authors slider-authors"
        :options="usersSlickOptions">
        <UserItem v-for="author in usersTop" :key="author.id" :author="author" />
      </Slick>
    </section>
    <!-- <section class="section-revs">
      <div class="h2"><h2>{{$lang.main.reviews}}</h2></div>
      <Slick
        ref="slick-4"
        class="slider-revs revs"
        :options="reviewsSlickOption">
        <ReviewItem />
        <ReviewItem />
        <ReviewItem />
        <ReviewItem />
        <ReviewItem />
        <ReviewItem />
        <ReviewItem />
        <ReviewItem />
        <ReviewItem />
        <ReviewItem />
      </Slick>
    </section> -->
    <section class="section-feed" id="feedback">
      <div class="h2"><h2>{{$lang.main.feedTitle}}</h2></div>
      <div class="form_txt">{{$lang.main.feedSubtitle}}</div>
      <div class="form_bg">
        <form>
          <div class="form_cols text-xs-left">
            <div class="form_cols_item">
              <div class="form_row">
                <label><span class="error">*</span> {{$lang.main.feedName}}:</label>
                <div class="form_el"><input type="text" class="t-inp" value="Николай" v-model="feedbackName"></div>
              </div>
              <div class="form_row">
                <label><span class="error">*</span> {{$lang.main.feedEmail}}:</label>
                <div class="form_el"><input type="email" class="t-inp" v-model="feedbackEmail" placeholder="example@gmail.com"></div>
              </div>
            </div>
            <div class="form_cols_item text-xs-left">
              <div class="form_row">
                <label><span class="error">*</span> {{$lang.main.feedTheme}}:</label>
                <div class="form_el">
                  <!-- <div class="jq-selectbox jqselect placeholder">
                    <div class="jq-selectbox__select">
                      <div class="jq-selectbox__select-text">{{$lang.main.feedEmpty}}</div>
                      <div class="jq-selectbox__trigger"><div class="jq-selectbox__trigger-arrow"></div></div>
                    </div>
                    <div class="jq-selectbox__dropdown">
                      <ul>
                        <li class="selected sel placeholder">{{$lang.main.feedEmpty}}</li>
                        <li style="">Предложение о сотрудничестве</li>
                        <li style="">Жалоба</li>
                        <li style="">Пожелания</li>
                      </ul>
                    </div>
                  </div> -->
                  <select class="jq-selectbox jqselect placeholder" v-model="feedbackTopic">
                    <option disabled selected value="">Выберите один из вариантов</option>
                    <option value="claim">claim</option>
                    <option value="offer">offer</option>
                    <option value="wish">wish</option>
                  </select>
                </div>
              </div>
              <div class="form_row">
                <label>{{$lang.main.feedMessage}}:</label>
                <div class="form_el"><textarea v-model="feedbackMessage"></textarea></div>
              </div>
            </div>
          </div>
          <div class="form_cols text-xs-left">
            <div class="form_cols_item">
              <div class="form_row form_capt">
                <div class="form_el">
                  <div class="capt_img"><vue-recaptcha sitekey="6LcG8W4UAAAAAKfUwS1VM07rakvrZT4cgxMGOQXS"/></div>
                </div>
              </div>
              <div class="file_cov">
                <div class="jq-file">
                  <div class="jq-file__name">{{$lang.main.feedAttach}}</div>
                  <div class="jq-file__browse"><span class="icon-link"></span></div>
                  <input type="file" ref="filefeed" @change="processFile">
                </div>
              </div>
            </div>
          </div>
          <div class="form_btn"><input type="submit" :value="$lang.main.feedSend" class="btn" @click.prevent="SubmitFeedback"></div>
        </form>
      </div>
    </section>
    <router-link to="/privacy-policy" class="doc_link">{{$lang.main.terms}}</router-link>
    <router-link to="/terms-of-use" class="doc_link">{{$lang.main.rules}}</router-link>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import Slick from 'vue-slick'
import PostItem from './PostItem'
import ThemeItem from './ThemeItem'
import UserItem from './UserItem'
import ReviewItem from './ReviewItem'
import VueRecaptcha from 'vue-recaptcha'
import slick from '@/components/mixins/slick'
//import checkFavorites from '@/components/mixins/checkFavorites'
let   feedbackFile = null;
export default {
  name: 'Main',

  mixins: [slick],

  data () {
    return {
      feedbackTopic: "",
      feedbackEmail: "",
      feedbackMessage: "",
      feedbackName: "",
      postsSlickOptions: {
        infinity: false,
        dots: true,
        slidesToShow: 2,
        slidesToScroll: 2,
        prevArrow: '<button class="slick-prev slick-arrow"><span class="icon-arrow"></span></button>',
        nextArrow: '<button class="slick-next slick-arrow"><span class="icon-arrow"></span></button>',
        responsive: [
          {
            breakpoint: 1024,
            settings: {
              slidesToShow: 4,
              slidesToScroll: 4
            }
          },
          {
            breakpoint: 724,
            settings: {
              slidesToShow: 3,
              slidesToScroll: 3
            }
          },
          {
            breakpoint: 524,
            settings: {
              slidesToShow: 2,
              slidesToScroll: 2
            }
          },
        ]
      },
      usersSlickOptions: {
        infinity: true,
        dots: true,
        slidesToShow: 3,
        slidesToScroll: 3,
        prevArrow: '<button class="slick-prev slick-arrow"><span class="icon-arrow"></span></button>',
        nextArrow: '<button class="slick-next slick-arrow"><span class="icon-arrow"></span></button>',
        responsive: [
          {
            breakpoint: 1024,
            settings: {
              slidesToShow: 4,
              slidesToScroll: 4
            }
          },
          {
            breakpoint: 724,
            settings: {
              slidesToShow: 3,
              slidesToScroll: 3
            }
          },
          {
            breakpoint: 600,
            settings: {
              slidesToShow: 2,
              slidesToScroll: 2
            }
          },
        ]
      },
      themesSlickOptions: {
        infinity: true,
        dots: true,
        rows: 2,
        slidesToShow: 3,
        slidesToScroll: 3,
        prevArrow: '<button class="slick-prev slick-arrow"><span class="icon-arrow"></span></button>',
        nextArrow: '<button class="slick-next slick-arrow"><span class="icon-arrow"></span></button>',
        responsive: [
          {
            breakpoint: 1024,
            settings: {
              slidesToShow: 4,
              slidesToScroll: 4
            }
          },
          {
            breakpoint: 724,
            settings: {
              slidesToShow: 3,
              slidesToScroll: 3
            }
          },
          {
            breakpoint: 600,
            settings: {
              slidesToShow: 2,
              slidesToScroll: 2
            }
          },
        ]
      },
      reviewsSlickOption: {
        slidesToShow: 3,
        slicesToScroll: 1,
        centerMode: true,
        prevArrow: '<button class="slick-prev slick-arrow"><span class="icon-arrow"></span></button>',
        nextArrow: '<button class="slick-next slick-arrow"><span class="icon-arrow"></span></button>',
        responsive: [
          {
            breakpoint: 1024,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1
            }
          }
        ]
      }
    }
  },

  components: { Slick, PostItem, ThemeItem, UserItem, //ReviewItem,
     VueRecaptcha },

  computed: {
    ...mapState('discussion', ['discussionsTop', 'discussionsLast', 'removedFavDisc', 'removedFavAuthorDisc']),
    ...mapState('profile', ['usersTop'])
  },

  methods: {
    ...mapActions('discussion', ['getDiscussionsTop', 'getDiscussionsLast']),
    ...mapActions('profile', ['getUsersTop']),
    allDiscusion(){
      this.$router.push('/all')
    },
    SubmitFeedback(){
      let data = new FormData();
      data.append("email", this.feedbackEmail)
      data.append("name", this.feedbackName)
      data.append("topic", this.feedbackTopic)
      data.append("message", this.feedbackMessage)
      if( feedbackFile !== null) {data.append("file", feedbackFile)}
      this.$axios.post('/feedback', data,{
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'multipart/form-data',
        }
      }).then(res => {
          this.$store.commit('openDialog', {type: 'success', message: res.data})
      }).catch(err =>{
        if (err.response){
          this.$store.commit('openDialog', err.response.data)
        }else { this.$store.commit('openDialog', err.message)}
      })
    },
    processFile(e) {
      feedbackFile = e.target.files[0]
   }

  },

  mounted () {
    if (this.discussionsLast.length == 0) { this.getDiscussionsLast() }
    if (this.discussionsTop.length == 0) { this.getDiscussionsTop() }
    if (this.usersTop.length == 0) { this.getUsersTop() }

  }

}
</script>

<style>
  .slick-slide {
    margin: 8px 12px 8px;
  }
  .section-discuss .slick-slide{
      margin: 8px 7px 8px
  }
  .posts_item {
    text-align: left;
  }

  .section-discuss .posts_item{
    height: 310px;
  }

   @media screen and (max-width: 1024px){
     .section-discuss .posts_item{
       height: 310px;
     }
   }
</style>

<style scoped>
  .posts_item{
    margin-bottom:15px;

  }
  .section-discuss .posts_item_cont{
    margin-top: -35px;
  }
    section {
      text-align: center;
    }
    .form_capt {
      margin-top: -105px;
    }

    .form_row {
      margin-bottom: 66px;
    }

</style>
