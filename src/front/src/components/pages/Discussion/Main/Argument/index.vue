<template>
  <div class="disc_item">
    <div class="disc_line disc_line_header">
      <div class="disc_line_cont">
        <div class="disc_line_inf">
          <div class="disc_line_name"><a href="#">{{argument.title}}</a></div>
          <div class="disc_line_athor"><span>Автор:</span> {{argument.thesis.author.fullname}} </div>
          <div class="disc_line_date">{{created_at}}</div>
        </div>
        <div class="truefalse"><span>{{argument.opinion_ratio.true}}%</span><span>{{argument.opinion_ratio.false}}%</span></div>
        <a href="#" @click.prevent="showArgumentThesis" class="disc_line_opener"><span class="icon-arrow_down"></span></a>
      </div>
    </div>
    <div class="disc_line_body" :class="{'show': show}">
      <div class="country_title">Выберите аспект:</div>
      <div class="disc_left_bg">
        <b>Дополнение</b>
      </div>
      <div class="disc_right_bg">
        <b>Опровержение:</b>
      </div>
      <div class="comm" @click="setArgumentId">
        <div  v-if="resAllArgumentsThesis.length">
          <Comment v-for="item in resAllArgumentsThesis" :comment="item" :key="item.id" />
        </div>
        <div v-if="myThesis.length">
          <Comment v-for="item in myThesis" :comment="item" :key="item.id" />
        </div>
        <div class="text-xs-center" v-if="$store.state.auth.auth.id && !is_frozen" >
          <v-btn outline color="info" @click="addModal({name: 'ModalArgument', data:argument.id})">
            <v-icon>add</v-icon>
            Add Thesis
          </v-btn>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import {GetArgumentThesis} from '@/api'
  import Comment from './Comment'
  import { mapActions, mapState } from 'vuex'
  export default {
    name: "Argument",
    props: ['argument', 'propThesis', "is_frozen"],
    data() {
      return {
        show: false,
        resAllArgumentsThesis: [],
        myThesis: []
      }
    },
    components: { Comment },
    computed:{
      ...mapState('discussion', ['current_discussion']),
      created_at(){
        return this.argument.thesis.created_at.slice(0,10)

      }
    },
    watch:{
      propThesis(val){
        if(val && this.argument.id == val.id) this.pushThesis(val.thesis)
      }

    },
    methods: {
      ...mapActions('modal', ['addModal']),
      setArgumentId(){
        this.$store.commit('discussion/setArgumentId', this.argument.id)
      },
      pushThesis(elem){
        this.myThesis.push(elem)
      },
      showArgumentThesis(){
        this.show = !this.show
        if(this.resAllArgumentsThesis.length == 0){
          GetArgumentThesis(this.argument.id).then(res => {
            this.resAllArgumentsThesis = res.data.items
          })
        }
      }
    },
  }
</script>

<style scoped>
.show{
  display: block !important;
}
</style>
