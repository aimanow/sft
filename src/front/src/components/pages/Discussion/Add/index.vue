<template>
  <div class="center">
    <section class="section_task">
      <div class="h2"><h1>{{$lang.descAdd.title}}</h1></div>
      <div class="edu_block_content">
        <a href="#" class="btn btn-bord-red c_link" @click="cansel">{{$lang.descAdd.cancel}}</a>
        <v-card elevation="5">
          <v-card-text>
            <div class="edu_block current">
              <div class="edu_number">
                <div class="circle active">
                  1
                </div>
              </div>
              <div class="w_v">
                <div class="w_thesis_title">{{$lang.descAdd.themeTitle}}</div>
                <div class="w_v_inp">
                  <input type="text" class="t-inp" v-model="newDiscussionForm.title" :placeholder="$lang.descAdd.themeTitle"
                         @change="nextStep(2)"/>
                </div>
              </div>
              <div class="edu-inp-wrap">
                <div class="w_thesis_title">{{$lang.descAdd.addImage}}:</div>
                <div class="edu-inp-cont" style="text-align: center;">
                  <input v-show="false" ref="discussionImageUpload" type="file" @change="addDiscussionImage"/>
                  <v-btn icon large color="#0560ce" dark @click.prevent="$refs.discussionImageUpload.click()">
                    <v-icon>link</v-icon>
                  </v-btn>
                </div>
              </div>
            </div>
          </v-card-text>
        </v-card>
        <v-card>
          <v-card-text>
            <div class="edu_block">
              <div class="edu_number">
                <div class="circle" :class="{active: step_2}">
                  2
                </div>
              </div>
              <div class="edu_block_wrap pt-0">
                <div class="w_asp country_wr">
                  <div v-if="allAspects.length" class="w_thesis_title">{{$lang.descAdd.select}}</div>
                  <div class="aspect aspect-check">
                    <Item
                      v-for="(item) in allAspects" :count="aspectsCount"
                      :key="item.id"
                      :item="item" @checkedAspect="checkedAspect" @checkOffAspect="checkOffAspect"
                    />
                    <!-- <div class="aspect_item aspect_item_plus">
                      <a href="#" @click.prevent="addModal({name: 'DiscussionAddAspects'})">
                        <div class="aspect_item_add"><span class="icon-plus"></span><span>{{$lang.descAdd.add}}</span></div>
                      </a>
                    </div> -->
                  </div>
                  <div class="w_v">
                    <div class="w_thesis_title">{{$lang.descAdd.searchAspects}}</div>
                    <div class="w_v_inp ">
                      <input type="text" class="t-inp col-3-4 pb-30" v-model="searchAspects" :placeholder="$lang.descAdd.nameAspects"/>
                      <v-btn large color="#0560ce" dark class="col-1-5 ma-0" @click="submitSearchAspects(searchAspects)">
                        <v-icon>search</v-icon>
                      </v-btn>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </v-card-text>
        </v-card>
        <v-card>
          <v-card-text>
            <div class="edu_block">
              <div class="edu_number">
                <div class="circle" :class="{active: step_3}">
                  3
                </div>
              </div>
              <div class="edu_block_wrap">
                <div class="w_thesis">
                  <div class="w_thesis_title">{{$lang.descAdd.arg}}</div>
                  <div class="w_v_inp">
                    <input class=" t-inp" v-model="form.argument" :placeholder="$lang.descAdd.arg"/>
                  </div>
                </div>
                <div class="w_thesis">
                  <div class="w_thesis_title">{{$lang.descAdd.theses}}</div>
                  <textarea v-model="form.thesis" :placeholder="$lang.descAdd.theses"></textarea>
                </div>
                <div class="w_thesis_linksblock">
                  <input type="file" style="display: none;" ref="files" multiple="multiple" name="files" @change="selectFiles">
                  <div class="w_thesis_linksblock_ls">
                    <a href="#" class="plus_link" @click.prevent="addFiles()" title="Add files"><span class="icon-plus"></span></a>
                    <a href="#" class="sh_link" @click.prevent="addLink()" title="Add links"><span class="icon-link2"></span></a>
                  </div>
                  <div class="w_thesis_title" v-show="form.links.length">{{$lang.descAdd.links}}</div>
                  <div class="w_thesis_link_cont">
                    <div
                      class="w_thesis_link_line"
                      v-for="(link, index) in form.links"
                      :key="index"
                    >
                      <input type="text" class="t-inp" :value="link" readonly/>
                      <a href="#" class="w-close-link" @click.prevent="removeLink(index)"><span class="icon-cab7"></span></a>
                    </div>
                  </div>
                  <div class="w_thesis_title" v-show="form.files.length">Files:</div>
                  <div class="w_thesis_files">
                    <div class="w_thesis_files_file" v-for="(file, index) in form.files" :key="`file_${index}`">
                      <span class="icon-doc1"></span>
                      <a href="#" class="w-close-link" @click.prevent="removeFile(`file_${index}`)"><span class="icon-cab7"></span></a>
                      <span class="w_thesis_txt">{{ file.name }}</span>
                    </div>
                  </div>
                </div>
                <div class="win_pos">
                  <div class="w_thesis_title">{{$lang.descAdd.position}}</div>
                  <div class="w_pos_links">
                    <a href="#" :class="{'active': form.position == true}" @click.prevent="form.position = true"
                       class="w_pos_links_link w_pos_links_link1">{{$lang.descAdd.yes}}</a>
                    <a href="#" :class="{'active': form.position == false}" @click.prevent="form.position = false"
                       class="w_pos_links_link w_pos_links_link2">{{$lang.descAdd.no}}</a>
                  </div>
                </div>
                <div class="text-xs-center text-md-left mt-4">
                  <input @click.prevent="sendForm" type="submit" class="btn btn-bot" :value="$lang.descAdd.publish"/>
                </div>
              </div>
            </div>
          </v-card-text>
        </v-card>
      </div>
    </section>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import Item from './Item'
