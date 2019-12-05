<template>
  <div class="center">
    <section class="section-rewards">
      <div class="h2"><h1>{{$lang.profile.rewardTitle}}</h1></div>
      <div class="rewards">
        <rewardItem
          class="active"
          v-for="(reward, i) in profile_rewards" :key="`reward_${i}`"
          :data="reward"
          />
      </div>
    </section>
  </div>
</template>

<script>
import rewardItem from './rewardItem'
import { mapState, mapActions } from 'vuex'

export default {
  components: {
    rewardItem
  },

  computed: {
    ...mapState('auth', ['auth']),
    ...mapState('profile', ['profile_rewards']),
  },

  methods: {
    ...mapActions('profile', ['getUserRewards'])
  },

  mouted () {
    this.getUserRewards(this.auth.id)
  },

  name: 'Rewards'
}
</script>

<style scoped>

</style>
