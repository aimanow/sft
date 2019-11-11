<template>
  <div class="center">
    <section class="section-form">
    <div class="h2 m-hid"><h1>{{ $lang.profile.knowTitle }}</h1></div>
      <div class="fields-vis" style="height: 750px;">
        <div class="fields_center">
          <div class="fields_center_circ">
            <div class="fields_center_ava"><img v-if="profile.avatar_url" :src="$baseUrl+profile.avatar_url" alt="foto"></div>
          </div>
          <div class="fields_center_name">{{  profile.fullname  }}</div>
          <router-link to="/profile/areas-of-knowledge/edit" class="btn btn-bord-blue">{{$lang.profile.edit}}</router-link>
        </div>

        <div class="fields">

          <div class="fields_col" v-for="(item, index) in profile_knowledge" :key="item.id">
            <div class="fields_item" :class="['fields_item'+(index+1)]">
              <circle-slider
                class="slider-circle__item"
                v-model="item.score"
                :text="item.knowledge.title"
                :urlImg="item.knowledge.image"
                :side="180"
                :min="0"
                :max="20"
                disabled
                :step-size="1"
                :circle-width="10"
                circle-color="#E7E7E7"
                progress-color="#E7E7E7"
                knob-color="#fff"
                :knob-radius="17"
              ></circle-slider>
              <!-- <div class="fields_item_num" style="left: 94%; top: 39%;">{{ item.score }}</div> -->
              <div class="fields_item_img"><img :src="item.knowledge.image" alt=""></div>
              <div class="fields_item_txt" >
              <span class="icon-check" v-if="item.score > 0"></span>
                <p>{{ item.knowledge }}</p>
              </div>
            </div>
        </div>

        </div>
      </div>
      <div class="txt_exp"><p>{{$lang.profile.knowDesc}}</p></div>
    </section>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import circleSlider from '@/components/ui/CircleSlider/components/CircleSlider.vue'
export default {
  name: 'MainAriasOfKnowledge',
  data(){
    return{
       profile_knowledge:[
         {
           knowledge: "Гуманитарные науки",
           image: '',
           score: 10
         },
         {
           knowledge: "Техныческие науки",
           image: '',
           score: 15
         },
         {
           knowledge: "Гуманитарные науки",
           image: '',
           score: 5
         },

       ]
    }
  },
  components:{circleSlider},
  computed: {
    ...mapState('auth', ['auth']),
    ...mapState('profile', ['profile_current']),
    profile(){
      return this.profile_current
    },
  },

  methods: {
    ...mapActions('profile', ['getCurrentProfile']),
    async fetchProfile () {
      if(this.auth){
        await this.getCurrentProfile()
        //await this.getUserKnowledges(this.auth.id)
      }

    }
  },

  created () {
    this.fetchProfile()
  }
}
</script>

<style lang="scss" scoped>
  .fields{

    &_col{
      flex-basis: 50%;
      justify-content: center;

    }
  }

  .fields_center{
    bottom: none;
    top: 265px;
  }
  .fields_item {
    background-color: transparent;
    &:before {
      display: none;
    }
  }
  .slider-circle__item {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 1;
  }
</style>
