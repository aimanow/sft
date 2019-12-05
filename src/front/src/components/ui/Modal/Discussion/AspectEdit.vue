<template>
  <div class="win win-ed win-aspect-edit" id="win-aspect-edit">
    <div class="win_cont" style="padding-top: 34px;">
      <div class="pt-0">
        <div class="w_asp country_wr">
          <div class="w_thesis_title">{{$lang.descAdd.select}}</div>
          <div class="w_v">
            <div class="w_v_inp " style="display: flex">
              <input type="text" class="t-inp col-3-4 pb-30" style="text-align: left; margin-right: 10px;" v-model="searchAspects"
                     :placeholder="$lang.descAdd.nameAspects"/>
              <v-btn color="#0560ce" dark class="col-1-5 ma-0" style="border-radius: 8px;" @click="submitSearchAspects(searchAspects)">
                <v-icon>search</v-icon>
              </v-btn>
            </div>
          </div>
          <div class="aspect aspect-check" style="margin-bottom: 30px; margin-top: 10px;">
            <div class="w_thesis_title" style="margin-top: 40px;" v-if="loadingAspects">{{$lang.descAdd.loadingAspects}}</div>
            <Item
              v-for="(item) in allAspects" :count="aspectsCount"
              :key="item.id"
              :item="item" @checkedAspect="checkedAspect" @checkOffAspect="checkOffAspect"
            />
          </div>
        </div>
      </div>

      <div style="position: absolute; bottom: 10px; right: 14px;">
        <div>
          <a href="#" class="btn" @click.prevent="submit">{{$lang.descAdd.graphCommit}}</a>
        </div>
      </div>
    </div>
    <a href="#" class="win_close" @click.prevent="closeAllModal"><span class="icon-cab7"></span></a>
  </div>
</template>

<script>
import {GetAspects, EditDiscussion} from '@/api'
import {mapMutations} from 'vuex'
import Item from './../../../pages/Discussion/Add/Item'

export default {
  name: 'AspectEdit',
  components: {
    Item
  },
  data() {
    return {
      aspects: [],
      allAspects: [],
      aspect_ids: [],
      aspectsCount: 0,
      loadingAspects: true,
      searchAspects: '',
    }
  },
  created() {
    this.loadingAspects = true
    this.$store.state.discussion.current_discussion.aspects.forEach((a) => {
      this.aspect_ids.push(a.id)
    })
    this.aspectsCount = this.aspect_ids.length
    this.submitSearchAspects()
  },
  computed: {},
  methods: {
    ...mapMutations('modal', ['closeAllModal']),
    ...mapMutations('discussion', ['changeCurrentDiscussionAspects']),
    submit() {
      EditDiscussion({
        id: this.$store.state.discussion.current_discussion.id,
        form: {
          aspects: this.aspect_ids,
          argument_id: this.$store.state.discussion.discussion_arguments[0].id
        }
      }).then((r) => {
        console.log(r)
        this.changeCurrentDiscussionAspects({aspects: r.aspects})
        this.closeAllModal()
      })
    },
    checkedAspect(id) {
      this.aspectsCount = this.aspectsCount + 1
      this.aspect_ids.push(id)
    },
    checkOffAspect(id) {
      this.aspectsCount = this.aspectsCount - 1
      this.aspect_ids.find((item, index) => {
        if (item == id) this.aspect_ids.splice(index, 1)
      })
    },
    submitSearchAspects(query = '') {
      GetAspects(query).then(res => {
        res.data.items.forEach((a) => {
          if (this.aspect_ids.indexOf(a.id) > -1) {
            a.active = true
          }
        })
        this.allAspects = res.data.items
        this.loadingAspects = false
      })
    },
  }
}
</script>

<style scoped>
  .win-aspect-edit {
    min-height: 300px;
    max-width: 584px;
  }
</style>
