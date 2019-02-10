
/* 
Nav
*/

$(function () {
	$("#user-messages").click(function() {
		$("#user-messages-modal").slideToggle(1000);
		$(".navbar").addClass("white-nav");
		$(".navbar-brand span").fadeIn();
	});
});

/* 
Get messages 
*/


$(function () {	
	(function messages_poll() {
		setTimeout(function () {
			$.ajax({
				type: "GET",
				url: `/enquiries/get_messages/`,
				success: function (data) {
					let messages = sort_messages(data);
					console.log(data);
					inner_messages(messages);
				},
				dataType: "json",
				complete: messages_poll,
				error: function name(xhr) {
					console.log(xhr);
				}
			});
		}, 3000);
	})();
});

/* 
Sort messages
*/

function sort_messages(data) {
	let unread_messages = [];
	let read_messages = [];
	for (let i = 0; i < data.length; i++) {
		if (data[i].fields.new_message == true) {
			unread_messages.push(data[i].fields);
		} else {
			read_messages.push(data[i].fields);
		}
	}
	return {
		"unread_messages": unread_messages,
		"read_messages": read_messages,
	}
}

/* 
Inner messages if any
*/

function inner_messages(messages) {
	if (messages.unread_messages.length > 0) {
		$("#user-messages button").html(`
			<i class="fas fa-envelope fa-fw"></i>
			<span class="badge badge-danger">${messages.unread_messages.length}</span>
		`);
	} else {
		$("#user-messages button").html(`
			<i class="fas fa-envelope fa-fw"></i>
		`);
	}
}