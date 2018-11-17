/* 
Google maps
*/

function initMap() {
	var companyLocation = { lat: 53.6175516, lng: -1.1434138 };
	var map = new google.maps.Map(document.getElementById("google-map"), {
		zoom: 15,
		center: companyLocation
	});
	var marker = new google.maps.Marker({
		position: companyLocation,
		map: map
	});
}