$(window).on('load',function(){
	if( /Android|webOS|iPhone|iPad|iPod|BlackBerry/i.test(navigator.userAgent) ) {
		$('body').addClass('ios');
        
	} else{
		$('body').addClass('web');
        
	};
	$('body').delay(500).removeClass('loaded'); 
});
/* viewport width */
function viewport(){
	var e = window, 
		a = 'inner';
	if ( !( 'innerWidth' in window ) )
	{
		a = 'client';
		e = document.documentElement || document.body;
	}
	return { width : e[ a+'Width' ] , height : e[ a+'Height' ] }
};
/* viewport width */


$(function(){
	/* placeholder*/	   
	$('input, textarea').each(function(){
 		var placeholder = $(this).attr('placeholder');
 		$(this).focus(function(){ $(this).attr('placeholder', '');});
 		$(this).focusout(function(){			 
 			$(this).attr('placeholder', placeholder);  			
 		});
 	});
	/* placeholder*/ 

  //
  $('.mobile-button').on('click', function(){
    $(this).toggleClass('open'); 
    $('.mob-side').toggleClass('open'); 
    $('.header_overlay').toggleClass('openSide'); 
    $('body').toggleClass('hid'); 
    return false;    
  });

  $('.mob-side_close').on('click', function(){
    $(this).removeClass('open');
    $('.header_overlay').removeClass('openSide');      
    $('.mob-side').removeClass('open'); 
    $('body').removeClass('hid');     
    return false;      
  });
  $('.header_overlay').on('click', function(){    
    $(this).removeClass('openSide');
    $('.mobile-button').removeClass('open'); 
    $('.mob-side').removeClass('open'); 
    $('body').removeClass('hid'); 
    return false;      
  });


  $('.js-bg').each(function(e){
      $(this).css('background-image', 'url('+$(this).find("img").attr("src")+')');
      $(this).find("img").hide();
  });
 
  //
  $('.moveTop').on('click', function(){
    $("html, body").animate({ scrollTop: 0 }, 300);
    $('.section-main').addClass('vs');
    return false;    
  });

  //
  $(".jq-selectbox__select").click(function () { 
      $(this).parent().toggleClass('opened');
      $(this).next('.jq-selectbox__dropdown').toggle();
      return false;
  });
  $(document).on('click', function(event) {
      if ($(event.target).closest(".jq-selectbox").length === 0) {
        $('.jq-selectbox').removeClass('opened');   
        $('.jq-selectbox__dropdown').hide(); 
      }
  });

  //cab_top_opener
  $('.cab_top_opener').on('click', function(){
    $('.cab').toggleClass('open');
    return false;    
  });

  //
  $('.filter_link').on('click', function(){  
    $(this).toggleClass('active');
    $('.filter_block').slideToggle(300);
    return false;    
  });

  //
  $('.disc_line_opener').on('click', function(){  
    $(this).parents('.disc_item').toggleClass('open');
    $(this).parents('.disc_item').find('.disc_line_body').slideToggle(300);
    return false;    
  });

  $('.comm_adds_opener').on('click', function(){    
    $(this).parent('.comm_adds').toggleClass('open');
    return false;    
  });

  //select_country_top
  $(".select_country_top").click(function () { 
      $(this).next('.select_country_drop').toggle();
      return false;
  });
  $(document).on('click', function(event) {
      if ($(event.target).closest(".select_country").length === 0) {
        $('.select_country_drop').hide(); 
      }
  });



});

//

var handler = function(){
	
	var height_footer = $('.footer').height();	
	var height_header = $('.header').height();		
	
	var viewport_wid = viewport().width;
	var viewport_height = viewport().height;

	if (viewport_wid <= 699) {
		
	}
  if ((viewport_wid <= 1024) && (viewport_wid > 699)) {
    
  }
	else {
		
	}

  
	
}
$(window).bind('load', handler);
$(window).bind('resize', handler);


