<template>
  <div class="disc_line">
    <div class="disc_line_img"><img src="@/assets/img/ar1.png" alt=""/></div>
    <div class="disc_line_cont">
      <div class="disc_line_inf">
        <div class="disc_line_name"><a href="#">Можно ли сойти с ума в <br/>{{$lang.filter.space}}е?</a></div>
        <div class="disc_line_athor"><span>Автор:</span> Бобель </div>
        <div class="disc_line_date">19.07.2018 </div>
      </div>
      <div class="truefalse"><span>80%</span><span>20%</span></div>
      <a href="#" class="fav_link active"><span class="icon-fav2"></span></a>
    </div>
  </div>
</template>

<script>
export default {
  name: 'historyItem'
}
</script>

<style scoped>

</style>
