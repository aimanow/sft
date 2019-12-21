<template>
  <div class="country_wr">
    <div class="country_title">{{$lang.descAdd.select}}</div>
    <div class="aspect aspect-check">
      <Item v-for="item in aspects" :key="item.id || item.title" :item="item"/>
<!--      <div class="aspect_item aspect_item_new active" @click.prevent="addAspect" v-if="isOwner">-->
      <div class="aspect_item aspect_item_new active" @click.prevent="addAspect" v-if="false">
      <a href="#" class="aspect_item_img">
          <div class="aspect_item_text">
            <span class="icon-plus"></span>
            <p>{{$lang.descAdd.add}}</p>
          </div>
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import {mapActions} from 'vuex'
import Item from './Item'

export default {
  name: 'Aspects',

  components: {Item},
  methods: {
    ...mapActions('modal', ['addModal']),
    addAspect() {
      this.addModal({name: 'AspectEdit'})
    }
  },
  props: ['aspects'],
  computed:{
    isOwner(){
      return this.$store.state.discussion.current_discussion.author.id === this.$store.state.auth.auth.id
    }
  }
}
</script>

<style scoped>
  .aspect_item_new.active .aspect_item_text .icon-plus {
    color: rgb(5, 96, 206);
    display: block;
    font-size: 2.2em;
    margin: 0 0 8px;
  }

  .aspect_item_new.active .aspect_item_text p {
    color: rgb(5, 96, 206);
  }

  .aspect_item_new {
    border: solid 2px rgb(5, 96, 206);
    box-shadow: unset !important;
    -webkit-box-shadow: unset !important;
  }

  .aspect_item_new .aspect_item_img:after {
    background: none !important;
    opacity: unset !important;
  }

  .aspect_item_new:hover {
    box-shadow: 0 8px 12px rgba(0, 0, 0, 0.22) !important;
    -webkit-box-shadow: 0 8px 12px rgba(0, 0, 0, 0.22) !important;
  }
</style>
