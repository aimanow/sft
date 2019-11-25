<template>
  <div @click="addModal({name: 'RewardsInfo', data: this.data })" class="rewards_item">
    <div class="rewards_item_ico"><img :src="data.image" alt=""/></div>
    <div class="rewards_item_name">{{ data.title }}</div>
    <a href="#" class="cover_link"></a>
  </div>
</template>

<script>
import {mapActions} from 'vuex'
export default {
  name: 'Reward',
  props: ['data'],
  methods: {
    ...mapActions('modal', ['addModal']),
  }
}
</script>

<style scoped>

</style>
