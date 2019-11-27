<template>
  <div class="center">
    <div class="center_search m-show">
      <form @submit.prevent="search">
        <input type="text" placeholder="Что вы ищете?" class="t-inp" v-model="searchDiscussion">
        <button class="search-btn" type="submit"><span class="icon-search"></span></button>
      </form>
    </div>
    <section class="section-discuss">
      <div class="h2"><h1>{{$lang.filter.searchResults}}</h1></div>

      <a href="#" @click.prevent="showFilter = !showFilter" class="filter_link btn btn-bo rd-blue"><span class="icon-filter"></span>{{$lang.filter.filter}}</a>
      <div class="filter_block" :class="{'show' : showFilter}">
        <div class="filter_block_top">
          <div class="filter_block_res_title">{{$lang.filter.points}}:</div>
          <div class="filter_block_rads rads">
            <div class="rads_item">
              <label class="radio"><input type="checkbox" checked="" placeholder="">
                <span class="radio_text">{{$lang.filter.byDate}} <img src="@/assets/svg/arrs.svg" alt=""></span>
              </label>
            </div>
            <div class="rads_item">
              <label class="radio"><input type="checkbox" checked=""><span class="radio_text">Рус</span></label>
            </div>
            <div class="rads_item">
              <label class="radio"><input type="checkbox" placeholder=""><span class="radio_text">Eng</span></label>
            </div>
            <div class="rads_item">
              <label class="radio"><input type="checkbox" placeholder=""><span class="radio_text">Deu</span></label>
            </div>
            <div class="rads_item">
              <label class="radio"><input type="checkbox" placeholder=""><span class="radio_text">{{$lang.filter.byPop}}</span></label>
            </div>
          </div>
        </div>
        <div class="filter_block_res">
          <div class="filter_block_res_title">{{$lang.filter.byAspects}}:</div>
          <div class="aspect aspect-check aspect-gr">
            <div class="aspect_item">
              <a href="#" class="aspect_item_img">
                <div class="aspect_item_bg js-bg" style="background-image: url('@/assets/img/ar1.png');"><img src="img/img3.jpg" alt=""
                                                                                                              style="display: none;"></div>
                <div class="aspect_item_text"><span class="icon-check"></span>
                  <p>{{$lang.filter.karma}}</p></div>
              </a>
            </div>
            <div class="aspect_item active">
              <a href="#" class="aspect_item_img">
                <div class="aspect_item_bg js-bg" style="background-image: url('@/assets/img/ar1.png');"><img src="img/img3.jpg" alt=""
                                                                                                              style="display: none;"></div>
                <div class="aspect_item_text"><span class="icon-check"></span>
                  <p>{{$lang.filter.earth}}</p></div>
              </a>
            </div>
            <div class="aspect_item ">
              <a href="#" class="aspect_item_img">
                <div class="aspect_item_bg js-bg" style="background-image: url('@/assets/img/ar1.png');"><img src="img/img3.jpg" alt=""
                                                                                                              style="display: none;"></div>
                <div class="aspect_item_text"><span class="icon-check"></span>
                  <p>{{$lang.filter.physics}}</p></div>
              </a>
            </div>
            <div class="aspect_item active">
              <a href="#" class="aspect_item_img">
                <div class="aspect_item_bg js-bg" style="background-image: url('@/assets/img/ar1.png');"><img src="img/img3.jpg" alt=""
                                                                                                              style="display: none;"></div>
                <div class="aspect_item_text"><span class="icon-check"></span>
                  <p>{{$lang.filter.quantum}}</p></div>
              </a>
            </div>
            <div class="aspect_item ">
              <a href="#" class="aspect_item_img">
                <div class="aspect_item_bg js-bg" style="background-image: url('@/assets/img/ar1.png');"><img src="img/img3.jpg" alt=""
                                                                                                              style="display: none;"></div>
                <div class="aspect_item_text"><span class="icon-check"></span>
                  <p>{{$lang.filter.space}}</p></div>
              </a>
            </div>
            <div class="aspect_item active">
              <a href="#" class="aspect_item_img">
                <div class="aspect_item_bg js-bg" style="background-image: url('@/assets/img/ar1.png');"><img src="img/img3.jpg" alt=""
                                                                                                              style="display: none;"></div>
                <div class="aspect_item_text"><span class="icon-check"></span>
                  <p>{{$lang.filter.football}}</p></div>
              </a>
            </div>
          </div>
        </div>
      </div>
      <div v-if="result" class="empty-res">
        <img src="@/assets/img/search.png" alt="foto"/>
        <p>{{$lang.filter.notFoundOne}}<br/>{{$lang.filter.notFoundTwo}}</p>
      </div>
      <component
        :is="slickComp"
        ref="slick2"
        class="posts posts-sm"
        :options="SlickOptions">
        <ThemeItem
          v-for="item in searchedDiscusion" :key="item.id"
          :item="item"
        />
      </component>
    </section>
    <section class="section-discuss">
      <div class="h2"><h2>{{$lang.filter.sameThemes}}</h2></div>
      <component
        :is="slickComp"
        ref="slick3"
        class="posts posts-sm"
        :options="SlickOptions1">
        <ThemeItem
          v-for="item in searchedDiscusion" :key="item.id"
          :item="item"
        />
      </component>
    </section>
    <section class="section-themes">
      <div class="h2"><h2>{{$lang.main.dayTheme}}</h2></div>
      <component
        :is="slickComp"
        ref="slick1"
        class="posts slider-posts"
        :options="SlickOptions2">
        <PostItem
          :key="item.id"
          v-for="item in discussionsLast"
          :item="item"
        />
      </component>
    </section>
  </div>
</template>

<script>
import { GetFilteredDiscussion } from '@/api'
import { mapState, mapActions } from 'vuex'
// import Slick from 'vue-slick'
import slick from '@/components/mixins/slick'
import ThemeItem from '../Main/ThemeItem'
import PostItem from '../Main/PostItem'

export default {
  name: 'Search',
  mixins: [slick],
  data() {
    return {
      slickComp: '',
      showFilter: false,
      searchDiscussion: '',
      SlickOptions: {
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
      SlickOptions1: {
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
      SlickOptions2: {
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
    }


  },
  components: {
    ThemeItem,
    PostItem,
    Slick: () => import('vue-slick')
  },
  methods: {
    ...mapActions('discussion', ['getDiscussionsLast']),
    search() {
      this.$store.commit('discussion/setFilteredDiscusion', [])
      GetFilteredDiscussion(this.searchDiscussion).then(res => {
        this.$store.commit('discussion/setFilteredDiscusion', res.data.items)
      })
    },
  },
  computed: {
    ...mapState('discussion', ['discussionsLast',]),
    result() {
      return this.searchedDiscusion.length == 0
    },
    searchedDiscusion() {
      return this.$store.state.discussion.searchedDiscusion
    }
  },
  mounted() {
    this.$nextTick(function() {
      this.slickComp = 'Slick'
    })
    if (this.discussionsLast.length == 0) {
      this.getDiscussionsLast()
    }
  }
}
</script>

<style scoped lang="scss">
  .show {
    display: block !important;
  }

  @media screen and (min-width: 1024px) {
    .section-themes {
      position: relative;

      &:before {
        content: "";
        display: inline-block;
        background: white;
        width: 41px;
        position: absolute;
        top: 0;
        bottom: 0;
        left: -41px;
        z-index: 1;
      }
    }
  }

  .section-discuss {
    overflow: hidden;
    padding: 0 0 0 6px;
  }

  .center {
    text-align: center;
  }
</style>
