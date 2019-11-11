<template>
  <div class="win win-complaints" id="win-complaints">
    <div class="win_cont">
      <div class="complaints_block">
        <div class="complaints_block_title">Оставьте свое жалобу в этой форме, и мы примем меры</div>
        <div class="complaints_block_wrap">

          <div class="form_row">
            <label><span class="error">*</span>  Причина:</label>
            <div class="form_el">
              <div class="jq-selectbox jqselect placeholder">
                <div class="jq-selectbox__select">
                  <div class="jq-selectbox__select-text">Пока ничего не выбрано</div>
                  <div class="jq-selectbox__trigger"><div class="jq-selectbox__trigger-arrow"></div></div>
                </div>
                <div class="jq-selectbox__dropdown">
                  <ul>
                    <li class="selected sel placeholder">Пока ничего не выбрано</li>
                    <li style="">Предложение о сотрудничестве</li>
                    <li style="">Жалоба</li>
                    <li style="">Пожелания</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
          <div class="form_row">
            <label>Сообщение:</label>
            <div class="form_el"><textarea></textarea></div>
          </div>
          <div class="form_row">
            <label>Введите код:</label>
            <div class="form_el">
              <input type="text" class="t-inp capt_inp">
              <div class="capt_img"><img src="img/image.jpg" alt=""/></div>

            </div>
          </div>
          <div class="form_btn"><input type="submit" value="Отправить" class="btn"></div>

        </div>
      </div>
    </div>
    <a href="#" class="win_close"><span class="icon-cab7"></span></a>
  </div>
</template>

<script>
    export default {
        name: "Complaints"
    }
</script>

<style scoped>

</style>
