<template>
  <div class="authors">
    <v-container grid-list-lg class="pa-0">
      <v-layout row wrap >
          <v-flex xs6 sm3 md4  v-for="author in favoritesAuthors" :key="author.id">
            <UserItem fav :author="author" @deleteFavorites="deleteFavorites"/>
          </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import UserItem from '@/components/pages/Main/UserItem'
export default {
  name: 'Authors',
  computed: {
    ...mapState('auth', ['auth']),
    ...mapState('profile', ['favoritesAuthors'])
  },
  components:{UserItem},
  methods: {
  ...mapActions('profile', ['getFavoritesDiscussionAuthors', 'toggleDiscusionAuthorFav']),
    deleteFavorites (id) {
      this.toggleDiscusionAuthorFav(id).then((res) =>{
        this.$emit('removeAuthor', id)
        this.$store.commit('profile/removeFavoritesDiscussionAuthors', res.id)
      })
    }
  },
  created(){
    if (this.favoritesAuthors.length == 0) { this.getFavoritesDiscussionAuthors(1) }
  },


}
</script>

<style>

</style>
