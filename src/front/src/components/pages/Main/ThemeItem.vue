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
        <v-icon v-if="permission" :class="{'admin': permission }" :color="is_deleted">delete</v-icon>
        <v-icon v-if="permission && !item.is_frozen" :color="is_frozen" :class="{'admin': permission }">lock_open</v-icon>
        <v-icon v-if="item.is_frozen" :class="{'admin': permission }">lock</v-icon>
        <div class="posts_item_date">{{created_at}}</div>
      </div>
    </div>
  </div>
</template>
<script>
import {mapState} from 'vuex'
import {DeleteDiscussion} from '@/api'
export default {
  name: 'ThemeItem',
  props: ['item', 'eventModel'],
  data(){
    return{
      deleted: false,
    }
  },
  computed:{
    ...mapState('auth', ['permission']),
    is_frozen(){
      return this.item.is_frozen ? 'red' : ''
    },
    is_deleted(){
      return this.deleted ? 'red' : ''
    },
    created_at(){
      let created_at = this.item.created_at;
      return created_at.slice(0, 10)
    }
  },
  methods: {
    cardEvent($event){
      if($event.target.classList[0] == "v-icon"){
        if($event.target.innerText == 'lock_open' || $event.target.innerText == 'lock'){
          this.$emit("freeze-toggle", this.item.id)
        }else if($event.target.innerText == 'delete'){
            DeleteDiscussion(this.item.id).then(()=>{
              this.deleted = true;
            })
        }


        return;
      }
      if($event.target.className == "icon-fav"){
        if(this.eventModel){
            this.$emit("fav-toggle", this.item.id)
        }else{
          this.$store.dispatch('discussion/toggleDiscusionFav',this.item.id).then(disc =>{
            this.$store.commit('discussion/replaceDiscussionTop', {id : disc.id, is_favorite: disc.is_favorite})
          })
        }
      }else {
        this.$router.push('/discussion/' + this.item.id)
      }
    }
  },
}
</script>

<style scoped>
.posts_item{
  height: auto;
  width: 100%;
  margin: 0;
}
.v-icon{
  float: right;
  margin-top: -10px;
  cursor: pointer;
}
.v-icon.admin:hover{
  color:#FF441D;
}
</style>
