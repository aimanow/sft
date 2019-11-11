<template>
  <div class="center">
    <section class="section-favorite">
      <div class="h2"><h1>Архив тем дискуссий</h1></div>
      <div class="filter_wrap">
        <div class="filter">
          <div class="filter_search">
            <form>
              <button type="submit" class="search-btn"><span class="icon-search"></span></button>
              <input type="text" class="t-inp search-t-inp" placeholder="Введите название темы дискуссии"/>
            </form>
          </div>
          <a href="#" @click.prevent="showFilter = !showFilter" class="filter_link btn btn-bo rd-blue"><span class="icon-filter"></span>Фильтр</a>
        </div>
        <div class="filter_block" :class="{'show':showFilter}">
          <div class="filter_block_top">
            <div class="filter_block_res_title">Выберите нужные пункты:</div>
            <div class="filter_block_rads rads">
              <div class="rads_item">
                <label class="radio"><input type="checkbox" checked="" placeholder="">
                  <span class="radio_text">По дате <img src="@/assets/svg/arrs.svg" alt=""></span>
                </label>
              </div>
              <div class="rads_item">
                <label class="radio"><input type="checkbox" checked=""><span class="radio_text">Рус</span></label>
              </div>
              <div class="rads_item">
                <label class="radio"><input type="checkbox" placeholder=""><span class="radio_text">Eng</span></label>
              </div>
              <div class="rads_item">
                <label class="radio"><input type="checkbox" placeholder=""><span class="radio_text">Deu</span></label>
              </div>
              <div class="rads_item">
                <label class="radio"><input type="checkbox" placeholder=""><span class="radio_text">По популярности</span></label>
              </div>
            </div>
          </div>
          <div class="filter_block_res">
            <div class="filter_block_res_title">По аспектам:</div>
            <div class="aspect aspect-check aspect-gr">
              <div class="aspect_item">
                <a href="#" class="aspect_item_img">
                  <div class="aspect_item_bg js-bg" style="background-image: url('@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
                  <div class="aspect_item_text"><span class="icon-check"></span><p>Карма</p></div></a>
              </div>
              <div class="aspect_item active">
                <a href="#" class="aspect_item_img">
                  <div class="aspect_item_bg js-bg" style="background-image: url('@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
                  <div class="aspect_item_text"><span class="icon-check"></span><p>Земля</p></div></a>
              </div>
              <div class="aspect_item ">
                <a href="#" class="aspect_item_img">
                  <div class="aspect_item_bg js-bg" style="background-image: url('@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
                  <div class="aspect_item_text"><span class="icon-check"></span><p>Физика</p></div></a>
              </div>
              <div class="aspect_item active">
                <a href="#" class="aspect_item_img">
                  <div class="aspect_item_bg js-bg" style="background-image: url('@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
                  <div class="aspect_item_text"><span class="icon-check"></span><p>Квантовая механика</p></div></a>
              </div>
              <div class="aspect_item ">
                <a href="#" class="aspect_item_img">
                  <div class="aspect_item_bg js-bg" style="background-image: url('@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
                  <div class="aspect_item_text"><span class="icon-check"></span><p>Космос</p></div></a>
              </div>
              <div class="aspect_item active">
                <a href="#" class="aspect_item_img">
                  <div class="aspect_item_bg js-bg" style="background-image: url('@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
                  <div class="aspect_item_text"><span class="icon-check"></span><p>Футбол</p></div></a>
              </div>
              <div class="aspect_item ">
                <a href="#" class="aspect_item_img">
                  <div class="aspect_item_bg js-bg" style="background-image: url('@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
                  <div class="aspect_item_text"><span class="icon-check"></span><p>Космос</p></div></a>
              </div>
              <div class="aspect_item active">
                <a href="#" class="aspect_item_img">
                  <div class="aspect_item_bg js-bg" style="background-image: url('@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
                  <div class="aspect_item_text"><span class="icon-check"></span><p>Футбол</p></div></a>
              </div>
              <div class="aspect_item ">
                <a href="#" class="aspect_item_img">
                  <div class="aspect_item_bg js-bg" style="background-image: url('~@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
                  <div class="aspect_item_text"><span class="icon-check"></span><p>Карма</p></div></a>
              </div>
              <div class="aspect_item active">
                <a href="#" class="aspect_item_img">
                  <div class="aspect_item_bg js-bg" style="background-image: url('~@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
                  <div class="aspect_item_text"><span class="icon-check"></span><p>Физика</p></div></a>
              </div>
              <div class="aspect_item active">
                <a href="#" class="aspect_item_img">
                  <div class="aspect_item_bg js-bg" style="background-image: url('~@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
                  <div class="aspect_item_text"><span class="icon-check"></span><p>Физика</p></div></a>
              </div>
              <div class="aspect_item ">
                <a href="#" class="aspect_item_img">
                  <div class="aspect_item_bg js-bg" style="background-image: url('~@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
                  <div class="aspect_item_text"><span class="icon-check"></span><p>Космос</p></div></a>
              </div>
              <div class="aspect_item active">
                <a href="#" class="aspect_item_img">
                  <div class="aspect_item_bg js-bg" style="background-image: url('~@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
                  <div class="aspect_item_text"><span class="icon-check"></span><p>Футбол</p></div></a>
              </div>
              <div class="aspect_item ">
                <a href="#" class="aspect_item_img">
                  <div class="aspect_item_bg js-bg" style="background-image: url('~@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
                  <div class="aspect_item_text"><span class="icon-check"></span><p>Космос</p></div></a>
              </div>
              <div class="aspect_item active">
                <a href="#" class="aspect_item_img">
                  <div class="aspect_item_bg js-bg" style="background-image: url('~@/assets/img/ar1.png');"><img src="img/img3.jpg" alt="" style="display: none;"></div>
                  <div class="aspect_item_text"><span class="icon-check"></span><p>Футбол</p></div></a>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="disc">
        <div v-for="(items, i) in archive" :key="`archiveItems_${i}`">
          <item v-for="(item, index) in items" :item="item" :key="`items_${index}`"></item>
          <div class="div-date"><span>{{i}}</span></div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
  import item from './archiveItem'
  import {mapState} from 'vuex'
  export default {
    name: "index",
    data() {
      return {
        showFilter: false
      }
    },

    components: {item},

    computed: { ...mapState('archive', ['archive']) }
  }
</script>

<style scoped>
  .show {
    display: block !important;
  }
</style>