import { GetAspects, PutDiscussionImage, PostDiscussionArgements, AddThesisFile, AddThesisLink } from '@/api'

export default {
  name: 'Discussion',
  data() {
    return {
      newDiscussionForm: {
        title: '',
        lang: ''
      },
      responseDiscussion: null,
      discussionPoster: null,
      searchAspects: '',
      form: {
        thesis: '',
        argument: '',
        position: null,
        links: [],
        files: []
      },
      aspect_ids: [],
      aspectsCount: 0,
      arrayAspects: [],
      step_2: false,
      step_3: false
    }
  },

  components: { Item },

  beforeRouteLeave(to, from, next) {
    this.$store.commit('discussion/toggleDiscussionButton', true)
    next()
  },

  computed: {
    ...mapState('auth', ['auth']),
    ...mapState('discussion', ['discussion_aspects']),
    allAspects() {
      let disc_asp = this.discussion_aspects
      let arrayAspects = this.arrayAspects
      return disc_asp.concat(arrayAspects)
    },

  },
  methods: {
    ...mapActions('modal', ['addModal']),
    ...mapActions('discussion', ['createNewDiscussion']),
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
    cansel() {
      this.$router.go(-1)
    },
    addDiscussionImage(e) {
      let img = e.target.files[0]
      let form = new FormData()
      form.append('image', img)
      this.discussionPoster = form
    },
    sendForm() {
      if (this.newDiscussionForm.title.length < 10) {
        this.$store.commit('openDialog', 'Please sign title discussion at least 10 characters long')
        return false
      }
      if (this.aspectsCount === 0) {
        this.$store.commit('openDialog', 'Please check Aspects \'Only maximum three aspects can be chosen\'')
        return false
      }
      if (this.form.position === null) {
        this.$store.commit('openDialog', 'Please check Yes or No')
        return false
      }
      if (this.form.thesis.length < 10 && this.form.argument.length < 10) {
        this.$store.commit('openDialog', 'Please check filds thesis and arguments the filds must have at least 10 characters long')
        return false
      }
      this.newDiscussionForm.lang = this.$lang.current_lang
      this.createNewDiscussion(this.newDiscussionForm)
        .then(res => {
          this.responseDiscussion = res.data
          return res.data.id
        }).then(id => {
          if (this.discussionPoster) {
            PutDiscussionImage({ id, image: this.discussionPoster })
          }
          let form = {
            'title': this.form.argument,
            'aspect_ids': this.aspect_ids,
            'thesis': {
              'position': this.form.position,
              'message': this.form.thesis
            }
          }
          PostDiscussionArgements({ id, form }).then(res => {
            const thesisId = res.data.thesis.id
            if (this.form.files.length) AddThesisFile({ id: thesisId, file: this.form.files })
            if (this.form.links.length) AddThesisLink({ id: thesisId, link: this.form.links })
            return id
          })
            .then(id => this.$router.push('/discussion/' + id))
        })
    },
    submitSearchAspects(query) {
      GetAspects(query).then(res => {
        this.arrayAspects = res.data.items
      })
    },
    removeLink(index) {
      this.form.links.splice(index, 1)
    },
    nextStep(val) {
      if (val == 2 && this.newDiscussionForm.title.length >= 3) this.step_2 = true
      if (val == 3) this.step_3 = true
    },
    addLink() {
      let link = prompt('Enter link')
      if (link.length > 0) {
        this.form.links.push(link)
      }
    },
    addFiles() {
      this.$refs.files.click()
    },
    removeFile(key) {
      this.form.files.splice(key, 1)
    },
    selectFiles(e) {
      if (this.form.files.length <= 1 && e.target.files.length == 1) {
        this.form.files.push(e.target.files[0])

      } else {
        let files = e.target.files
        let filesArray = []
        for (let i = 0; i < files.length; i++) {
          filesArray[i] = files.item(i)
        }
        if (filesArray.length > 2) {
          alert('Max 2 files')
          this.form.files = filesArray.splice(1)
        } else {
          this.form.files = filesArray
        }
      }

    },
    setActiveAspect(index) {
      this.index_active_aspect = index
      this.form.aspect = this.favorite_aspects[index]
    }
  },
  watch: {
    index_active_aspect: function(val) {
      if (typeof val === 'number') this.nextStep(3)
    },
    aspectsCount(num) {
      if (num > 3) {
        this.$store.commit('openDialog', 'Only maximum three aspects can be chosen')
      }
    }
  }
}
</script>

