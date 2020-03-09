	
	
      //revolution-slider
		
jQuery(document).ready(function($) {

		
	if ( $('.fullscreenbanner').length){
			
			
		var api =	
		
		$('.fullscreenbanner').revolution(
		{
					//delay:9000,
					 //startwidth:1170,
					 startheight:710,
					 startWithSlide:0,
			 
					 fullScreenAlignForce:"off",
					 autoHeight:"off",
					 minHeight:"off",
			 
					 shuffle:"off",
			 
					 onHoverStop:"on",
			 
					 thumbWidth:100,
					 thumbHeight:50,
					 thumbAmount:3,
			 
					 hideThumbsOnMobile:"off",
					 hideNavDelayOnMobile:1500,
					 hideBulletsOnMobile:"off",
					 hideArrowsOnMobile:"off",
					 hideThumbsUnderResoluition:0,
			 
					 hideThumbs:0,
					 hideTimerBar:"off",
			 
					 keyboardNavigation:"on",
			 
					 navigationType:"bullet",
					 navigationArrows:"solo",
					 navigationStyle:"round",
			 
					 navigationHAlign:"center",
					 navigationVAlign:"bottom",
					 navigationHOffset:30,
					 navigationVOffset:30,
			 
					 soloArrowLeftHalign:"left",
					 soloArrowLeftValign:"center",
					 soloArrowLeftHOffset:20,
					 soloArrowLeftVOffset:0,
			 
					 soloArrowRightHalign:"right",
					 soloArrowRightValign:"center",
					 soloArrowRightHOffset:20,
					 soloArrowRightVOffset:0,
			 
			 
					 touchenabled:"on",
					 swipe_velocity:"0.7",
					 swipe_max_touches:"1",
					 swipe_min_touches:"1",
					 drag_block_vertical:"false",
			 
					 parallax:"mouse",
					 parallaxBgFreeze:"on",
					 parallaxLevels:[10,7,4,3,2,5,4,3,2,1],
					 parallaxDisableOnMobile:"off",
			 
					 stopAtSlide:-1,
					 stopAfterLoops:-1,
					 hideCaptionAtLimit:0,
					 hideAllCaptionAtLilmit:0,
					 hideSliderAtLimit:0,
			 
					 dottedOverlay:"none",
			 
					 spinned:"spinner4",
			 
					 fullWidth:"off",
					 forceFullWidth:"off",
					 fullScreen:"0ff",
					 fullScreenOffsetContainer:"#topheader-to-offset",
					 fullScreenOffset:"0px",
			 
					 panZoomDisableOnMobile:"off",
			 
					 simplifyAll:"off",
			 
					 shadow:0
			
				});
			
			api.revpause();
	}
	
	//revolution-slider 2
	
	if ( $('.fullscreenbanner-banner-2').length)
	{		
			
		var api =	
		
		$('.fullscreenbanner-banner-2').revolution(
		{
			//delay:9000,
			 //startwidth:1170,
			 startheight:364,
			 startWithSlide:0,
			 navigationType: 'none',			
	
		});
			
		api.revpause();
	}
	
	//price slider
	
	$(function() {
		
		if( $('#slider-range').length ) {
			$( "#slider-range" ).slider({
				range: true,
				min: 0,
				max: 600,
				values: [ 50, 410 ],
				slide: function( event, ui ) {
					$( "#amount" ).val( "" + ui.values[ 0 ] + " - " + ui.values[ 1 ] + "$" );
				}
			});
			$( "#amount" ).val( "" + $( "#slider-range" ).slider( "values", 0 ) +
			" - " + $( "#slider-range" ).slider( "values", 1 ) + "$" );
		}
		
	
		if( $('#slider-range2').length ) {
			$( "#slider-range2" ).slider({
				range: true,
				min: 0,
				max: 600,
				values: [ 50, 410 ],
				slide: function( event, ui ) {
					$( "#amount2" ).val( "" + ui.values[ 0 ] + " - $" + ui.values[ 1 + "$" ] );
				}
			});
			$( "#amount2" ).val( "" + $( "#slider-range2" ).slider( "values", 0 ) +
			" - " + $( "#slider-range2" ).slider( "values", 1 ) + "$" );
		}
	
	
		if( $('#slider-range3').length ) {
			$( "#slider-range3" ).slider({
				range: true,
				min: 0,
				max: 600,
				values: [ 50, 410 ],
				slide: function( event, ui ) {
					$( "#amount3" ).val( "" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] + "$" );
				}
			});
			
			$( "#amount3" ).val( "" + $( "#slider-range3" ).slider( "values", 0 ) +
			" - " + $( "#slider-range3" ).slider( "values", 1 ) + "$" );
		}
		
		
		if( $('#slider-range4').length ) {
			$( "#slider-range4" ).slider({
				range: true,
				min: 0,
				max: 300,
				values: [ 84, 122 ],
				slide: function( event, ui ) {
					$( "#size" ).val( ui.values[ 0 ] + " -" + ui.values[ 1 ] + "Sq Ft" );
				}
			});
			
			$( "#size" ).val( $( "#slider-range4" ).slider( "values", 0 ) +
			" - " + $( "#slider-range4" ).slider( "values", 1 ) + "Sq Ft " );
		}
	
	
	});	
	
	
	//testimonial carousel
	
	try {
		$('.testi-carousel').owlCarousel({
			items: 1,
			navigation : true,
			navigationText: false,
			pagination: true,
			itemsCustom: [[768,1], [600,1], [360,1], [320,1]],
			slideSpeed: 1000
		});
	} catch(e) {
		console.log( 'testi-carousel error' );
	}
	
	//partner carousel
	
	try {
		
		$('.partner-carousel').owlCarousel({
			items: 5,
			navigation : true,
			navigationText: true,
			pagination: false,
			autoPlay: true,
			itemsCustom: [[1300,5], [768,3], [600,3],[480,2],[320,1]],
			slideSpeed: 1000
		});
	} catch(e) {
		console.log( 'partner-carousel error' );
	}


	//portfoli mixitup	
	try {	
	
		$('.filter-list').mixitup( {
			effects: ['fade', 'blur']
		});
		
		
		
		$(function(){
			$('.filter-property').on('click', function(e) {
				e.preventDefault();
				var price1 = $('input[name=min-price]').val(),
				price2 = $('input[name=max-price]').val(),
				$container = $('.filter-list');
				
				// Filter the mixed elements
				var $show = $container.find('.mix').filter(function(){
					var price = Number($(this).attr('data-price'));
					
					return price >= price1 && price <= price2;
				});
				//console.log($show);
				// Call mix it up to.. well.. mix it up..
				$container.find('.mix').removeClass('custom-price-filter');
				
				$.each($show, function( index, element ) {
					$(this).addClass('custom-price-filter');
				});
				$container.mixitup('filter', 'custom-price-filter');

			});
		});
		
	} catch(e) {
		console.log ('filter-list error' );
	}
	
	
	//photo box

	try{
		$('.zoom-img').photobox('a',{ time:0 });
	} catch(e) {
		console.log( 'Photo box error ' );
	}
	
	//photo box for blog-img
	
	try{
		$('.blogsingle-img').photobox('a',{ time:0 });
	} catch(e) {
		console.log( 'Photo box error ' );
	}
	
	
	//photo box for agent-img
	
	try{
		$('.agent-img').photobox('a',{ time:0 });
	} catch(e) {
		console.log( 'Photo box error ' );
	}
	
	
	// checkbox
	
	
	$(window).load(function(e){
		$('.checkbox input[type=checkbox]:checked').next('span').addClass('checked').parent('label').addClass('selected');	
	});
	
	$('.checkbox input[type=checkbox]').change(function(e) {
		e.preventDefault();
		$(this).next('span').toggleClass('checked');
		$(this).parent('label').toggleClass('selected');
	});
	
 
	try{
		//google-map
		if( $('#map-street').length ) {    
			var locations = [
				['<div class="infobox">BHALI RESORT<i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div>', 40.5458921,-74.1843522, 2],
				//['<div class="infobox">121 King Street, Melbourne Victoria 3000<br />United States of America, CA 90017</div>', 40.550121,-74.187378, 3],
				//['<div class="infobox">Vineland Avenue, Staten Island, NY<br />United States of America, CA 90017</div>', 40.5474649,-74.187468, 2]
			];
		
			var map = new google.maps.Map(document.getElementById('map-street'), {
			  zoom: 15,
				scrollwheel: false,
				navigationControl: true,
				mapTypeControl: false,
				scaleControl: false,
				draggable: true,
		
				center: new google.maps.LatLng(40.550121,-74.187378),
			  mapTypeId: google.maps.MapTypeId.ROADMAP
			});
		
			var infowindow = new google.maps.InfoWindow();
		
			var marker, i;
				
			for (i = 0; i < locations.length; i++) {  
		  
				marker = new google.maps.Marker({ 
				position: new google.maps.LatLng(locations[i][1], locations[i][2]), 
				map: map ,
				icon: 'images/marker.png'
				});
		
			  google.maps.event.addListener(marker, 'click', (function(marker, i) {
				return function() {
				  infowindow.setContent(locations[i][0]);
				  infowindow.open(map, marker);
				}
			  })(marker, i));
			}
		}
	} catch(e) {
		console.log( 'google map error' );
	}
	
	try{
		//google-map-2
		if( $('#map-street-2').length ) {  
			var locations = [
				['<div class="infobox-2">HEADQUARTERS</div>', 40.5458921,-74.1843522, 2],
				//['<div class="infobox">121 King Street, Melbourne Victoria 3000<br />United States of America, CA 90017</div>', 40.550121,-74.187378, 3],
				//['<div class="infobox">Vineland Avenue, Staten Island, NY<br />United States of America, CA 90017</div>', 40.5474649,-74.187468, 2]
			];
		
			var map = new google.maps.Map(document.getElementById('map-street-2'), {
			  zoom: 15,
				scrollwheel: false,
				navigationControl: true,
				mapTypeControl: false,
				scaleControl: false,
				draggable: true,
		
				center: new google.maps.LatLng(40.550121,-74.187378),
			  mapTypeId: google.maps.MapTypeId.ROADMAP
			});
		
			var infowindow = new google.maps.InfoWindow();
		
			var marker, i;
				
			for (i = 0; i < locations.length; i++) {  
		  
				marker = new google.maps.Marker({ 
				position: new google.maps.LatLng(locations[i][1], locations[i][2]), 
				map: map ,
				icon: 'images/marker-2.png'
				});
		
			  google.maps.event.addListener(marker, 'click', (function(marker, i) {
				return function() {
				  infowindow.setContent(locations[i][0]);
				  infowindow.open(map, marker);
				}
			  })(marker, i));
			}
		}
	} catch(e) {
		console.log( 'google map error' );
	}
	
	function syncPosition(el){
		var current = this.currentItem;
		$(".sync2")
		  .find(".owl-item")
		  .removeClass("synced")
		  .eq(current)
		  .addClass("synced")
		if($(".sync2").data("owlCarousel") !== undefined){
		  center(current)
		}
	  }
	
	
	try {
		//property carousel
		  var sync1 = $(".sync1");
		  var sync2 = $(".sync2");
		 
		  sync1.owlCarousel({
			items: 1,
			itemsCustom: [[1300,5], [768,3], [600,2],[480,2],[320,1]],
			singleItem : true,
			slideSpeed : 1000,
			navigation: true,
			pagination:false,
			afterAction : syncPosition,
			responsiveRefreshRate : 200,
			scrollPerPage:1
		  });
		 
		  sync2.owlCarousel({
			items : 1,
			itemsCustom: [[1300,5], [768,2], [600,2],[480,2],[320,1]],
			pagination:false,
			responsiveRefreshRate : 100,
			afterInit : function(el){
			  el.find(".owl-item").eq(0).addClass("synced");
			},
			scrollPerPage: 1
		  });
		 
		  
		 
		  $(".sync2").on("click", ".owl-item", function(e){
			e.preventDefault();
			var number = $(this).data("owlItem");
			sync1.trigger("owl.goTo",number);
		  });
		 
		  function center(number){
			var sync2visible = sync2.data("owlCarousel").owl.visibleItems;
			var num = number;
			var found = false;
			for(var i in sync2visible){
			  if(num === sync2visible[i]){
				var found = true;
			  }
			}
		 
			if(found===false){
			  if(num>sync2visible[sync2visible.length-1]){
				sync2.trigger("owl.goTo", num - sync2visible.length+2)
			  }else{
				if(num - 1 === -1){
				  num = 0;
				}
				sync2.trigger("owl.goTo", num);
			  }
			} else if(num === sync2visible[sync2visible.length-1]){
			  sync2.trigger("owl.goTo", sync2visible[1])
			} else if(num === sync2visible[0]){
			  sync2.trigger("owl.goTo", num-1)
			}
			
		  }
	} catch(e) {
		console.log( 'owl carousel custom script error '+e.message );
	}	  
	  
	  
	  //radiobtn
	  
	  
	  	$(window).load(function(e){
		$('.radio input[type=radio]:checked').next('span').addClass('checked').parent('label').addClass('selected');	
	});
	
	$('.radio input[type=radio]').on('change', function(e) {
		e.preventDefault();
		$('.radio input[type=radio]').next('span').removeClass('checked');
		$('.radio input[type=radio]').parent('label').removeClass('selected');
		$(this).next('span').addClass('checked');
		$(this).parent('label').addClass('selected');
	});
	
	$('.navbar-header > .navbar-toggle').on('click', function(e){
		 e.preventDefault();
	  
		 $('#navbar').slideToggle('slow');
	 });
	  
	 
	 if ( $('.animated').length){
		var $ = jQuery;
	
		$('.animated').appear(function(){
			var element = $(this);
			var animation = element.data('animation');
			var animationDelay = element.data('delay');
		if (animationDelay) {
			setTimeout(function(){
			element.addClass( animation + " in" );
			element.removeClass('out');
		  }, animationDelay);
		}
		else {
			element.addClass( animation + " in" );
			element.removeClass('out');
		}    
		
		},{accY: -150});
		
	}
});
	
