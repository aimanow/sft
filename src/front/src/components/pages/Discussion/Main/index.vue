<template>
  <div class="center">
    <section class="section_discussion" v-if="discussion">
      <div class="h2"><h1 :class="{'frozen': discussion.is_frozen}">{{ discussion.title + isFrozen}}</h1>
        <div class="text-xs-right">
          <v-icon v-if="permission" :class="{'admin': permission }" :color="is_deleted" class="pointer"
                  @click="deleteDiscussion($route.params.id)">delete
          </v-icon>
          <v-icon v-if="permission && !discussion.is_frozen" :color="is_frozen" :class="{'admin': permission }" class="pointer"
                  @click="toggleFreeze($route.params.id)">lock_open
          </v-icon>
          <v-icon v-if="discussion.is_frozen" :class="{'admin': permission }" class="pointer" @click="toggleFreeze($route.params.id)">lock
          </v-icon>
        </div>
      </div>
      <div class="country_libra">
        <div class="country_libra_in">
          <div class="country_libra_svg"></div>
          <div class="c_b blue_c">
            <span class="icon-check"></span>
            <v-progress-circular :size="circleSizeTrue" :value="discussionVote.votes.true" color="blue" width="12" rotate="-90">
              {{discussionVote.votes.true}}%
            </v-progress-circular>
          </div>
          <div class="c_b blue_r">
            <span class="icon-close"></span>
            <v-progress-circular :size="circleSizeFalse" :value="discussionVote.votes.false" color="red" width="12" rotate="-90">
              {{discussionVote.votes.false}}%
            </v-progress-circular>
          </div>
        </div>
      </div>
      <div class="discussion-description">
        {{discussion.description}}
      </div>
      <Aspects :aspects="discussion.aspects"/>
      <div class="country_wr">
        <div class="country_title">{{$lang.descAdd.arg}}:</div>
        <div class="disc" v-if="discussion_arguments.length>0">
          <Argument v-for="(argument, index) in filterArgument" :argument="argument" :key="`argument_${index}`"
                    :propThesis="thesis"
                    :is_frozen=" discussion.is_frozen"/>
          <div v-if="$store.state.auth.auth.id && !discussion.is_frozen" class="disc_line_plus"
               @click.prevent="addModal({name: 'ModalArgument'})"><a href="#"><span
            class="icon-plus"></span><span>{{$lang.descAdd.addNew}}</span></a></div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import {mapState, mapActions} from 'vuex'
import {GetCurrentDiscussions, ToggleDiscusionFreeze, DeleteDiscussion} from '@/api'
import Aspects from './Aspects'
import Argument from './Argument'

export default {
  name: 'MainDiscussion',

  data() {
    return {
      discussion: null,
      thesis: null,
      deleted: false,
      window: {
        width: 0
      }
    }
  },

  components: {Aspects, Argument},

  computed: {
    ...mapState('discussion', [
      'discussion_arguments',
      'selected_aspects',
      'current_discussion'
    ]),
    ...mapState('auth', ['permission']),
    is_frozen() {
      return this.discussion.is_frozen ? 'red' : ''
    },
    is_deleted() {
      return this.deleted ? 'red' : ''
    },
    isFrozen() {
      return this.discussion.is_frozen ? ' (Дискусія заморожена)' : ''
    },
    discussionVote() {
      if (this.current_discussion) {
        return this.current_discussion
      } else {
        return this.discussion
      }
    },
    filterArgument() {
      return this.discussion_arguments.filter((arg) => {
        return arg.aspect_ids.some((_id) => {
          return this.selected_aspects.some(selected_aspect => selected_aspect == _id)
        }) || this.selected_aspects.length === 0
      })
    },
    circleSizeTrue() {
      if (this.window.width < 600) return 100
      if (this.discussion.votes.true >= this.discussion.votes.false) {
        return 174
      } else {
        return 150
      }
    },
    circleSizeFalse() {
      if (this.window.width < 600) return 100
      if (this.discussion.votes.true <= this.discussion.votes.false) {
        return 174
      } else {
        return 150
      }
    }
  },

  methods: {
    ...mapActions('modal', ['addModal']),
    ...mapActions('discussion', ['getDiscussionArguments']),
    handleResize() {
      if (process.client) {
        this.window.width = window.innerWidth
      }
    },
    toggleFreeze(id) {
      ToggleDiscusionFreeze(id).then(res => {
        this.discussion.is_frozen = res.data.is_frozen
      })
    },
    deleteDiscussion(id) {
      DeleteDiscussion(id).then(() => {
        this.deleted = true
      })
    },
    async fetch() {
      await Promise.all([
        this.getDiscussionArguments(this.$route.params.id),
        GetCurrentDiscussions(this.$route.params.id).then(res => {
          this.discussion = res.data
          this.$store.commit('discussion/setCurrentDiscussion', res.data)
        }),
      ])
    }
  },
  mounted() {
    this.$store.commit('discussion/setCurrentDiscussion', null)
    this.$store.subscribe((mutation, state) => {
      switch (mutation.type) {
        case 'discussion/pushDiscussionThesis': {
          const status = state.discussion.argument_thesis
          this.thesis = status
          break
        }
      }
    })
  },
  created() {
    this.fetch()
    if (process.client) {
      window.addEventListener('resize', this.handleResize)
    }
    this.handleResize()
  },
  destroyed() {
    if (process.client) {
      window.removeEventListener('resize', this.handleResize)
    }
  },
  watch: {
    'discussion_arguments': function () {
      this.$forceUpdate()
    },
    '$route.params.id': function (id) {
      this.$forceUpdate()
    }
  }
}
</script>

<style scoped>
  .frozen {
    color: red;
  }

  .c_b {
    background: none;
    width: auto;
    height: auto;
    background: none;
  }

  .discussion-description {
    font-size: 18px;
    margin-bottom: 24px;
  }

  .discussion-description:before {
    margin: 0 11px 4px 0;
    content: '';
    display: inline-block;
    width: 12px;
    height: 12px;
    vertical-align: middle;
    border: 4px solid #0560CE;
    border-radius: 50%;
  }
</style>