<style scoped lang="scss">
  .t-inp {
    height: 45px;
    line-height: 1.1;
  }

  .pb-30 {
    padding-bottom: 30px !important;
  }

  .w_v_inp {
    margin-bottom: 20px;
  }

  .h2 {
    margin-bottom: 50px;
  }

  .circle {
    position: absolute;
    display: inline-block;
    width: 75px;
    height: 75px;
    background-color: #EDECEC;
    border-radius: 100%;
    margin-top: -50px;
    font-size: 42px;
    color: white;
    border: 10px solid white;
    font-weight: bold;
    left: 50%;
    top: -45px;
    transform: translateX(-50%);
    text-align: center;
    box-shadow: 0px 0px 0px 0px rgba(0, 0, 0, 0), 0px 0px 0px 0px rgba(0, 0, 0, 0), 0px -2px 2px 0px rgba(0, 0, 0, 0.12);

    &.active {
      background: linear-gradient(45deg, rgba(5, 96, 206, 1) 0%, rgba(2, 156, 231, 1) 100%);
    }
  }

  .col- {
    &1-5 {
      width: 20%;
      float: right;
    }

    &3-4 {
      width: 75%;
      display: inline-block;
    }
  }

  .edu_number {
    position: relative;
  }

  .v-card {
    margin-bottom: 60px;
  }

  .v-card__text {
    padding: 60px 30px;
  }

  .w_pos_links_link1 {
    &.active, &:hover {
      background: linear-gradient(45deg, rgba(5, 96, 206, 1) 0%, rgba(2, 156, 231, 1) 100%);
      color: white;
    }
  }

  .w_pos_links_link2 {
    &.active, &:hover {
      background: linear-gradient(45deg, rgba(227, 20, 10, 1) 0%, rgba(236, 63, 81, 1) 100%);
      color: white;
    }
  }
</style>
