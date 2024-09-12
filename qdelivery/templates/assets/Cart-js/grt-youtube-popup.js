 /*!
         * GRT Youtube Popup - jQuery Plugin
         * Version: 2.0.0
         * Author: GRT107
         *
         * Copyright (c) 2024 GRT107
         * Released under the MIT license
         */

 (function ($) {

	$.fn.grtyoutube = function (options) {

		return this.each(function () {

			// Get video ID
			var getvideoid = $(this).data("youtube-id");

			// Default options
			var settings = $.extend({
				videoID: getvideoid,
				autoPlay: true,
				theme: "dark"
			}, options);

			// Convert some values
			settings.autoPlay = settings.autoPlay ? 1 : 0;
			settings.theme = settings.theme === "light" ? "grtyoutube-light-theme" : "grtyoutube-dark-theme";

			// Initialize on click
			if (settings.videoID) {
				$(this).on("click", function () {
					$("body").append('<div class="grtyoutube-popup ' + settings.theme + '">' +
						'<div class="grtyoutube-popup-content">' +
						'<span class="grtyoutube-popup-close"></span>' +
						'<iframe class="grtyoutube-iframe" src="https://www.youtube.com/embed/' + settings.videoID + '?rel=0&wmode=transparent&autoplay=' + settings.autoPlay + '&iv_load_policy=3" frameborder="0" allow="autoplay; fullscreen"></iframe>' +
						'</div>' +
						'</div>');
				});
			}

			// Close the box on click or escape
			$(this).on('click', function (event) {
				event.preventDefault();
				$(".grtyoutube-popup-close, .grtyoutube-popup").click(function () {
					$(".grtyoutube-popup").remove();
				});
			});

			$(document).keyup(function (event) {
				if (event.keyCode == 27) {
					$(".grtyoutube-popup").remove();
				}
			});
		});
	};

}(jQuery));