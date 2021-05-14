/* 
======================================
        Table of Content
======================================
1)  header fixed
2)  Search
3)  preloader
4)  header options custom
5)  responsive menu
6)  mobile menu
7)  banner slider
8)  testimonial slider
9)  blog slider
10) Special product slider
11) Related Product slider
12) Brand logo slider
13) Product Zoom & Slider
14) scrol to top button
15) Countdown
16) Newsletter popup window
17) Color Selector
18) Category view
19) verticle toggle
20) Theme Features
21) light-dark mode
22) color option
======================================
*/
(function($){
  "use strict";


  //==================== header fixed ====================//
  var fixed_top = $(".header-section");
  $(window).on("scroll", function(){
      if( $(window).scrollTop() > 50){  
          fixed_top.addClass("animated fadeInDown menu-fixed");
      }
      else{
          fixed_top.removeClass("animated fadeInDown menu-fixed");
      }
  });
  

 //================ Search ============================//
 jQuery(window).resize(function(){
  var width =jQuery(window).width();
    if (width <= 1199) {
    jQuery('.search-block').insertAfter(jQuery('.header-banner .main-menu'));
    }
    else{
    jQuery('.header-banner .search-block').insertAfter(jQuery('.verticle-menu'));  
    }
  });
  jQuery(window).resize();



  $(window).on('load', function(){

      //==================== preloader====================//
      $("#preloader").delay(300).animate({
        "opacity" : "0"
        }, 500, function() {
        $("#preloader").css("display","none");
    });

     responsiveSize();
     $(window).resize(responsiveSize);

    //==================== header options custom ====================//
    var fixed_top = $(".header-section");
    $(window).on("scroll", function(){
      
      if( $(this).scrollTop() > 50 ){  
        fixed_top.addClass("header-close");
      }
      else{
        fixed_top.removeClass("header-close");
      }
    });

  });

  //==================== responsive menu ====================//
  function responsiveSize(){
    if (window.matchMedia('(max-width: 1199px)').matches) {
      $(".navbar-collapse>ul>li>a, .navbar-collapse ul.sub-menu>li>a").on("click", function() {
        var element = $(this).parent("li");
        if (element.hasClass("open")) {
          element.removeClass("open");
          element.find("li").removeClass("open");
          element.find("ul").slideUp(500,"linear");
        }
        else {
          element.addClass("open");
          element.children("ul").slideDown();
          element.siblings("li").children("ul").slideUp();
          element.siblings("li").removeClass("open");
          element.siblings("li").find("li").removeClass("open");
          element.siblings("li").find("ul").slideUp();
        }
      });
    }
  }

  //==================== mobile menu ====================//
  $(".menu-toggle").on("click", function() {
      $(this).toggleClass("is-active");
      $('.header-section').toggleClass("responsive-menu-fixed");
  });


  //==================== banner slider ====================//
  $('.banner-section').slick({
    infinite: true,
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    arrows: true,
    dots: false
  });


  //============== testimonial slider =========================//
  $('.testimonial-slider').slick({
    infinite: true,
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    arrows: false,
    dots: true
  });

    //============== testimonial slider =========================//
  $('.testimonial-slider-index2').slick({
    infinite: true,
    slidesToShow: 2,
    slidesToScroll: 1,
    autoplay: true,
    arrows: false,
    dots: true,
    responsive: [
    {
      breakpoint: 991,
      settings: {
        slidesToShow: 2,
      }
    },  
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
      }
    }
  ]
  });

  //============== blog slider =========================//
  $('.blog-slider').slick({
  slidesToShow: 3,
  slidesToScroll: 1,
  arrows: true,
  appendArrows: '.blogarrow',
  dots: false,
  responsive: [
    {
      breakpoint: 991,
      settings: {
        slidesToShow: 2,
      }
    },  
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
      }
    }
  ]
  });

    //============== blog slider =========================//
  $('.blog-slider-index3').slick({
  slidesToShow: 2,
  slidesToScroll: 1,
  arrows: true,
  appendArrows: '.blogarrow',
  dots: false,
  responsive: [
    {
      breakpoint: 991,
      settings: {
        slidesToShow: 2,
      }
    },  
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
      }
    }
  ]
  });


  //==================== Special product slider ====================//
  $('.specialproductslider').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  arrows: true,
  appendArrows: '.specialprod-arrow',
  dots: false
  });

    //==================== Special product slider ====================//
  $('.specialproductslider-index3').slick({
  slidesToShow: 2,
  slidesToScroll: 1,
  arrows: true,
  appendArrows: '.specialprod-arrow',
  dots: false,
   responsive: [
    {
      breakpoint: 991,
      settings: {
        slidesToShow: 2,
      }
    },  
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
      }
    }
  ]
  });


  //==================== Related Product slider ====================//
  $('.relatedproduct-slider').slick({
  slidesToShow: 3,
  slidesToScroll: 1,
  arrows: true,
  appendArrows: '.relatedprod-arrow',
  dots: false,
  responsive: [
    {
      breakpoint: 1200,
      settings: {
        slidesToShow: 3,
      }
    },  
    {
      breakpoint: 991,
      settings: {
        slidesToShow: 2,
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1
      }
    } 
  ]
  });


  //==================== Brand logo slider ====================//
  $('.brand-slider').slick({
  infinite: true,
  slidesToShow: 4,
  slidesToScroll: 1,
  autoplay: true,
  arrows: false,
  responsive: [
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 4
      }
    },
    {
      breakpoint: 600,
      settings: {
        slidesToShow: 3
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 2
      }
    }
  ]
});  



