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
});


/* 
Modal
*/
setTimeout(() => {
	$(".alert").slideUp(2000);
}, 4000);
