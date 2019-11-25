<template>
  <div class="center">
    <section class="section-favorite">
      <div class="h2"><h1>{{$lang.profile.favTitle}}</h1></div>
      <ul class="tabs">
        <li :class="{'active': index === 1}"><a href="#" @click.prevent="index = 1">{{$lang.profile.favAsp}}</a></li>
        <li :class="{'active': index === 2}"><a href="#" @click.prevent="index = 2">{{$lang.profile.favDisc}}</a></li>
        <li :class="{'active': index === 3}"><a href="#" @click.prevent="index = 3">{{$lang.profile.favAvt}}</a></li>
      </ul>
      <Aspects v-if="index === 1" />
      <Discuss v-if="index === 2" @removeDisc="removeDisc"/>
      <Authors v-if="index === 3" @removeAuthor="removeAuthor"/>
    </section>
  </div>
</template>

<script>
import { mapMutations } from 'vuex'
export default {
  name: 'Favorites',
  components: {
    Aspects: () => import('./Aspects.vue'),
    Authors: () => import('./Authors.vue'),
    Discuss: () => import('./Discuss.vue'),
  },
  data() {
    return {
      index: 3,
      removedAuthors:[],
      removedDiscussions:[],
    }
  },
  methods:{
    ...mapMutations('profile', ['cleareFavoritesDiscussions', 'cleareFavoritesDiscussionAuthors']),
    ...mapMutations('discussion', ['setRemovedFavDisc', 'setRemovedFavAuthor']),
    removeAuthor(id){
      this.removedAuthors.push(id)
    },
    removeDisc(id){
      this.removedDiscussions.push(id)
    },
  },
  beforeDestroy(){
    this.cleareFavoritesDiscussions()
    this.cleareFavoritesDiscussionAuthors()
    this.setRemovedFavDisc(this.removedDiscussions)
    this.setRemovedFavAuthor(this.removedAuthors)
  },
  created(){
    this.setRemovedFavDisc(this.removedDiscussions)
    this.setRemovedFavAuthor(this.removedAuthors)
  }

}
</script>

<style scoped>

</style>
