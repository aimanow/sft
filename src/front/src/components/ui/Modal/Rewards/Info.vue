<template>
  <div class="win win-reward" id="win-reward">
    <div class="win_cont">
      <div class="rewards_item_window active">
        <div class="rewards_item_ico active"><img :src="modal.data.image" alt=""/></div>
        <div class="rewards_item_name">{{modal.data.title}}</div>
        <div class="rewards_item_inf">{{ modal.data.description }}</div>
        <div class="rewards_item_date">
          <span>Награда была получена:</span>{{ modal.data.date }}
        </div>
      </div>
    </div>
    <a href="#" @click.prevent="closeAllModal" class="win_close"><span class="icon-cab7"></span></a>
  </div>
</template>

<script>
import { mapMutations } from 'vuex'
export default {
  name: 'rewardInfo',
  props: ['modal'],
  methods:{
    ...mapMutations('modal', ['closeAllModal']),
  }
}
</script>

<style scoped>

</style>
