<template>
  <div class="aspect aspect-fav">
    <aspect v-for="item in favorite_aspects" :key="item.id" :item="item" :disable="true"/>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import aspect from '@/components/pages/Discussion/Main/Aspects/Item'
export default {
  name: 'FavoriteAspects',

  computed: {
    ...mapState('auth', ['auth']),
    ...mapState('profile', ['all_aspects']),
    favorite_aspects(){
      if(this.all_aspects.length){
        let arr = [];
        this.all_aspects.forEach(page=>{
          arr = arr.concat(page.items)
        });
        return arr.filter(aspect=>{ return aspect.is_favorite === true})
      }else{return []}

    }
  },
  components:{aspect},
  methods: {
    ...mapActions('profile', ['GetAllAspects']),
  },
  mounted () {
    if (this.all_aspects.length == 0) { this.GetAllAspects()}
  }
}
</script>
