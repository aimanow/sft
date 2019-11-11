<template>
  <div class="authors_item" @click.prevent="cardEvent">
    <a href="#" class="fav_link" v-if="$store.state.auth.auth.id !== null"
       :class="{'active': author.is_favorite}">
      <span class="icon-fav"></span>
    </a>
    <div class="authors_item_img"><img v-if="author.avatar_url" :src="$baseUrl+author.avatar_url" alt="avatar"/></div>
    <div class="authors_item_name">{{author.fullname}}</div>
    <a href="#" class="win_close" v-if="fav">
      <span class="icon-cab7"></span>
    </a>
    <div :class="{'authors_item_likes': author.i_like}"><span class="icon-like px-1" ></span>{{author.total_likes}}</div>
    <div class="authors_item_info">
      <div class="authors_item_info_in">
        <div class="authors_info_circ"><span class="icon-i3"></span></div>
        <div class="authors_info_circ"><span class="icon-i4"></span></div>
        <div class="authors_info_circ"><span class="icon-i5"></span></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UserItem',

  props: {
    author: {
      type: Object,
    },
    fav:{
      type: Boolean
    }
  },
  methods: {
    cardEvent($event){
      if($event.target.className == "icon-fav"){
        this.$store.dispatch('profile/toggleDiscusionAuthorFav',this.author.id).then(author =>{
          this.$store.commit('profile/replaceDiscusionAuthorFav', {id : author.id, is_favorite: author.is_favorite})
        })
      }else if($event.target.classList[0] == "icon-like"){
        console.dir($event.target)
        this.$store.dispatch('profile/toggleDiscusionAuthorLike',this.author.id).then(author =>{
          this.$store.commit('profile/replaceDiscusionAuthorLike', {id : author.id, i_like: author.i_like, total_likes: author.total_likes})
        })
      }else if($event.target.className == "icon-cab7"){
        this.$emit('deleteFavorites', this.author.id )
      }else{this.$router.push('/author/' + this.author.id)}
    }
  },
}
</script>

<style scoped>
  .win_close {
    top: 5px;
    visibility: hidden;
    right: 5px;
    opacity: 0;
    transition: 0.2s ease;
  }
  .authors_item:hover .win_close {
    visibility: visible;
    opacity: 1;
  }

</style>
