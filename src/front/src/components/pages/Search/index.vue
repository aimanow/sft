<template>
  <div class="center">
    <div class="center_search m-show">
      <form @submit.prevent="search">
        <input type="text" placeholder="Что вы ищете?" class="t-inp" v-model="searchDiscussion">
        <button class="search-btn" type="submit"><span class="icon-search"></span></button>
      </form>
    </div>
    <section class="section-discuss">
      <div class="h2"><h1>Результат поиска</h1></div>

      <a href="#" @click.prevent="showFilter = !showFilter" class="filter_link btn btn-bo rd-blue"><span class="icon-filter"></span>Фильтр</a>
      <div class="filter_block" :class="{'show' : showFilter}">
        <div class="filter_block_top">
          <div class="filter_block_res_title">Выберите нужные пункты:</div>
          <div class="filter_block_rads rads">
            <div class="rads_item">
              <label class="radio"><input type="checkbox" checked="" placeholder="">
                <span class="radio_text">По дате <img src="@/assets/svg/arrs.svg" alt=""></span>
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
              <label class="radio"><input type="checkbox" placeholder=""><span class="radio_text">По популярности</span></label>
            </div>
          </div>
        </div>
        <div class="filter_block_res">
          <div class="filter_block_res_title">По аспектам:</div>
          <div class="aspect aspect-check aspect-gr">
            <div class="aspect_item">
              <a href="#" class="aspect_item_img">
                <div class="aspect_item_bg js-bg" style="background-image: url('@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
                <div class="aspect_item_text"><span class="icon-check"></span>
                  <p>Карма</p></div>
              </a>
            </div>
            <div class="aspect_item active">
              <a href="#" class="aspect_item_img">
                <div class="aspect_item_bg js-bg" style="background-image: url('@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
                <div class="aspect_item_text"><span class="icon-check"></span>
                  <p>Земля</p></div>
              </a>
            </div>
            <div class="aspect_item ">
              <a href="#" class="aspect_item_img">
                <div class="aspect_item_bg js-bg" style="background-image: url('@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
                <div class="aspect_item_text"><span class="icon-check"></span>
                  <p>Физика</p></div>
              </a>
            </div>
            <div class="aspect_item active">
              <a href="#" class="aspect_item_img">
                <div class="aspect_item_bg js-bg" style="background-image: url('@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
                <div class="aspect_item_text"><span class="icon-check"></span>
                  <p>Квантовая механика</p></div>
              </a>
            </div>
            <div class="aspect_item ">
              <a href="#" class="aspect_item_img">
                <div class="aspect_item_bg js-bg" style="background-image: url('@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
                <div class="aspect_item_text"><span class="icon-check"></span>
                  <p>Космос</p></div>
              </a>
            </div>
            <div class="aspect_item active">
              <a href="#" class="aspect_item_img">
                <div class="aspect_item_bg js-bg" style="background-image: url('@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
                <div class="aspect_item_text"><span class="icon-check"></span>
                  <p>Футбол</p></div>
              </a>
            </div>
            <div class="aspect_item ">
              <a href="#" class="aspect_item_img">
                <div class="aspect_item_bg js-bg" style="background-image: url('@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
                <div class="aspect_item_text"><span class="icon-check"></span>
                  <p>Космос</p></div>
              </a>
            </div>
            <div class="aspect_item active">
              <a href="#" class="aspect_item_img">
                <div class="aspect_item_bg js-bg" style="background-image: url('@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
                <div class="aspect_item_text"><span class="icon-check"></span>
                  <p>Футбол</p></div>
              </a>
            </div>
            <div class="aspect_item ">
              <a href="#" class="aspect_item_img">
                <div class="aspect_item_bg js-bg" style="background-image: url('~@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
                <div class="aspect_item_text"><span class="icon-check"></span>
                  <p>Карма</p></div>
              </a>
            </div>
            <div class="aspect_item active">
              <a href="#" class="aspect_item_img">
                <div class="aspect_item_bg js-bg" style="background-image: url('~@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
                <div class="aspect_item_text"><span class="icon-check"></span>
                  <p>Физика</p></div>
              </a>
            </div>
            <div class="aspect_item active">
              <a href="#" class="aspect_item_img">
                <div class="aspect_item_bg js-bg" style="background-image: url('~@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
                <div class="aspect_item_text"><span class="icon-check"></span>
                  <p>Физика</p></div>
              </a>
            </div>
            <div class="aspect_item ">
              <a href="#" class="aspect_item_img">
                <div class="aspect_item_bg js-bg" style="background-image: url('~@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
                <div class="aspect_item_text"><span class="icon-check"></span>
                  <p>Космос</p></div>
              </a>
            </div>
            <div class="aspect_item active">
              <a href="#" class="aspect_item_img">
                <div class="aspect_item_bg js-bg" style="background-image: url('~@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
                <div class="aspect_item_text"><span class="icon-check"></span>
                  <p>Футбол</p></div>
              </a>
            </div>
            <div class="aspect_item ">
              <a href="#" class="aspect_item_img">
                <div class="aspect_item_bg js-bg" style="background-image: url('~@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
                <div class="aspect_item_text"><span class="icon-check"></span>
                  <p>Космос</p></div>
              </a>
            </div>
            <div class="aspect_item active">
              <a href="#" class="aspect_item_img">
                <div class="aspect_item_bg js-bg" style="background-image: url('~@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
                <div class="aspect_item_text"><span class="icon-check"></span>
                  <p>Футбол</p></div>
              </a>
            </div>
          </div>
        </div>
      </div>
      <div v-if="result" class="empty-res">
        <img src="@/assets/img/search.png" alt="foto"/>
        <p>По вашему запросу ничего не <br/>найдено.</p>
      </div>
      <Slick
        ref="slick2"
        class="posts posts-sm"
        :options="SlickOptions">
        <ThemeItem
          v-for="item in searchedDiscusion" :key="item.id"
          :item="item"
          />
      </Slick>
    </section>
    <section class="section-discuss">
      <div class="h2"><h2>Похожие темы</h2></div>
      <Slick
        ref="slick3"
        class="posts posts-sm"
        :options="SlickOptions1">
        <ThemeItem
          v-for="item in searchedDiscusion" :key="item.id"
          :item="item"
          />
      </Slick>
    </section>
    <section class="section-themes">
      <div class="h2"><h2>Тема дня</h2></div>
      <Slick
        ref="slick1"
        class="posts slider-posts"
        :options="SlickOptions2">
        <PostItem
          :key="item.id"
          v-for="item in discussionsLast"
          :item="item"
          />
      </Slick>
    </section>
  </div>
