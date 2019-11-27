<template>
  <div class="posts_item" @click.prevent="cardEvent">
    <div class="posts_item_img">
      <img v-if="item.image_url" :src="$baseUrl + item.image_url" alt="foto"/>
      <div class="truefalse"><span>{{ item.votes.true }}%</span><span>{{ item.votes.false }}%</span></div>
    </div>
    <div class="posts_item_cont">
      <div class="posts_item_title">{{ item.title }}</div>
      <div class="posts_item_bot">
        <div class="posts_item_author">{{$lang.main.authorWrap}}: <b>{{ item.author.fullname }}</b></div>
        <a href="#" v-if="$store.state.auth.auth.id !== null" :class="{'active': item.is_favorite}" class="fav_link"><span class="icon-fav"></span></a>
        <div class="posts_item_date">{{created_at}}</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PostItem',
  props: ['item'],
  computed:{
    created_at(){
      let created_at = this.item.created_at
      return created_at.slice(0, 10)
    }
  },
  methods:{
    cardEvent($event){
      if($event.target.className == 'icon-fav'){
        this.$store.dispatch('discussion/toggleDiscusionFav',this.item.id).then(disc =>{
          this.$store.commit('discussion/replaceDiscussionLast', {id : disc.id, is_favorite: disc.is_favorite})
        })
      }else{
        this.$router.push('/discussion/' + this.item.id)
      }

    }
  }
}
</script>

<style scoped>

</style>
