<template>
  <div class="center">
    <div class="h2 mb-5"><h1>Добавить аспекты в избранное</h1></div>
      <div class="aspect aspect-fav" >
        <Item v-for="item in itemsPerPage" :key="item.id" :item="item" @toggle1="Update"/>
      </div>
      <v-layout row wrap >
        <v-flex xs12 class="text-xs-center">
          <v-pagination circle v-if="all_aspects.length > 0" v-model="page" :length="total_pages" @click.native="fetchAspects"></v-pagination>
        </v-flex>
      </v-layout>
  </div>
</template>

<script>
import { mapState, mapActions, mapMutations } from 'vuex'
import Item from './Item'
export default {
  name: 'Aspects',
  data: ()=>({
    page: 1,
    total_pages: null,
    total_items: null,
    items_per_page: null,
    itemsPerPage: []
  }),
  components:{Item},
  computed: {
    ...mapState('profile', ['all_aspects', 'paginationSetting']),
    ...mapState('auth', ['auth']),
  },

  methods: {
    ...mapActions('profile', ['GetAllAspects']),
    ...mapMutations('profile', ['UpdateAspects']),
    Update(payload){
      this.UpdateAspects({page: this.page, id: payload.id, is_favorite: payload.is_favorite})
    },
    fetchAspects(){
      this.GetAllAspects(this.page).then(()=>{
        let item = this.all_aspects.find(item => item.page === this.page);
        this.itemsPerPage = item.items
      })
    },
  },
  mounted () {
    if (this.all_aspects.length == 0) {
      this.GetAllAspects(this.page).then(res =>{
        this.total_pages = res.total_pages
        this.total_items = res.total_items
        this.items_per_page = res.items_per_page
        this.itemsPerPage = this.all_aspects[0].items
      })
    }else{
      this.total_pages = this.paginationSetting.total_pages
      this.total_items = this.paginationSetting.total_items
      this.items_per_page = this.paginationSetting.items_per_page
      this.itemsPerPage = this.all_aspects[0].items
    }

  }
}
</script>

<style>

</style>