</template>

<script>
  import {GetFilteredDiscussion} from '@/api'
  import { mapState, mapActions } from 'vuex'
  import Slick from 'vue-slick'
  import slick from '@/components/mixins/slick'
  import ThemeItem from '../Main/ThemeItem'
  import PostItem from '../Main/PostItem'
  export default {
    name: "Search",
    mixins: [slick],
    data() {
      return {
        showFilter: false,
        searchDiscussion: "",
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
    components:{ ThemeItem, PostItem, Slick },
    methods:{
      ...mapActions('discussion', ['getDiscussionsLast']),
      search(){
          this.$store.commit('discussion/setFilteredDiscusion', [])
        GetFilteredDiscussion(this.searchDiscussion).then(res =>{
            this.$store.commit('discussion/setFilteredDiscusion', res.data.items)
          })
      },
    },
    computed:{
      ...mapState('discussion', ['discussionsLast',]),
      result(){
        return this.searchedDiscusion.length == 0
      },
      searchedDiscusion(){
        return this.$store.state.discussion.searchedDiscusion
      }
    },
    mounted () {
      if (this.discussionsLast.length == 0) { this.getDiscussionsLast() }
    }
  }
</script>

<style scoped lang="scss">
.show {
  display: block !important;
}
@media screen and (min-width: 1024px){
  .section-themes{
    position:relative;
    &:before{
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
.section-discuss{
  overflow: hidden;
  padding: 0 0 0 6px;
}
.center{
  text-align: center;
}
</style>
