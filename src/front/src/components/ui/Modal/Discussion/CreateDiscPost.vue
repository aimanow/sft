<template>
  <div class="edu_block_wrap">
    <div v-if="!thesis" style="margin-bottom: 16px">
      <div class="w_thesis_title">{{$lang.descAdd.aspects}}</div>
      <div class="spinner" v-if="slickComp==null">
        <div class="bounce1"></div>
        <div class="bounce2"></div>
        <div class="bounce3"></div>
      </div>
      <component
        :is="slickComp" ref="slick" :options="SlickOptions" class="text-xs-center">
        <aspectItem
          v-for="item in all_aspects" :count="aspectsCount"
          :key="item.id"
          :item="item" @checkedAspect="checkedAspect" @checkOffAspect="checkOffAspect" :small="true"
        />
      </component>
      <!-- <div class="aspect_item aspect_item_plus">
        <a href="#" @click.prevent="addModal({name: 'DiscussionAddAspects', data: 'openModalArgument'})">
          <div class="aspect_item_add">
            <span class="icon-plus"></span>
            <span>Add</span>
          </div>
        </a>
      </div> -->
    </div>
    <div class="w_thesis" v-if="!thesis">
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
    <div class="text-xs-center text-md-left mt-4"><input @click.prevent="sendForm" type="submit" class="btn btn-bot"
                                                         :value="$lang.descAdd.publish"/></div>
  </div>
</template>

<script>
//import aspectItem from './aspectItem' './Item'
import aspectItem from '@/components/pages/Discussion/Add/Item'
import {mapMutations, mapState, mapActions} from 'vuex'
import {PostDiscussionArgements, PostDiscussionThesis, AddThesisFile, AddThesisLink, GetAspects, GetAllAspects} from '@/api'
// import Slick from 'vue-slick'

