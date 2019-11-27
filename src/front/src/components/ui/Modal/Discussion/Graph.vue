<template>
  <div class="win win-schedule" id="win-schedule">
    <div class="win_cont">
      <div class="schedule_block">
        <div class="schedule_block_in" ref="box" @mousedown="setScale">
          <div class="schedule_block_c" ref="ball"></div>
        </div>
        <div class="schedule_txt">
          <div :style="$lang.descAdd.graphCredibleness.length<13?'top: 10px; position: relative':''">{{$lang.descAdd.graphCredibleness}}
          </div>
        </div>
        <div class="schedule_txt2">
          <div>{{$lang.descAdd.graphPersuasiveness}}</div>
        </div>
        <div class="schedule_n schedule_n0">0</div>
        <div class="schedule_n schedule_n5">5</div>
        <div class="schedule_n schedule_n10">10</div>
        <div class="schedule_n schedule_n52">5</div>
        <div class="schedule_n schedule_n102">10</div>
      </div>

      <div class="schedule_block_bottom">
        <div class="schedule_left">
          <div class="schedule_rline">{{$lang.descAdd.graphPersRaiting}}: <span>{{x}}</span></div>
          <div class="schedule_rline">{{$lang.descAdd.graphCredRaiting}}: <span>{{y}}</span></div>
        </div>
        <div class="schedule_right">
          <a href="#" class="btn" @click.prevent="submit">{{$lang.descAdd.graphCommit}}</a>
        </div>
      </div>
    </div>
    <a href="#" class="win_close" @click.prevent="$store.commit('modal/closeAllModal')"><span class="icon-cab7"></span></a>
  </div>
</template>

<script>
import { PatchtThesisVotes, GetCurrentDiscussions, GetArguments } from '@/api'

export default {
  name: 'Graph',
  data() {
    return {
      top: 5,
      left: 5
    }
  },
  mounted() {

    let id = this.$store.state.discussion.thesisId

    const thesis = this.$store.state.discussion.thesises[id]

    this.top = thesis.votes.my_vote.y
    this.left = thesis.votes.my_vote.x

    let halfBall = 21.5
    let coordsBox = this.getCoords(this.$refs.box)

    const top = Math.round(((10 - this.top) / 10) * coordsBox.h - halfBall)
    const left = Math.round((this.left / 10) * coordsBox.w - halfBall)

    this.$refs.ball.style.left = left + 'px'
    this.$refs.ball.style.top = top + 'px'
  },
  computed: {
    x() {
      return this.left <= 0 ? 0 : this.left > 10 ? 10 : this.left
    },
    y() {
      return this.top <= 0 ? 0 : this.top > 10 ? 10 : this.top
    }
  },
  methods: {
    getCoords(elem) {
      let box = elem.getBoundingClientRect()
      return {
        top: box.top,
        left: box.left,
        h: box.height,
        w: box.width
      }
    },
    setScale(e) {
      let ball = this.$refs.ball
      let box = this.$refs.box
      let coordsBox = this.getCoords(box)
      let halfBall = 21.5
      let shiftX = coordsBox.left + halfBall
      let shiftY = coordsBox.top + halfBall
      let self = this
      box.appendChild(ball)

      function moveAt(e) {
        let left = e.clientX - shiftX
        let top = e.clientY - shiftY
        ball.style.left = left + 'px'
        ball.style.top = top + 'px'
        self.top = 10 - Math.round((top + halfBall) / coordsBox.h * 10)
        self.left = Math.round((left + halfBall) / coordsBox.w * 10)
      }

      moveAt(e)

      document.onmousemove = function(e) {
        moveAt(e)
      }

      ball.onmouseup = function() {
        document.onmousemove = null
        ball.onmouseup = null
      }

      ball.ondragstart = function() {
        return false
      }
    },
    submit() {
      let id = this.$store.state.discussion.thesisId
      PatchtThesisVotes(id, {
        x: this.x,
        y: this.y
      }).then((r) => {
        this.$store.commit('discussion/updateArgumentThesis', {
          argument_id: this.$store.state.discussion.argument_id,
          thesis_id: id,
          mean_x: r.data.mean_x,
          mean_y: r.data.mean_y,
          x: this.x,
          y: this.y
        })
        GetArguments(this.$store.state.discussion.argument_id).then(res => {
          this.$store.commit('discussion/replaceDiscussionArgument', {
            id: this.$store.state.discussion.argument_id,
            opinion_ratio: res.data.opinion_ratio
          })
        })
        GetCurrentDiscussions(this.$route.params.id).then(res => {
          this.$store.commit('discussion/setCurrentDiscussion', res.data)
        })
        this.$store.commit('modal/closeAllModal')
      })
    }
  }
}
</script>

<style scoped>
  .schedule_block_c {
    margin: 0;
    left: 44%;
    top: 43%;
  }
</style>
