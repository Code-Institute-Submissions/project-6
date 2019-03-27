/*
Nav
*/

$(document).ready(function() {
	if ($(document).scrollTop() >= 400) {
		$(".navbar").addClass("white-nav");
		$(".navbar-brand span").fadeIn();
	}
	$(document).scroll(function() {
		if ($(document).scrollTop() >= 400) {
			$(".navbar").addClass("white-nav");
			$(".navbar-brand span").fadeIn();
		}
	});
	$(".navbar-toggler").click(function() {
		$(".navbar").addClass("white-nav");
		$(".navbar-brand span").fadeIn();
	});
	if ($(window).width() >= 1200) {
		$(".footer-links .fab").hover(function () {
			$(".fa-twitter").toggleClass("twitter");
			$(".fa-facebook-f").toggleClass("facebook");
			$(".fa-linkedin-in").toggleClass("linkedin");
			$(".fa-instagram").toggleClass("instagram");
		});
	};
});

/* 
Modal
*/
setTimeout(() => {
	$(".alert").slideUp(2000);
}, 4000);

function toggle_modal(target) {
	$(target).modal("toggle");
}

function js_alerts(css_class="light", message) {
	$(".alert").html(`
		<p class="text-${css_class}">${message}</p>
	`);
	$(".alert").fadeIn(1000);
	$("#js-alerts").fadeIn(1500);
	setTimeout(() => {
		$("#js-alerts").slideUp(2000);
	}, 4000);
}