export default {
  name: 'Argument',
  components: {
    aspectItem,
    Slick: () => import('vue-slick')
  },
  props: {
    thesis: Boolean,
    id: null
  },
  mounted() {

  },
  data() {
    return {
      slickComp: null,
      form: {
        thesis: '',
        argument: '',
        position: null,
        links: [],
        files: []
      },
      aspect_ids: [],
      aspectsCount: 0,
      localAspects: [],
      allAspects: [],
      SlickOptions: {
        infinity: true,
        dots: true,
        slidesToShow: 5,
        slidesToScroll: 5,
        prevArrow: '<button class="slick-prev slick-arrow"><span class="icon-arrow"></span></button>',
        nextArrow: '<button class="slick-next slick-arrow"><span class="icon-arrow"></span></button>',
        responsive: [
          {
            breakpoint: 600,
            settings: {
              slidesToShow: 3,
              slidesToScroll: 3
            }
          },
        ]
      },


    }
  },

  computed: {
    ...mapState('auth', ['auth']),
    ...mapState('discussion', ['current_discussion', 'discussion_aspects']),
    //...mapState('profile', ['all_aspects']),
    all_aspects() {
      // return this.localAspects.concat(this.discussion_aspects)
      // return this.localAspects
      return this.allAspects
    },
    // favorite_aspects(){
    //   let arr =[];
    //   if(this.all_aspects.length){
    //     arr = this.all_aspects;
    //     return arr.filter(aspect=>{ return aspect.is_favorite === true})
    //   }else{
    //     arr = this.localAspects;
    //     return arr.filter(aspect=>{ return aspect.is_favorite === true})
    //   }
    //
    // }
  },

  methods: {
    ...mapMutations('modal', ['closeAllModal']),
    ...mapMutations('discussion', ['pushDiscussionArgument', 'pushDiscussionThesis', 'updateArgumentThesis', 'addCurrentDiscussionAspects']),
    ...mapActions('discussion', ['addDiscussionArguments']),
    ...mapActions('modal', ['addModal']),
    // addAspectId(id){
    //   this.aspect_ids.push(id)
    // },
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
    sendForm() {
      let form = {
        'title': this.form.argument,
        'aspect_ids': this.aspect_ids,
        'thesis': {
          'position': this.form.position,
          'message': this.form.thesis
        }
      }
      if (this.thesis) {
        if (this.form.thesis.length < 10) {
          this.$store.commit('openDialog', this.$lang.descAdd.errorMinThesis)
          return false
        }
        if (this.form.thesis.length > 1000) {
          this.$store.commit('openDialog', this.$lang.descAdd.errorMaxThesis)
          return false
        }

        PostDiscussionThesis({id: this.id, form: {position: this.form.position, message: this.form.thesis}})
          .then(res => {
            let myThesis = res.data
            if (this.form.files.length) {
              AddThesisFile({id: myThesis.id, file: this.form.files}).then((response) => {
                this.updateArgumentThesis({
                  argument_id: this.id,
                  thesis_id: myThesis.id,
                  attachments: response.data.attachments
                })
              })
            }
            if (this.form.links.length) {
              AddThesisLink({id: myThesis.id, link: this.form.links}).then((response) => {
                this.updateArgumentThesis({
                  argument_id: this.id,
                  thesis_id: myThesis.id,
                  attachments: response.data.attachments
                })
              })
            }
            this.pushDiscussionThesis({thesis: myThesis, id: this.id})
            this.closeAllModal()
          })
      } else {
        if (this.form.thesis.length < 10 || this.form.argument.length < 10) {
          this.$store.commit('openDialog', this.$lang.descAdd.errorMinThesisArgument)
          return false
        }
        if (this.form.argument.argument > 100) {
          this.$store.commit('openDialog', this.$lang.descAdd.errorMaxArgument)
          return false
        }
        if (this.form.thesis.length > 1000) {
          this.$store.commit('openDialog', this.$lang.descAdd.errorMaxThesis)
          return false
        }
        if (this.aspectsCount === 0) {
          this.$store.commit('openDialog', this.$lang.descAdd.errorChooseAspects)
          return false
        }
        if (this.form.position === null) {
          this.$store.commit('openDialog', this.$lang.descAdd.errorYesNo)
          return false
        }

        PostDiscussionArgements({id: this.$route.params.id, form}).then((res) => {
          let myArg = res.data
          if (this.form.files.length) {
            AddThesisFile({id: myArg.thesis.id, file: this.form.files})
          }
          if (this.form.links.length) {
            AddThesisLink({id: myArg.thesis.id, link: this.form.links})
          }
          this.pushDiscussionArgument(myArg)
          this.addCurrentDiscussionAspects({aspects: myArg.aspects})

          this.closeAllModal()
        })
      }
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
    removeLink(index) {
      this.form.links.splice(index, 1)
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

  },

  created() {
    this.localAspects = this.current_discussion.aspects
    // this.localAspects.forEach((a) => {
    //   this.allAspects.push(a)
    // })


    GetAllAspects().then(res => {
      res.data.items.forEach((a) => {
        // if (this.allAspects.findIndex(as => as.id === a.id) < 0) {
        //   this.allAspects.push(a)
        //   console.log(a)
        // }
        this.allAspects.push(a)
      })
      this.$nextTick(function () {
        this.slickComp = 'Slick'
      })
      // this.loadingAspects = false
    })
  }
}
</script>

<style scoped lang='scss'>
  .aspect_item {
    float: none;
    display: inline-block;
  }

  .btn-holder {
    display: block;
    position: absolute;
    width: 140px;
    height: 34px;
    left: 50%;
    transform: translateX(-50%);
  }

  .btn-holder:before {
    content: '';
    display: block;
    width: calc(100% + 18px);
    height: 45px;
    border: 11px solid #fff;
    border-radius: 43px;
    margin-left: -8.5px;
    margin-top: -3px;
  }

  .btn-holder .btn-bot {
    bottom: 0;
    width: 100%;
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

  .spinner {
    margin: 100px auto 0;
    width: 70px;
    text-align: center;
    margin-top: -2px;
  }

  .spinner > div {
    width: 18px;
    height: 18px;
    background-color: #CFD9E4;

    border-radius: 100%;
    display: inline-block;
    -webkit-animation: sk-bouncedelay 1.4s infinite ease-in-out both;
    animation: sk-bouncedelay 1.4s infinite ease-in-out both;
  }

  .spinner .bounce1 {
    -webkit-animation-delay: -0.32s;
    animation-delay: -0.32s;
  }

  .spinner .bounce2 {
    -webkit-animation-delay: -0.16s;
    animation-delay: -0.16s;
  }

  @-webkit-keyframes sk-bouncedelay {
    0%, 80%, 100% {
      -webkit-transform: scale(0)
    }
    40% {
      -webkit-transform: scale(1.0)
    }
  }

  @keyframes sk-bouncedelay {
    0%, 80%, 100% {
      -webkit-transform: scale(0);
      transform: scale(0);
    }
    40% {
      -webkit-transform: scale(1.0);
      transform: scale(1.0);
    }
  }
</style>
