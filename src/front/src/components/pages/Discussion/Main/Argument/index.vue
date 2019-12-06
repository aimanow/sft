<template>
  <div class="disc_item">
    <div class="disc_line disc_line_header">
      <div class="disc_line_cont">
        <div class="disc_line_inf">
          <div class="disc_line_name"><a href="#">{{argument.title}}</a></div>
          <div class="disc_line_athor"><span>{{$lang.main.authorWrap}}:</span> {{argument.thesis.author.fullname}}</div>
          <div class="disc_line_date">{{created_at}}</div>
        </div>
        <div class="truefalse"><span>{{argument.opinion_ratio.true}}%</span><span>{{argument.opinion_ratio.false}}%</span></div>
        <a href="#" @click.prevent="showArgumentThesis" class="disc_line_opener"><span class="icon-arrow_down"></span></a>
      </div>
    </div>
    <div class="disc_line_body" :class="{'show': show}">
      <div class="country_title">{{$lang.descAdd.selectOne}}:</div>
      <div class="disc_left_bg">
        <b>{{$lang.descAdd.argAdditional}}</b>
      </div>
      <div class="disc_right_bg">
        <b>{{$lang.descAdd.argConflict}}</b>
      </div>
      <div class="comm" @click="setArgumentId">
        <div v-if="comments.length">
          <Comment v-for="item in comments" :comment="item" :key="item.id"/>
        </div>
<!--        <div v-if="myThesis.length">-->
<!--          <Comment v-for="item in myThesis" :comment="item" :key="item.id"/>-->
<!--        </div>-->
        <div class="text-xs-center" v-if="$store.state.auth.auth.id && !is_frozen">
          <v-btn outline color="info" @click="addModal({name: 'ModalArgument', data:argument.id})">
            <v-icon>add</v-icon>
            {{$lang.descAdd.addThesis}}
          </v-btn>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { GetArgumentThesis } from '@/api'
import Comment from './Comment'
import { mapActions, mapState, mapMutations } from 'vuex'

export default {
  name: 'Argument',
  props: ['argument', 'propThesis', 'is_frozen'],
  data() {
    return {
      show: false,
      // resAllArgumentsThesis: [],
      // myThesis: [],
      comments: [],
      argumentIdPass: null
    }
  },
  components: { Comment },
  computed: {
    ...mapState('discussion', ['current_discussion', 'argument_thesises']),
    created_at() {
      return this.argument.thesis.created_at.slice(0, 10)
    }
  },
  watch: {
    propThesis(val) {
      if (val && this.argument.id == val.id) this.pushThesis(val.thesis)
    }

  },
  methods: {
    ...mapActions('modal', ['addModal']),
    ...mapMutations('discussion', ['setArgumentThesises']),
    setArgumentId() {
      this.$store.commit('discussion/setArgumentId', this.argument.id)
    },
    pushThesis(elem) {
      this.comments.push(elem)
    },
    showArgumentThesis() {
      this.show = !this.show
      if (this.comments.length < 1) {
        GetArgumentThesis(this.argument.id).then(res => {
          this.setArgumentThesises({ argument_id: this.argument.id, items: res.data.items })
          this.argumentIdPass = this.argument.id
          res.data.items.forEach((i) => {
            this.comments.push(i)
          })
        })
      }
    }
  },
}
</script>

<style scoped>
  .show {
    display: block !important;
  }
</style>
