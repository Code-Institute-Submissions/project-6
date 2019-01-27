/*
Nav
*/

$(document).ready(function() {
	$(document).scroll(function() {
		if ($(document).scrollTop() >= 400) {
			$(".navbar").addClass("white-nav");
		} else {
			$(".navbar").removeClass("white-nav");
		}
	});
	$("#nav .container").hover(function() {
			$(".navbar-brand span").fadeIn();
		}, function() {
			$(".navbar-brand span").fadeOut();
		});
});

/* 
Modal
*/
setTimeout(() => {
	$(".alert").slideUp(2000);
}, 4000);
