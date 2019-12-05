<template>
  <div @click.prevent="selected" class="aspect_item" :class="{active}">
    <a href="#" class="aspect_item_img">
      <div class="aspect_item_bg js-bg">
        <img v-if="item.image_url" :src="$baseUrl+item.image_url" :alt="item.title"/>
      </div>
      <div class="aspect_item_text">
        <span class="icon-check"></span>
        <p>{{ item.title }}</p>
      </div>
    </a>
  </div>

</template>

<script>
export default {
  name: 'argumentItem',

  props: ['item'],

  data () {
    return {
      active: false
    }
  },

  methods: {
    selected () {
      this.active = !this.active
      if(this.active){
        this.$emit('selected', this.item.id)
      }

    }
  }
}
</script>

<style scoped>
.aspect_item_text{
  top: 9px;
}
</style>
