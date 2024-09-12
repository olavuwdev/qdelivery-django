// Template Name: Lunch Box
// Version: 1.0.0
// Author: Webstrot 


/************ TABLE OF CONTENTS ***************

  01. preloader js
  02. owlCarousel js
  03. Outer height js
  04. Element rotated on scroll js
  05. Header Scroll js
  06. Mouse Animation 
  07. Mouse Animation 
  08. Dropdown js
  09. Mobile menu toggle js

**********************************************/

// preloader js
$(window).on('load', function () {
  $("#status").fadeOut();
  $("#preloader").delay(450).fadeOut("slow");
});

// owlCarousel js
$('.clientsSaySlider').owlCarousel({
  loop: false,
  items: 1,
  margin: 10,
  responsiveClass: true,
  dots: false,
  nav: true,
})

$('.trustedUsersCarousel').owlCarousel({
  loop: true,
  margin: 10,
  nav: false,
  dots: false,
  autoplay: true,
  autoplayTimeout: 1500,
  autoplayHoverPause: true,
  smartSpeed: 500,
  animateOut: 'fadeOut',
  animateIn: 'fadeIn',
  responsiveClass: true,
  responsive: {
    0: {
      items: 1,
    },
    450: {
      items: 2,
    },
    767: {
      items: 3,
    },
    768: {
      items: 4,
    },
    992: {
      items: 5,
    }
  }
})

// Outer height js
$(document).ready(function ($) {
  // Function to be executed on document ready and window resize
  function adjustOnResize() {
    var windowWidth = $(window).width();

    if (windowWidth <= 991) {
      var topHeaderHeight = $('.header').outerHeight();
  
      $('.header #collapsibleNavbar').css('top', topHeaderHeight);
      var newHeight = 'calc(100vh - ' + topHeaderHeight + 'px)';
      $('.header #collapsibleNavbar').css('height', newHeight);
      $('.lunchboxSidebar').css('top', topHeaderHeight);
      var newHeight = 'calc(100vh - ' + topHeaderHeight + 'px)';
      $('.lunchboxSidebar').css('height', newHeight);

    } else {
      // Reset styles if window width is greater than 1199 pixels
      $('.header #collapsibleNavbar').css('top', '');
      $('.header #collapsibleNavbar').css('height', '');
      $('.lunchboxSidebar').css('top', '');
      $('.lunchboxSidebar').css('height', '');

    }
  }

  // Initial adjustment on document ready
  adjustOnResize();

  // Bind adjustOnResize function to the window resize event
  $(window).resize(function () {
    adjustOnResize();
  });
});
$(document).ready(function() {
  $('a[data-bs-toggle="pill"]').on('shown.bs.tab', function (e) {
      var targetTab = $(e.target).attr("href"); // activated tab
      var topReviewBoxHeight = $(targetTab).find('.reviewStar').outerHeight();
      $(targetTab).find('.reviewComment').css('height', topReviewBoxHeight);
  });
});
// Mobile menu toggle js
$(document).ready(function () {
  $('#nav-icon2').click(function () {
    $(this).toggleClass('open');
  });
  $('.blogFilterIcon').click(function () {
    $('.lunchboxSidebar').toggleClass('active');
  });
  $('.blogFilterCloseIcon').click(function () {
    $('.lunchboxSidebar').toggleClass('active');
  });
});

// Element rotated on scroll js
window.addEventListener(
  "scroll",
  () => {
    document.body.style.setProperty(
      "--scroll",
      window.pageYOffset / (document.body.offsetHeight - window.innerHeight)
    );
  },
  false
);


// Header Scroll js
$(document).ready(function () {
  const header = $(".header");
  const toggleClass = "headerActive";

  // Check if there's a saved scroll position in localStorage
  const savedScrollPosition = localStorage.getItem("scrollPosition");

  if (savedScrollPosition && parseInt(savedScrollPosition) > 150) {
    header.addClass(toggleClass);
  }

  $(window).scroll(function () {
    const currentScroll = $(window).scrollTop();
    if (currentScroll > 150) {
      header.addClass(toggleClass);
    } else {
      header.removeClass(toggleClass);
    }

    // Save the current scroll position in localStorage
    localStorage.setItem("scrollPosition", currentScroll.toString());
  });
});



// Mouse Animation 
document.addEventListener("mousemove", parallax);
function parallax(e) {
  document.querySelectorAll(".movingjs").forEach(function (move) {
    var moving_value = move.getAttribute("data-value");

    var x = (e.clientX * moving_value) / 250;
    var y = (e.clientY * moving_value) / 250;

    move.style.transform = "translateX(" + x + "px) translateY(" + y + "px)";
  });
}


// Dropdown js
$(document).ready(function () {
  $('.dropdown').on('show.bs.dropdown', function (e) {
    $(this).find('.dropdown-menu').first().stop(true, true).slideDown(300);
  });
  $('.dropdown').on('hide.bs.dropdown', function (e) {
    $(this).find('.dropdown-menu').first().stop(true, true).slideUp(200);
  });

  $(".navbar-nav .dropdown").hover(
    function () {
      $('.dropdown-menu', this).not('.in .dropdown-menu').stop(true, true).slideDown("400");
      $(this).toggleClass('open');
    },
    function () {
      $('.dropdown-menu', this).not('.in .dropdown-menu').stop(true, true).slideUp("400");
      $(this).toggleClass('open');
    }
  );
});

// Quantity increase/decrease js
document.addEventListener('DOMContentLoaded', function () {
  var quantityInputs = document.querySelectorAll('.quantity');
  var increaseButtons = document.querySelectorAll('.increase');
  var decreaseButtons = document.querySelectorAll('.decrease');

  increaseButtons.forEach(function (button, index) {
    button.addEventListener('click', function () {
      var currentValue = parseInt(quantityInputs[index].value);
      quantityInputs[index].value = currentValue + 1;
    });
  });

  decreaseButtons.forEach(function (button, index) {
    button.addEventListener('click', function () {
      var currentValue = parseInt(quantityInputs[index].value);
      if (currentValue > 1) {
        quantityInputs[index].value = currentValue - 1;
      }
    });
  });
});

// search js
$(".search, .searchBoxClose").click(function(){
  $(".searchBox").toggleClass("active");
});
$(".ourMealWishlist").click(function(){
  $(this).toggleClass("active");
});




$(document).ready(function() {
  var lunchboxSidebar = $('.lunchboxSidebar');
  var header = $('.header');
  var headerHeight = header.outerHeight();
  var additionalTop = 20; // Adjust this value as needed

  // Check the screen width before applying sticky behavior
  if ($(window).width() >= 992) {
      // Check the scroll position on page load
      var scrollPosition = $(window).scrollTop();
      if (scrollPosition > headerHeight) {
          lunchboxSidebar.css('top', headerHeight + additionalTop + 'px').addClass('sticky');
      }

      // Add scroll event listener
      $(window).scroll(function() {
          scrollPosition = $(window).scrollTop();

          // Adjust the threshold value as needed
          if (scrollPosition > headerHeight) {
              lunchboxSidebar.css('top', headerHeight + additionalTop + 'px').addClass('sticky');
          } else {
              lunchboxSidebar.css('top', '0').removeClass('sticky');
          }
      });
  }
});




