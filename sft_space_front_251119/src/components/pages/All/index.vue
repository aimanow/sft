<template>
  <div class="center">
    <div class="h2"><h1>{{$lang.filter.all}}</h1></div>
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
              <div class="aspect_item_bg js-bg" style="background-image: url('@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
              <div class="aspect_item_text"><span class="icon-check"></span>
                <p>{{$lang.filter.karma}}</p></div>
            </a>
          </div>
          <div class="aspect_item active">
            <a href="#" class="aspect_item_img">
              <div class="aspect_item_bg js-bg" style="background-image: url('@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
              <div class="aspect_item_text"><span class="icon-check"></span>
                <p>{{$lang.filter.earth}}</p></div>
            </a>
          </div>
          <div class="aspect_item ">
            <a href="#" class="aspect_item_img">
              <div class="aspect_item_bg js-bg" style="background-image: url('@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
              <div class="aspect_item_text"><span class="icon-check"></span>
                <p>{{$lang.filter.physics}}</p></div>
            </a>
          </div>
          <div class="aspect_item active">
            <a href="#" class="aspect_item_img">
              <div class="aspect_item_bg js-bg" style="background-image: url('@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
              <div class="aspect_item_text"><span class="icon-check"></span>
                <p>{{$lang.filter.quantum}}</p></div>
            </a>
          </div>
          <div class="aspect_item ">
            <a href="#" class="aspect_item_img">
              <div class="aspect_item_bg js-bg" style="background-image: url('@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
              <div class="aspect_item_text"><span class="icon-check"></span>
                <p>{{$lang.filter.space}}</p></div>
            </a>
          </div>
          <div class="aspect_item active">
            <a href="#" class="aspect_item_img">
              <div class="aspect_item_bg js-bg" style="background-image: url('@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
              <div class="aspect_item_text"><span class="icon-check"></span>
                <p>{{$lang.filter.football}}</p></div>
            </a>
          </div>
          <div class="aspect_item ">
            <a href="#" class="aspect_item_img">
              <div class="aspect_item_bg js-bg" style="background-image: url('@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
              <div class="aspect_item_text"><span class="icon-check"></span>
                <p>{{$lang.filter.space}}</p></div>
            </a>
          </div>
          <div class="aspect_item active">
            <a href="#" class="aspect_item_img">
              <div class="aspect_item_bg js-bg" style="background-image: url('@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
              <div class="aspect_item_text"><span class="icon-check"></span>
                <p>{{$lang.filter.football}}</p></div>
            </a>
          </div>
          <div class="aspect_item ">
            <a href="#" class="aspect_item_img">
              <div class="aspect_item_bg js-bg" style="background-image: url('~@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
              <div class="aspect_item_text"><span class="icon-check"></span>
                <p>{{$lang.filter.karma}}</p></div>
            </a>
          </div>
          <div class="aspect_item active">
            <a href="#" class="aspect_item_img">
              <div class="aspect_item_bg js-bg" style="background-image: url('~@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
              <div class="aspect_item_text"><span class="icon-check"></span>
                <p>{{$lang.filter.physics}}</p></div>
            </a>
          </div>
          <div class="aspect_item active">
            <a href="#" class="aspect_item_img">
              <div class="aspect_item_bg js-bg" style="background-image: url('~@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
              <div class="aspect_item_text"><span class="icon-check"></span>
                <p>{{$lang.filter.physics}}</p></div>
            </a>
          </div>
        </div>
      </div>
    </div>
    <section>
      <v-container grid-list-lg class="pa-0">
        <v-layout row wrap >
          <v-flex xs12 class="text-xs-center">
            <v-pagination circle v-if="discussionsAll.length > 0" v-model="page" :length="total_pages" @click.native="fetchDiscussions"></v-pagination>
          </v-flex>
          <v-flex xs6 sm3 md4 v-for="item in itemsPerPage" :key="item.id">
              <ThemeItem :eventModel="true" :item="item" @fav-toggle="toggleFavorite" @freeze-toggle="toggleFreeze"/>
          </v-flex>
          <v-flex xs12 class="text-xs-center">
            <v-pagination circle v-if="discussionsAll.length > 0" v-model="page" :length="total_pages" @click.native="fetchDiscussions"></v-pagination>
          </v-flex>
        </v-layout>
      </v-container>
    </section>
  </div>
</template>

<script>
import {ToggleDiscusionFav, ToggleDiscusionFreeze, } from '@/api'
import { mapState, mapActions, mapMutations } from 'vuex'
import ThemeItem from '@/components/pages/Main/ThemeItem'
export default {
  name: 'All',
  data() {
    return {
      showFilter: false,
      page: 1,
      total_pages: null,
      total_items: null,
      items_per_page: null,
      itemsPerPage: []
    }
  },
  components:{ ThemeItem },
  methods:{
    ...mapActions('discussion', ['getDiscussionsAll']),
    ...mapMutations('discussion', ['replaceDiscussionAll']),
    fetchDiscussions(){
      this.getDiscussionsAll(this.page).then(()=>{
        let item = this.discussionsAll.find(item => item.page === this.page)
        this.itemsPerPage = item.items
      })
    },
    toggleFreeze(id){
      ToggleDiscusionFreeze(id).then(res=>{
        this.replaceDiscussionAll({page: this.page, id, is_favorite: res.data.is_favorite, is_frozen: res.data.is_frozen})
      })
    },
    toggleFavorite(id){
      ToggleDiscusionFav(id).then(res =>{
        this.replaceDiscussionAll({page: this.page, id, is_favorite: res.data.is_favorite})
      })

    }
  },
  computed:{
    ...mapState('discussion', ['discussionsAll','paginationSetting', 'removedFavDisc']),
  },
  mounted () {
    if (this.discussionsAll.length == 0) {
      this.getDiscussionsAll(this.page).then(res =>{
        this.total_pages = res.total_pages
        this.total_items = res.total_items
        this.items_per_page = res.items_per_page
        this.itemsPerPage = this.discussionsAll[0].items
      })
    }else{
      this.total_pages = this.paginationSetting.total_pages
      this.total_items = this.paginationSetting.total_items
      this.items_per_page = this.paginationSetting.items_per_page
      this.itemsPerPage = this.discussionsAll[0].items
    }
    this.removedFavDisc.forEach(id =>{
      this.replaceDiscussionAll({page: this.page, id, is_favorite: false})
    })
  },
  watch: {
    page(page){
      this.removedFavDisc.forEach(id =>{
        this.replaceDiscussionAll({page, id, is_favorite: false})
      })

    }
  }

}
</script>

<style scope lang="scss">
  .posts_item{
    height: auto;
    width: 100%;
    margin: 0;
  }
</style>
