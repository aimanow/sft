<template>
  <div class="win win-argument" id="win-argument">
    <div class="win_cont">
      <CreateDiscPost :id="id" v-if="id" thesis/>
      <CreateDiscPost v-else/>
      <a href="#" class="win_close" @click.prevent="closeAllModal()"><span class="icon-cab7"></span></a>
    </div>
  </div>
</template>

<script>
import CreateDiscPost from './CreateDiscPost'
import {mapMutations} from 'vuex'
export default {
  name: 'ModalArgument',
  props:['id'],
  components:{CreateDiscPost},
  methods: {
    ...mapMutations('modal', ['closeAllModal']),
  }
}
</script>
