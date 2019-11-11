<template>
    <div class="disc_line">
        <div class="disc_line_img">
          <img  v-if="discussion.image_url" :src="$baseUrl + discussion.image_url" :alt="discussion.title"/>
        </div>
        <div class="disc_line_cont">
            <div class="disc_line_inf">
                <div class="disc_line_name"><a href="#">{{discussion.title}}</a>
                </div>
                <div class="disc_line_athor"><span>Автор:</span> {{discussion.author.fullname}}</div>
                <div class="disc_line_date">{{discussion.created_at}}</div>
            </div>
            <div class="truefalse"><span>{{discussion.votes.true}}%</span><span>{{discussion.votes.false}}%</span></div>
            <a href="#" class="fav_link active"
               @click.prevent="deleteDiscussion">
              <span class="icon-fav2"></span>
            </a>
        </div>
    </div>
</template>
<script>
import { mapActions, mapState } from 'vuex'
export default {
  name: 'discussionItem',
  props: ['discussion'],
  computed: {
    ...mapState('auth', ['auth']),
  },
  methods: {
    ...mapActions('profile', ['deleteFavoritesDiscussion']),
    deleteDiscussion () {
      this.$emit('remove', this.discussion.id)
      this.deleteFavoritesDiscussion(this.discussion.id)
    }
  }
}

</script>
