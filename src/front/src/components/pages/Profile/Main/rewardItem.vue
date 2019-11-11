<template>
  <div @click="addModal({name: 'RewardsInfo', data: {title: info.title}})" class="rewards_item active">
    <div class="rewards_item_ico"><img src="@/assets/svg/i1.svg" alt=""/></div>
    <div class="rewards_item_name">{{info.title}}</div>
    <a href="#" class="cover_link"></a>
  </div>
</template>

<script>
  import {mapActions} from 'vuex'
  export default {
    name: "Header",
    props: ['info'],
    methods: {
      ...mapActions('modal', ['addModal']),
    }
  }
</script>

<style scoped>

</style>
