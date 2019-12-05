<template>
  <footer class="footer">
    <div class="wrapper">
      <div class="foter_left">
        <h4 class="m-hid">{{$lang.footer.stayConnect}}</h4>
        <div class="soc footer_soc">
          <a href="#" class="soc_link"><span class="icon-fb"></span></a>
          <a href="#" class="soc_link"><span class="icon-inst"></span></a>
          <a href="#" class="soc_link"><span class="icon-vk"></span></a>
          <a href="#" class="soc_link"><span class="icon-tw"></span></a>
          <a href="#" class="soc_link"><span class="icon-youtube"></span></a>
        </div>
        <div class="footer_copy">© 2019 SFT. All rights reserved.</div>
      </div>
      <div class="footer_col m-hid">
        <h4>{{$lang.footer.footSup}}</h4>
        <ul class="footer_list">
          <li><a href="#">{{$lang.main.terms}}</a></li>
          <li><a href="#">{{$lang.footer.aboutSite}}</a></li>
          <li><a href="#">{{$lang.footer.contacts}}</a></li>
          <li><a href="#">{{$lang.footer.faq}}</a></li>
        </ul>
      </div>
      <div class="footer_col m-hid">
        <h4>{{$lang.footer.footStruct}}</h4>
        <ul class="footer_list">
          <li><a href="#">{{$lang.footer.quickStart}}</a></li>
          <li><a href="#">{{$lang.footer.supportProject}}</a></li>
          <li><a href="#">{{$lang.footer.developSitemap}}</a></li>
        </ul>
      </div>
      <div class="footer_col m-hid">
      </div>
      <div class="footer_col m-hid">
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'Footer'
}
</script>

<style scoped>

</style>
