<template>
  <div class="center">
    <section class="section-form" v-if="profile">
      <div class="h2 m-hid"><h1>{{ profile.fullname }}</h1></div>
      <div class="card">
        <div class="card_img"><img :src="profile.avatar" alt=""/></div>
        <div class="card_cont">
          <div class="card_verif"><span class="icon-check" v-if="profile.education.verification"></span>{{ $lang.profile[profile.education.verification ? 'confirm' : 'notConfirm'] }}</div>
          <table class="card_info">
            <tr><th>{{$lang.profile.country}}:</th><td>{{ profile.education.country || $lang.profile.empty }}</td></tr>
            <tr><th>{{$lang.profile.city}}:</th><td>{{ profile.education.city || $lang.profile.empty }}</td></tr>
            <tr><th>{{$lang.profile.uni}}:</th><td>{{ profile.education.hight_school || $lang.profile.empty }}</td></tr>
            <tr><th>{{$lang.profile.date}}:</th><td>{{ profile.education.date || $lang.profile.empty }}</td></tr>
            <tr><th>{{$lang.profile.fuc}}:</th><td>{{ profile.education.faculty || $lang.profile.empty }}</td></tr>
            <tr><th>{{$lang.profile.spec}}:</th><td>{{ profile.education.specialty || $lang.profile.empty }}</td></tr>
          </table>
        </div>
      </div>

      <div class="card_title" v-if="profile_rewards.length"><span class="icon-cab4"></span>{{$lang.profile.achive}}</div>
      <div class="rewards scroll" v-if="profile_rewards.length">
        <div class="scroll_in">
          <div
            v-for="(reward, index) in profile_rewards" :key="`reward_${index}`"
            @click.prevent="addModal({name: 'RewardsInfo', data: reward })"
            class="rewards_item">
            <div class="rewards_item_ico"><img :src="reward.image" alt=""/></div>
            <div class="rewards_item_name">{{ reward.title }}</div>
            <a href="#" class="cover_link"></a>
          </div>
        </div>
      </div>

      <div class="card_title" v-if="profile_knowledge.length"><span class="icon-cab5"></span>{{$lang.profile.edu}}</div>
      <div class="fields" v-if="profile_knowledge.length">
        <div class="fields_col" v-for="(item, index) in profile_knowledge" :key="index">
          <div class="fields_item" style="margin: 0; left: 0; right: 0; top: 0; bottom: 0;">
            <div class="fields_item_num" style="left: 94%; top: 39%;">{{ item.score }}</div>
            <div class="fields_item_img"><img :src="item.knowledge.image" alt=""/></div>
            <div class="fields_item_txt">
              <span :class="{ 'icon-check': item.score > 0 }"></span>
              <p>{{ item.knowledge.title }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
  name: 'Profile',
  methods: {
    ...mapActions('profile', ['getUserProfile', 'getUserRewards', 'getUserKnowledges']),
    ...mapActions('modal', ['addModal']),
  },

  mounted () {
    let requests = [
      this.getUserProfile(this.id),
      //this.getUserRewards(this.id),
      //this.getUserKnowledges(this.id)
    ]

    Promise.all(requests)
      .then(() => {

      })
  },

  computed: {
    ...mapState('profile', ['profile', 'profile_rewards', 'profile_knowledge']),

    id() {
      return this.$route.params.id
    }
  },
}
</script>

<style scoped>

</style>