//==================== Brand logo slider ====================//
  $('.brand-slider-index3').slick({
  infinite: true,
  slidesToShow: 2,
  slidesToScroll: 1,
  autoplay: true,
  arrows: false,
  rows:2,
  responsive: [
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 2
      }
    },
    {
      breakpoint: 991,
      settings: {
        slidesToShow: 3
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 2
      }
    }
  ]
});  

//==================== Instagram slider ====================//
$('.insta-slider').slick({
infinite: true,
slidesToShow: 5,
slidesToScroll: 1,
autoplay: true,
arrows: false,
responsive: [
  {
    breakpoint: 1024,
    settings: {
      slidesToShow: 4
    }
  },
  {
    breakpoint: 600,
    settings: {
      slidesToShow: 3
    }
  },
  {
    breakpoint: 480,
    settings: {
      slidesToShow: 2
    }
  }
]
}); 


  //==================== Product Zoom & Slider====================//
   $('.main-product-image').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: false,
    fade: true,
    dots: false,
    asNavFor: '.product-thumbnails'
  });

  $('.product-thumbnails').slick({
    slidesToShow: 4,
    slidesToScroll: 1,
    asNavFor: '.main-product-image',
    dots: false,
    arrows: false,
    focusOnSelect: true
  });

  $('.thumbnails').zoom({ on:'click' });


  // debounce so filtering doesn't happen every millisecond
  function debounce( fn, threshold ) {
    var timeout;
    return function debounced() {
      if ( timeout ) {
        clearTimeout( timeout );
      }
      function delayed() {
        fn();
        timeout = null;
      }
      timeout = setTimeout( delayed, threshold || 100 );
    }
  }

  $(window).bind("load", function() {
    $('#all').click();
  });


  //==================== scrol to top button ====================//
  $(window).on("scroll", function() {
    if ($(this).scrollTop() > 200) {
        $(".scroll-to-top").fadeIn(200);
    } else {
        $(".scroll-to-top").fadeOut(200);
    }
  });

  $(".scroll-to-top").on("click", function(event) {
    event.preventDefault();
    $("html, body").animate({scrollTop: 0}, 800);
  });



  //==================== Countdown ====================//
  $('.count').each(function () {
    $(this).prop('Counter',0).animate({
        Counter: $(this).text()
    }, {
        duration: 4000,
        easing: 'swing',
        step: function (now) {
            $(this).text(Math.ceil(now));
        }
    });

});

    //==================== Newsletter popup window ====================//
    $("#newsletter-popup").modal('show');

   //==================== Color Selector ====================//
    $(".color-selector li").click(function(){
        $(this).addClass('active').siblings().removeClass('active');
    });
    
   //==================== Category view ====================//  
    //list layout view
    $('.list-layout-view').on('click', function(e) {
        $(this).addClass('active').siblings().removeClass('active');
        $('.category-main').addClass("list-view");
        $(".category-main .right-column .left-bottom-space").addClass("full");
        $(".category-main .right-column .left-bottom-space .product-single").addClass("d-flex");
        $(".category-main .right-column .left-bottom-space .blog-description").css('display', 'block');
        setTimeout(function(){
            $(".category-main").css("opacity","1");
        }, 500);
    });
   //grid layout view
    $('.grid-layout-view').on('click', function(e) {
        $(this).addClass('active').siblings().removeClass('active');
        $('.category-main').removeClass("list-view");
        $(".category-main .right-column .left-bottom-space").removeClass("full");
        $(".category-main .right-column .left-bottom-space .product-single").removeClass("d-flex");
        $(".category-main .right-column .left-bottom-space .blog-description").css('display', 'none');
    });


 //=============== verticle toggle ===================//

  $('.verticle-menu .sub-menu ul,.left-categories .sub-menu ul').hide();
  $(".verticle-menu .sub-menu a,.left-categories .sub-menu a").click(function () {
    $(this).parent(".verticle-menu .sub-menu,.left-categories .sub-menu").children("ul").slideToggle("100");
    $(this).find(".right").toggleClass("fa-plus fa-minus");
  });


    //==================== Theme Features ====================//
    $('.theme-feature button').on('click', function(){
      $('.theme-feature').toggleClass('open');
    });


    $(".theme-colors li").click(function(){
        $(this).addClass('active').siblings().removeClass('active');
    });


    //==================== light-dark mode ====================//
    var body_theme_version = $("body");
    body_theme_version.on("click", ".dark-vesion" , function(){
        $(this).toggleClass('dark');
        $('.size-box.light').removeClass("light");
        $('body').removeClass('dark');
        if($('.dark-vesion').hasClass('dark')){
            $('body').addClass('dark');

        }
        return false;
    });
    body_theme_version.on("click", ".light-vesion" , function(){
        $(this).addClass('light');
        $('.size-box.dark').removeClass("dark");
        $('body').removeClass('dark');
        return false;
    });


   //==================== color option ====================//
    // chnage color
    $(".color1").click(function(){
      $(".theme-colors .colorchange").removeClass("active");
      $(".color1").addClass("active");
      document.documentElement.style.setProperty('--main-bg-color', '#f04f00');
    });

    $(".color2").click(function(){
      $(".theme-colors .colorchange").removeClass("active");
      $(".color2").addClass("active");
      document.documentElement.style.setProperty('--main-bg-color', '#373d94');
    });

    $(".color3").click(function(){
      $(".theme-colors .colorchange").removeClass("active");
      $(".color3").addClass("active");
      document.documentElement.style.setProperty('--main-bg-color', '#e4604a');
    });

    $(".color4").click(function(){
      $(".theme-colors .colorchange").removeClass("active");
      $(".color4").addClass("active");
      document.documentElement.style.setProperty('--main-bg-color', '#cc0000');
    });

    $(".color5").click(function(){
      $(".theme-colors .colorchange").removeClass("active");
      $(".color5").addClass("active");
      document.documentElement.style.setProperty('--main-bg-color', '#dc457e');
    });

    $(".color6").click(function(){
      $(".theme-colors .colorchange").removeClass("active");
      $(".color6").addClass("active");
      document.documentElement.style.setProperty('--main-bg-color', '#1b7ed1');
    });

    $(".color7").click(function(){
      $(".theme-colors .colorchange").removeClass("active");
      $(".color7").addClass("active");
      document.documentElement.style.setProperty('--main-bg-color', '#d4b196');
    });

    $(".color8").click(function(){
      $(".theme-colors .colorchange").removeClass("active");
      $(".color8").addClass("active");
      document.documentElement.style.setProperty('--main-bg-color', '#f0b54d');
    });

    $(".color9").click(function(){
      $(".theme-colors .colorchange").removeClass("active");
      $(".color9").addClass("active");
      document.documentElement.style.setProperty('--main-bg-color', '#6d7e87');
    });

    $(".color10").click(function(){
      $(".theme-colors .colorchange").removeClass("active");
      $(".color10").addClass("active");
      document.documentElement.style.setProperty('--main-bg-color', '#3fdda7');
    });



})(jQuery);