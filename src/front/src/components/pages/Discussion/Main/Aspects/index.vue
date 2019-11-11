<template>
  <div class="country_wr">
    <div class="country_title">{{$lang.descAdd.select}}</div>
    <div class="aspect aspect-check">
      <Item v-for="item in aspects" :key="item.title" :item="item"/>
    </div>
  </div>
</template>

<script>
import Item from './Item'
export default {
  name: "Aspects",

  components: { Item },
  methods: {

  },
  props: ['aspects'],
}
</script>

<style scoped>

</style>
