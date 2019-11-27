<template>
  <div class="aspect_item " :class="{'active': active}" @click.prevent="filter">
    <a href="#" class="aspect_item_img">
      <div class="aspect_item_bg js-bg"><img v-if="item.image_url" :src="$baseUrl + item.image_url" alt="foto"/></div>
      <div class="aspect_item_text">
        <span class="icon-check"></span>
        <p>{{$lang.aspects[item.title] || item.title}}</p>
      </div>
    </a>
  </div>
</template>

<script>
export default {
  name: 'Item',
  data() {
    return {
      active: false
    }
  },
  props: ['item', 'disable'],
  methods:{
    filter(){
      if(this.disable) return false
      this.active = !this.active
      if(this.active){
        this.$store.commit('discussion/setSelectedAspects', this.item.id)
      }else{
        this.$store.commit('discussion/deleteSelectedAspects', this.item.id)
      }
    },
  }
}
</script>

<style scoped>

</style>
