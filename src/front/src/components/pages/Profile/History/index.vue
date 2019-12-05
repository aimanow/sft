<template>
  <div class="center">
    <section class="section-favorite">
      <div class="h2"><h1>{{$lang.profile.hisThemeTitle}}</h1></div>
      <div class="filter_wrap">
        <div class="filter">
          <div class="filter_search">
             <button type="submit" class="search-btn"><span class="icon-search"></span></button>
            <input type="text" class="t-inp search-t-inp" :placeholder="$lang.profile.hisThemeTitle"/>
          </div>
          <a href="#" class="filter_link btn btn-bord-blue"><span class="icon-filter"></span>{{$lang.profile.hisThemeSort}}</a>
        </div>
        <div class="filter_block">
          <div class="filter_block_top">
            <div class="filter_block_res_title">{{$lang.filter.points}}:</div>
            <div class="filter_block_rads rads">
              <div class="rads_item">
                <label class="radio"><input type="checkbox" checked="">
                  <span class="radio_text">{{$lang.filter.byDate}} <img src="@/assets/svg/arrs.svg" alt=""/></span>
                </label>
              </div>
              <div class="rads_item">
                <label class="radio"><input type="checkbox" checked=""><span class="radio_text">Рус</span></label>
              </div>
              <div class="rads_item">
                <label class="radio"><input type="checkbox"><span class="radio_text">Eng</span></label>
              </div>
              <div class="rads_item">
                <label class="radio"><input type="checkbox"><span class="radio_text">Deu</span></label>
              </div>
              <div class="rads_item">
                <label class="radio"><input type="checkbox"><span class="radio_text">{{$lang.filter.byPop}}</span></label>
              </div>
            </div>
          </div>
          <div class="filter_block_res">
            <div class="filter_block_res_title">{{$lang.filter.byAspects}}:</div>
            <div class="aspect aspect-check aspect-gr">
              <div class="aspect_item">
                <a href="#" class="aspect_item_img">
                  <div class="aspect_item_bg js-bg"><img src="@/assets/img/img3.jpg" alt=""/></div>
                  <div class="aspect_item_text"><span class="icon-check"></span><p>{{$lang.filter.karma}}</p></div></a>
              </div>
              <div class="aspect_item active">
                <a href="#" class="aspect_item_img">
                  <div class="aspect_item_bg js-bg"><img src="@/assets/img/img3.jpg" alt=""/></div>
                  <div class="aspect_item_text"><span class="icon-check"></span><p>{{$lang.filter.earth}}</p></div></a>
              </div>
              <div class="aspect_item ">
                <a href="#" class="aspect_item_img">
                  <div class="aspect_item_bg js-bg"><img src="@/assets/img/img3.jpg" alt=""/></div>
                  <div class="aspect_item_text"><span class="icon-check"></span><p>{{$lang.filter.physics}}</p></div></a>
              </div>
              <div class="aspect_item active">
                <a href="#" class="aspect_item_img">
                  <div class="aspect_item_bg js-bg"><img src="@/assets/img/img3.jpg" alt=""/></div>
                  <div class="aspect_item_text"><span class="icon-check"></span><p>{{$lang.filter.quantum}}</p></div></a>
              </div>
              <div class="aspect_item ">
                <a href="#" class="aspect_item_img">
                  <div class="aspect_item_bg js-bg"><img src="@/assets/img/img3.jpg" alt=""/></div>
                  <div class="aspect_item_text"><span class="icon-check"></span><p>{{$lang.filter.space}}</p></div></a>
              </div>
              <div class="aspect_item active">
                <a href="#" class="aspect_item_img">
                  <div class="aspect_item_bg js-bg"><img src="@/assets/img/img3.jpg" alt=""/></div>
                  <div class="aspect_item_text"><span class="icon-check"></span><p>{{$lang.filter.football}}</p></div></a>
              </div>
              <div class="aspect_item ">
                <a href="#" class="aspect_item_img">
                  <div class="aspect_item_bg js-bg"><img src="@/assets/img/img3.jpg" alt=""/></div>
                  <div class="aspect_item_text"><span class="icon-check"></span><p>{{$lang.filter.space}}</p></div></a>
              </div>
              <div class="aspect_item active">
                <a href="#" class="aspect_item_img">
                  <div class="aspect_item_bg js-bg"><img src="@/assets/img/img3.jpg" alt=""/></div>
                  <div class="aspect_item_text"><span class="icon-check"></span><p>{{$lang.filter.football}}</p></div></a>
              </div>
              <div class="aspect_item ">
                <a href="#" class="aspect_item_img">
                  <div class="aspect_item_bg js-bg"><img src="@/assets/img/img3.jpg" alt=""/></div>
                  <div class="aspect_item_text"><span class="icon-check"></span><p>{{$lang.filter.karma}}</p></div></a>
              </div>
              <div class="aspect_item active">
                <a href="#" class="aspect_item_img">
                  <div class="aspect_item_bg js-bg"><img src="@/assets/img/img3.jpg" alt=""/></div>
                  <div class="aspect_item_text"><span class="icon-check"></span><p>{{$lang.filter.earth}}</p></div></a>
              </div>
              <div class="aspect_item ">
                <a href="#" class="aspect_item_img">
                  <div class="aspect_item_bg js-bg"><img src="@/assets/img/img3.jpg" alt=""/></div>
                  <div class="aspect_item_text"><span class="icon-check"></span><p>{{$lang.filter.physics}}</p></div></a>
              </div>
              <div class="aspect_item active">
                <a href="#" class="aspect_item_img">
                  <div class="aspect_item_bg js-bg"><img src="@/assets/img/img3.jpg" alt=""/></div>
                  <div class="aspect_item_text"><span class="icon-check"></span><p>{{$lang.filter.physics}}</p></div></a>
              </div>
              <div class="aspect_item ">
                <a href="#" class="aspect_item_img">
                  <div class="aspect_item_bg js-bg"><img src="@/assets/img/img3.jpg" alt=""/></div>
                  <div class="aspect_item_text"><span class="icon-check"></span><p>{{$lang.filter.space}}</p></div></a>
              </div>
              <div class="aspect_item active">
                <a href="#" class="aspect_item_img">
                  <div class="aspect_item_bg js-bg"><img src="@/assets/img/img3.jpg" alt=""/></div>
                  <div class="aspect_item_text"><span class="icon-check"></span><p>{{$lang.filter.football}}</p></div></a>
              </div>
              <div class="aspect_item ">
                <a href="#" class="aspect_item_img">
                  <div class="aspect_item_bg js-bg"><img src="@/assets/img/img3.jpg" alt=""/></div>
                  <div class="aspect_item_text"><span class="icon-check"></span><p>{{$lang.filter.space}}</p></div></a>
              </div>
              <div class="aspect_item active">
                <a href="#" class="aspect_item_img">
                  <div class="aspect_item_bg js-bg"><img src="@/assets/img/img3.jpg" alt=""/></div>
                  <div class="aspect_item_text"><span class="icon-check"></span><p>{{$lang.filter.football}}</p></div></a>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="disc">
        <historyItem />
        <historyItem />
        <div class="div-date"><span>2017</span></div>
        <historyItem />
        <historyItem />
        <historyItem />
        <historyItem />
        <historyItem />
        <div class="div-date"><span>2016</span></div>
        <historyItem />
        <historyItem />
        <historyItem />
        <historyItem />

        <div class="div-date"><span>2015</span></div>
        <historyItem />
        <historyItem />
        <historyItem />
        <historyItem />

      </div>
    </section>
    <section class="section-discuss">
      <div class="h2"><h2>{{$lang.profile.hisThemeInterest}}</h2></div>
      <div class="posts posts-sm slick-initialized slick-slider">
        <button type="button" class="slick-prev slick-arrow"><span class="icon-arrow"></span></button>
        <div class="slick-list">
          <div class="slick-track">
            <div class="posts_col">
              <div class="posts_item"><a href="#" class="cover_link"></a>
                <div class="posts_item_img"><img src="@/assets/img/img10.png" alt=""/></div>
                <div class="posts_item_cont">
                  <div class="posts_item_title">Были ли американцы на луне?</div>
                  <div class="posts_item_bot">
                    <div class="posts_item_author">Автор: <b>Бобель</b></div>
                    <a href="#" class="fav_link"><span class="icon-fav"></span></a>
                    <div class="posts_item_date">19.07.2018</div>
                  </div>
                </div>
              </div>
              <div class="posts_item"><a href="#" class="cover_link"></a>
                <div class="posts_item_img"><img src="@/assets/img/img7.png" alt=""/></div>
                <div class="posts_item_cont">
                  <div class="posts_item_title">Были ли американцы на луне?</div>
                  <div class="posts_item_bot">
                    <div class="posts_item_author">Автор: <b>Бобель</b></div>
                    <a href="#" class="fav_link"><span class="icon-fav"></span></a>
                    <div class="posts_item_date">19.07.2018</div>
                  </div>
                </div>
              </div>
            </div>
            <div class="posts_col">
              <div class="posts_item"><a href="#" class="cover_link"></a>
                <div class="posts_item_img"><img src="@/assets/img/img11.png" alt=""/></div>
                <div class="posts_item_cont">
                  <div class="posts_item_title">Были ли американцы на луне?</div>
                  <div class="posts_item_bot">
                    <div class="posts_item_author">Автор: <b>Бобель</b></div>
                    <a href="#" class="fav_link"><span class="icon-fav"></span></a>
                    <div class="posts_item_date">19.07.2018</div>
                  </div>
                </div>
              </div>
              <div class="posts_item"><a href="#" class="cover_link"></a>
                <div class="posts_item_img"><img src="@/assets/img/img13.png" alt=""/></div>
                <div class="posts_item_cont">
                  <div class="posts_item_title">Были ли американцы на луне?</div>
                  <div class="posts_item_bot">
                    <div class="posts_item_author">Автор: <b>Бобель</b></div>
                    <a href="#" class="fav_link"><span class="icon-fav"></span></a>
                    <div class="posts_item_date">19.07.2018</div>
                  </div>
                </div>
              </div>
            </div>
            <div class="posts_col">
              <div class="posts_item"><a href="#" class="cover_link"></a>
                <div class="posts_item_img"><img src="@/assets/img/img12.png" alt=""/></div>
                <div class="posts_item_cont">
                  <div class="posts_item_title">Были ли американцы на луне?</div>
                  <div class="posts_item_bot">
                    <div class="posts_item_author">Автор: <b>Бобель</b></div>
                    <a href="#" class="fav_link"><span class="icon-fav"></span></a>
                    <div class="posts_item_date">19.07.2018</div>
                  </div>
                </div>
              </div>
              <div class="posts_item"><a href="#" class="cover_link"></a>
                <div class="posts_item_img"><img src="@/assets/img/img7.jpg" alt=""/></div>
                <div class="posts_item_cont">
                  <div class="posts_item_title">Были ли американцы на луне?</div>
                  <div class="posts_item_bot">
                    <div class="posts_item_author">Автор: <b>Бобель</b></div>
                    <a href="#" class="fav_link"><span class="icon-fav"></span></a>
                    <div class="posts_item_date">19.07.2018</div>
                  </div>
                </div>
              </div>
            </div>
            <div class="posts_col">
              <div class="posts_item"><a href="#" class="cover_link"></a>
                <div class="posts_item_img"><img src="@/assets/img/img3.jpg" alt=""/></div>
                <div class="posts_item_cont">
                  <div class="posts_item_title">Были ли американцы на луне?</div>
                  <div class="posts_item_bot">
                    <div class="posts_item_author">Автор: <b>Бобель</b></div>
                    <a href="#" class="fav_link"><span class="icon-fav"></span></a>
                    <div class="posts_item_date">19.07.2018</div>
                  </div>
                </div>
              </div>
              <div class="posts_item"><a href="#" class="cover_link"></a>
                <div class="posts_item_img"><img src="@/assets/img/img4.jpg" alt=""/></div>
                <div class="posts_item_cont">
                  <div class="posts_item_title">Были ли американцы на луне?</div>
                  <div class="posts_item_bot">
                    <div class="posts_item_author">Автор: <b>Бобель</b></div>
                    <a href="#" class="fav_link"><span class="icon-fav"></span></a>
                    <div class="posts_item_date">19.07.2018</div>
                  </div>
                </div>
              </div>
            </div>
            <div class="posts_col">
              <div class="posts_item"><a href="#" class="cover_link"></a>
                <div class="posts_item_img"><img src="@/assets/img/img15.jpg" alt=""/></div>
                <div class="posts_item_cont">
                  <div class="posts_item_title">Были ли американцы на луне?</div>
                  <div class="posts_item_bot">
                    <div class="posts_item_author">Автор: <b>Бобель</b></div>
                    <a href="#" class="fav_link"><span class="icon-fav"></span></a>
                    <div class="posts_item_date">19.07.2018</div>
                  </div>
                </div>
              </div>
              <div class="posts_item"><a href="#" class="cover_link"></a>
                <div class="posts_item_img"><img src="@/assets/img/img5.jpg" alt=""/></div>
                <div class="posts_item_cont">
                  <div class="posts_item_title">Были ли американцы на луне?</div>
                  <div class="posts_item_bot">
                    <div class="posts_item_author">Автор: <b>Бобель</b></div>
                    <a href="#" class="fav_link"><span class="icon-fav"></span></a>
                    <div class="posts_item_date">19.07.2018</div>
                  </div>
                </div>
              </div>
            </div>
            <div class="posts_col">
              <div class="posts_item"><a href="#" class="cover_link"></a>
                <div class="posts_item_img"><img src="@/assets/img/img6.jpg" alt=""/></div>
                <div class="posts_item_cont">
                  <div class="posts_item_title">Были ли американцы на луне?</div>
                  <div class="posts_item_bot">
                    <div class="posts_item_author">Автор: <b>Бобель</b></div>
                    <a href="#" class="fav_link"><span class="icon-fav"></span></a>
                    <div class="posts_item_date">19.07.2018</div>
                  </div>
                </div>
              </div>
              <div class="posts_item"><a href="#" class="cover_link"></a>
                <div class="posts_item_img"><img src="@/assets/img/img7.jpg" alt=""/></div>
                <div class="posts_item_cont">
                  <div class="posts_item_title">Были ли американцы на луне?</div>
                  <div class="posts_item_bot">
                    <div class="posts_item_author">Автор: <b>Бобель</b></div>
                    <a href="#" class="fav_link"><span class="icon-fav"></span></a>
                    <div class="posts_item_date">19.07.2018</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <button type="button" data-role="none" class="slick-next slick-arrow" aria-label="Next" role="button" style=""><span class="icon-arrow"></span></button>
        <div class="dots_wrap">
          <ul class="slick-dots">
            <li class="slick-active" id="slick-slide00"><button type="button">1</button></li>
            <li id="slick-slide01"><button type="button">2</button></li>
            <li id="slick-slide02"><button type="button">3</button></li>
          </ul>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import historyItem from './historyItem'
export default {
  components: {
    historyItem
  },

  name: 'index'
}
</script>

<style scoped>

</style>
