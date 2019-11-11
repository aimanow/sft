<template>
  <div class="aspect_item " :class="{'active': active}" @click.prevent="toggle">
    <v-icon v-if="permission" :class="{'admin': permission }" class="pointer" :color="is_deleted">delete</v-icon>
    <a href="#" class="aspect_item_img">
      <div class="aspect_item_bg js-bg"><img v-if="item.image_url" :src="$baseUrl + item.image_url" alt="foto"/></div>
      <div class="aspect_item_text">
        <span class="icon-check"></span>
        <p>{{item.title}}</p>
      </div>
    </a>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import {DeleteAspect} from '@/api'
  export default {
    name: "Item",
    data() {
      return {
        deleted: false
      }
    },
    props: ['item'],
    computed:{
      active(){
        return this.item.is_favorite
      },
      ...mapState('auth', ['permission']),
      is_deleted(){
        return this.deleted ? 'red' : 'white'
      },
    },
    methods:{
      ...mapActions('profile', ['toggleAspects',]),
      toggle(e){
        if(e.target.innerText == "delete"){
          this.remove()
          return false;
        }else{
          this.toggleAspects(this.item.id).then(res => {
            this.$emit('toggle1', res.data)
          })
        }
      },
      remove(){
        DeleteAspect(this.item.id).then(()=>{
          this.deleted = true;
        })
      }
    },
  }
</script>

<style scoped>
  .v-icon{
    position: absolute;
    z-index: 5;
    right: 0;
  }
</style>
