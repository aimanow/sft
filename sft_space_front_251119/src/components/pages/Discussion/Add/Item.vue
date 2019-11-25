<template>
  <div class="aspect_item " :class="{'active': active}" @click.prevent="toggle">
    <a class="aspect_item_img">
      <div class="aspect_item_bg js-bg"><img v-if="item.image_url" :src="$baseUrl + item.image_url" alt="foto"/></div>
      <div class="aspect_item_text"  :class="{'active': small}"><span class="icon-check"></span><p>{{$lang.aspects[item.title] || item.title}}</p></div>
    </a>
  </div>
</template>

<script>
export default {
  name: 'Item',
  data(){
    return{
      active: false
    }
  },
  props: ['item', 'count', 'small'],
  methods:{
    toggle(){
      if (this.count > 2 && !this.active) return false
      this.active = !this.active
      if(this.active){
        this.$emit('checkedAspect', this.item.id)
      }else{this.$emit('checkOffAspect', this.item.id)}
    }
  }
}
</script>

<style scoped>
.aspect_item_text.active{
  top: 9px;
}
</style>
