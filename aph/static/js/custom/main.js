/*
Nav
*/

$(document).ready(function() {
	$(document).scroll(function() {
		if ($(document).scrollTop() >= 400) {
			$(".navbar").addClass("white-nav");
			$(".navbar-brand span").fadeIn();
		} else {
			$(".navbar").removeClass("white-nav");
			$(".navbar-brand span").fadeOut();
		}
	});
});

/* 
Modal
*/
setTimeout(() => {
	$(".alert").slideUp(2000);
}, 4000);
