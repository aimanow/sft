<template>
  <div class="win win-schedule" id="win-schedule">
    <div class="win_cont">
      <div class="schedule_block">
        <div class="schedule_block_in">

          <div class="schedule_block_tech">
            <div class="item-row" v-for="i in 10" :key="i">
              <div @click="cords = [i, j]" class="schedule_block_tech__item" v-for="j in 10" :key="j">
                <div v-if="i === cords[0] && j === cords[1]" class="schedule_block_c"></div>
              </div>
            </div>

          </div>
        </div>
        <div class="schedule_txt"><div :style="$lang.descAdd.graphCredibleness.length<13?'top: 10px; position: relative':''">{{$lang.descAdd.graphCredibleness}}</div></div>
        <div class="schedule_txt2">{{$lang.descAdd.graphPersuasiveness}}</div>
        <div class="schedule_n schedule_n0">0</div>
        <div class="schedule_n schedule_n5">5</div>
        <div class="schedule_n schedule_n10">10</div>
        <div class="schedule_n schedule_n52">5</div>
        <div class="schedule_n schedule_n102">10</div>
      </div>
      <div class="schedule_block_bottom">
        <div class="schedule_left">
          <div class="schedule_rline">{{$lang.descAdd.graphPersRaiting}}: <span>{{cords[1] - 1}}</span></div>
          <div class="schedule_rline">{{$lang.descAdd.graphCredRaiting}}: <span>{{10 - cords[0]}}</span></div>
        </div>
        <div class="schedule_right">
          <a href="#" class="btn">{{$lang.descAdd.graphCommit}}</a>
        </div>
      </div>
    </div>
    <a href="#" class="win_close"><span class="icon-cab7"></span></a>
  </div>
</template>

<script>
export default {
  name: 'Main',
  data() {
    return {
      cords: [2, 7]
    }
  },
}
</script>

<style scoped>
  .item-row {
    width: 100%;
    display: flex;
    height: 10%;
  }

  .schedule_block_tech__item {
    width: 10%;
    height: 100%;
    position: relative;
    box-shadow: inset -2px -2px 0 -1px #dcdcdc
  }
</style>
