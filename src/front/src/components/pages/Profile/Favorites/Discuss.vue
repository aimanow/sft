<template>
    <div>
      <div class="filter_wrap">
        <div class="filter">
          <div class="filter_search">
            <form @submit.prevent="">
              <button type="submit" class="search-btn">
                <span class="icon-search"></span>
              </button>
              <input v-model.trim="filter.q"
                     type="text" class="t-inp search-t-inp"
                     placeholder="Введите название темы дискуссии"/>
            </form>
          </div>

          <a href="#"
             class="filter_link btn btn-bord-blue"
             @click.prevent="isOpenFilter = !isOpenFilter">
            <span class="icon-filter"></span> Фильтр
          </a>

        </div>

        <div class="filter_block" v-show="isOpenFilter">
          <div class="filter_block_top">

            <div class="filter_block_res_title">{{$lang.filter.points}}:</div>

            <div class="filter_block_rads rads">

              <div class="rads_item">
                <label class="radio">
                  <input type="checkbox" v-model="filter.by_date">
                  <span class="radio_text">{{$lang.filter.byDate}} <img src="@/assets/svg/arrs.svg" alt=""/></span>
                </label>
              </div>

              <div class="rads_item">
                <label class="radio">
                  <input type="radio" v-model="filter.lang" value="ru">
                  <span class="radio_text">Рус</span>
                </label>
              </div>

              <div class="rads_item">
                <label class="radio">
                  <input type="radio" v-model="filter.lang" value="en">
                  <span class="radio_text">Eng</span>
                </label>
              </div>

              <div class="rads_item">
                <label class="radio">
                  <input type="radio" v-model="filter.lang" value="de">
                  <span class="radio_text">Deu</span>
                </label>
              </div>

              <div class="rads_item">
                <label class="radio">
                  <input type="checkbox" v-model="filter.by_score">
                  <span class="radio_text">{{$lang.filter.byPop}}</span>
                </label>
              </div>

            </div>
          </div>

          <div class="filter_block_res">
            <div class="filter_block_res_title">{{$lang.filter.byAspects}}:</div>
            <div class="aspect aspect-check aspect-gr">

              <div class="aspect_item"
                   v-for="aspect in []" :key="aspect.id"
                   @click.prevent="selectAspect(aspect.id)"
                   :class="{'active': filter.aspect.includes(aspect.id)}">

                <div class="aspect_item_img">

                  <div class="aspect_item_bg js-bg">
                    <img :src="aspect.image" :alt="aspect.title"/>
                  </div>

                  <div class="aspect_item_text">
                    <span class="icon-check"></span>
                    <p>{{aspect.title}}</p>
                  </div>

                </div>
              </div>

            </div>
          </div>

        </div>
      </div>

      <div class="disc disc-fav">
        <discussionItem @remove="remove"
          v-for="discussion in favoritesDiscussions"
          :discussion="discussion"
          :key="discussion.id"/>
        <!-- <div class="div-date"><span>2017</span></div> -->
      </div>
    </div>
</template>

<script>
import { mapActions, mapState} from 'vuex'
import DiscussionItem from './DiscussionItem'
export default {
  name: 'Discuss',

  components: { DiscussionItem},

  data () {
    return {
      isOpenFilter: false,
      filter: {
        by_date: true,
        by_score: false,
        lang: 'ru',
        aspect: [],
        q: ''
      },

    }
  },

  computed: {
    ...mapState('auth', ['auth']),
    ...mapState('profile', ['favoritesDiscussions'])
  },

  methods: {
    ...mapActions('profile', ['getFavoritesDiscussion']),
    remove(id){
      this.$emit('removeDisc', id)
    }
  },

  created () {
    if (this.favoritesDiscussions.length == 0) { this.getFavoritesDiscussion(1) }
  },
}
</script>

<style scoped>

  .filter_block {
    display: block;
  }

  .aspect_item {
    cursor: pointer;
  }

  .radio {
    cursor: pointer;
  }

</style>
