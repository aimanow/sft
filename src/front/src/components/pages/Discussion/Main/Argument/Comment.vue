<template>
  <div class="comm_item">
    <div class="comm_row" :class="{'comm_row_right': !comment.position}">
      <div class="comm_ava"><img v-if="comment.author.avatar_url" :src="$baseUrl+comment.author.avatar_url" alt="image"></div>
      <div class="comm_block">
        <div class="comm_block_bord">
          <div class="comm_img">
            <scale :x="comment.votes.mean_x" :y="comment.votes.mean_y" @click.native="setScale"/>
          </div>
          <div class="comm_cont">
            <div class="comm_txt">{{comment.message}}.</div>
            <div class="comm_adds" :class="{'open': toggle}">
              <div class="comm_adds_opener" v-if="comment.attachments.length" @click="showMore">{{$lang.descAdd.attachments}}<span
                class="icon-arrow_down"></span></div>
              <div class="comm_adds_drop">
                <div v-for="item in comment.attachments" :key="item.id">
                  <div class="adds_file" v-if="item.type == 'link'">
                    <!-- <a href="#" class="adds_file_rem"><span class="icon-cab7"></span></a>
                    <a href="#" class="adds_file_check"><span class="icon-check"></span></a> -->
                    <a :href="item.payload_url" class="adds_file_txt" target="_blank">{{item.payload_url}}</a>
                  </div>
                  <div class="adds_file adds_file-sm" v-if="item.type == 'file'">
                    <!-- <a href="#" class="adds_file_rem"><span class="icon-cab7"></span></a>
                    <a href="#" class="adds_file_check"><span class="icon-check"></span></a> -->
                    <div class="adds_file_ico"><span class="icon-doc1"></span></div>
                    <a :href="$baseUrl+item.payload_url" class="adds_file_txt">{{item.type}}</a>
                  </div>
                </div>
              </div>
            </div>
            <!-- <div class="comm_bot">
              <div class="comm_date">18:45</div>
              <div class="comm_ans"><a href="#">Ответы
                <span class="inline" v-if="responseThesisIdComments === null">0</span>
                <span class="inline" v-else>
                  <span class="inline" v-if="responseThesisIdComments.items.length == 0">0</span>
                  <span class="inline" v-else>{{responseThesisIdComments.items[0].total_comments}}</span>
                </span>
                </a>
              </div>
              <div class="comm_compl"><a href="#">Пожаловаться</a></div>
            </div> -->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { GetThesisIdComments } from '@/api'
import { mapActions, mapState } from 'vuex'
import scale from './Scale'

export default {
  name: 'Comment',
  props: ['comment'],
  data: () => ({
    toggle: false,
    responseThesisIdComments: null,

  }),
  watch: {
    'comment.message': () => {
      console.log(123)
    }
  },
  components: { scale },
  computed: {
    ...mapState('auth', ['auth'])
  },
  methods: {
    ...mapActions('modal', ['addModal']),
    setScale() {
      if (this.auth.id === null) return this.$store.commit('openDialog', this.$lang.auth.voteLogin)
      if (this.auth.id !== this.comment.author.id && this.comment.votes.my_vote == null) {
        this.addModal({ name: 'DiscussionGraph' })
        this.$store.commit('discussion/setThesisId', this.comment.id)
      }
    },
    showMore() {
      this.toggle = !this.toggle
    }
  },
  async created() {
    await GetThesisIdComments(this.comment.id).then(res => {
      this.responseThesisIdComments = res.data
    })
  },
}
</script>

<style scoped>
  .inline {
    display: inline-block;
  }
</style>
