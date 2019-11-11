<template>
  <div class="schedule_block_in"><div class="schedule_block_c" :style="{ left: x*10+'%', top: (100-y*10)+'%' }"></div></div>
</template>

<script>
    export default {
        name: "Scale",
        props: ['x','y']
    }
</script>
<style scoped lang="scss">
  .schedule_block_in{
    background: #B8C6D6;
    &:before, &:after{
      background: white;
    }
    .schedule_block_c{
      width:20px;
      height: 20px;
      margin: -10px 0 0 -10px;
      left:0%;
      top: 0%;
      &:after{
        width:8px;
        height: 8px;
        margin: 0;
        transform: translateX(-50%) translateY(-50%);

      }
    }
  }

</style>
