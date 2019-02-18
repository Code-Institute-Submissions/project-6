/* 
Nav
*/

$(function() {
	$("#user-messages").click(function() {
		$("#user-messages-modal").slideToggle(1000);
		$(".navbar").addClass("white-nav");
		$(".navbar-brand span").fadeIn();
	});
});

/* 
Get messages 
*/

$(function() {
	(function messages_poll() {
		setTimeout(function() {
			$.ajax({
				type: "GET",
				url: `/enquiries/get_messages/`,
				success: function(data) {
					let messages = sort_messages(data);
					inner_messages(messages);
				},
				dataType: "json",
				complete: messages_poll,
				error: function(xhr) {
					console.log(xhr);
				}
			});
			$(".loader").slideUp();
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
			unread_messages.push(data[i]);
		} else {
			read_messages.push(data[i]);
		}
	}
	return {
		unread_messages: unread_messages,
		read_messages: read_messages
	};
}

/* 
Inner messages if any
*/

function inner_messages(messages) {
	let unread_m = messages.unread_messages;
	let read_m = messages.read_messages;
	let unread_ids = $("input[name=unread_messages_id]").val();
	let read_ids = $("input[name=read_messages_id]").val();
	if (unread_m.length == 0) {
		$("#user-messages button").html(`
		<i class="fas fa-envelope fa-fw"></i>
		<i class="fas fa-caret-down"></i>
	`);
	} else {
		$("#user-messages button").html(`
			<i class="fas fa-envelope fa-fw"></i>
			<span class="badge badge-danger">${unread_m.length}</span>
			<i class="fas fa-caret-down"></i>
		`);		
	}
	if (unread_m.length > 0) {
		let splited_ids = unread_ids.split(",");
		if (splited_ids.length == 2) {
			for (let i = 0; i < unread_m.length; i++) {
				message_template(
					"#unread-message-inner",
					unread_m[i].fields,
					unread_m[i].pk
				);
				unread_ids = unread_ids + unread_m[i].pk + ",";
				$("input[name=unread_messages_id]").val(unread_ids);
			}
		} else {
			for (let i = 0; i < unread_m.length; i++) {
				if ($.inArray(unread_m[i].pk.toString(), splited_ids) == -1) {
					message_template(
						"#unread-message-inner",
						unread_m[i].fields,
						unread_m[i].pk
					);
					unread_ids = unread_ids + unread_m[i].pk + ",";
					$("input[name=unread_messages_id]").val(unread_ids);
				}
			}
		}
	} else {
		$('#unread-message-inner').html(`
			<div class="col-12 loader">
					<div class="row justify-content-center py-5">
						<i class="fas fa-check fa-10x text-secondary"></i>
						<h4 class="col-12 text-center font-weight-bold py-3">No messages...</h4>
					</div>
				</div>
		`)
	}

	if (read_m.length > 0) {
		let splited_ids = read_ids.split(",");
		if (splited_ids.length == 2) {
			for (let i = 0; i < read_m.length; i++) {
				message_template("#read-message-inner", read_m[i].fields, read_m[i].pk);
				read_ids = read_ids + read_m[i].pk + ",";
				$("input[name=read_messages_id]").val(read_ids);
			}
		} else {
			for (let i = 0; i < read_m.length; i++) {
				if ($.inArray(read_m[i].pk.toString(), splited_ids) == -1) {
					message_template(
						"#read-message-inner",
						read_m[i].fields,
						read_m[i].pk
					);
					read_ids = read_ids + read_m[i].pk + ",";
					$("input[name=read_messages_id]").val(read_ids);
				}
			}
		}
	} else {
		$('#read-message-inner').html(`
			<div class="col-12 loader">
					<div class="row justify-content-center py-5">
						<i class="fas fa-check fa-10x text-secondary"></i>
						<h4 class="col-12 text-center font-weight-bold py-3">No messages...</h4>
					</div>
				</div>
		`)
	}
}

/* 
Expand messages
*/

function expand_message(btn) {
	$(btn)
		.parent()
		.parent()
		.next()
		.slideToggle();
}
/* 
Switch between read nad unread messages
*/

$("#unread-message-h5").click(function() {
	activate();
});

$("#read-message-h5").click(function() {
	activate();
});

function activate() {
	$("#unread-message-inner").slideToggle();
	$("#read-message-inner").slideToggle();
	$("#unread-message-h5").toggleClass("text-success");
	$("#read-message-h5").toggleClass("text-success");
	$("#unread-message-h5").toggleClass("text-secondary");
	$("#read-message-h5").toggleClass("text-secondary");
}

/* 
Delete message modal
*/

function create_delete_btn_url(target) {
	let base_url = "/enquiries/delete_message/";
	let url = base_url + target;
	$("#delete-message-modal .modal-footer").append(`
		<button onclick="delete_message('${url}')" type="button" class="btn btn-danger">Delete</button>
		<button type="button" class="btn btn-secondary" data-dismiss="modal">Back</button>
	`);
	toggle_modal("#delete-message-modal");
}

function delete_message(target) {
	$("#delete-message-modal .modal-footer .btn").attr("disabled", "disabled");
	$.ajax({
		type: "DELETE",
		url: target,
		data: {},
		beforeSend: function (xhr) {
			xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
		},
		success: function (data) {
			if (data) {
				let p_data = JSON.parse(data)
				let message_id = "#message-" + p_data[0].pk.toString();
				$(message_id).slideUp();
				toggle_modal("#delete-message-modal");
				$("#delete-message-modal .modal-footer").empty();
				js_alerts("success", "Message deleted!");
			}
		},
		error: function (xhr) {
			console.log(xhr);
		}
	});
}



/*
Reply message
*/

function reply_message(btn) {
	$(btn).parent().html(`
	`)
}

/* 

Templates

*/

/* 
Message template
*/

function message_template(target, message, message_id) {
	let m = message;
	$(target).append(`
		<div id="message-${message_id}" class="col-12">
			<div class="row pb-3 justify-content-around">
				<div class="col-md-10 mr-1 card bg-transparent border-0">
					<div class="row card-header border-0 bg-light pb-3 pb-lg-4 text-secondary">
						<div class="my-3 col-5 font-weight-bold">
							<p>
								<i class="fas fa-calendar-alt"></i> ${m.posted}
							</p>
							<p>
								<i class="fas fa-pencil-alt"></i> Enquire
							</p>
						</div>
						<div class="my-3 col-7 font-weight-bold">
							<p>
								<i class="fas fa-user-friends"></i> ${m.sender}
							</p>
							<p class="mb-3">
								<i class="fas fa-home"></i> ${m.house_name}
							</p>
						</div>
						<a class="dropdown-message-delete">
							<button class="btn btn-outline-secondary" type="button" 
							onclick="create_delete_btn_url('${m.to_id}/${message_id}')">
								<i class="fas fa-trash"></i>
							</button>
						</a>
						<div class="dropdown-message-btn">
							<button onclick="expand_message(this)" class="btn btn-secondary "type="button">
								<i class="fas fa-eye"></i>
								<i class="fas fa-caret-down"></i>
							</button>
						</div>
					</div>
					<div class="row card-body">
						<div class="col-12 pt-5">
							<h6 class="text-success text-capitalize">${m.sender}</h6>
							<hr>
							<pre>${m.message}</pre>
						</div>
						<div class="col-12 pt-5 text-right">
							<button onclick="reply_message(this)" class="btn btn-secondary" type="button">
								<i class="fas fa-reply"></i>
							</button>
							${reply_message_form(m)}
						</div>
					</div>
					<div>
						
					</div>
				</div>
			</div>
		</div>	
	`);
}


/*
Reply message form
*/

function reply_message_form(m) {
	return `
		<div class="row justify-content-center">
			<form method="POST" action="/enquiries/send_enquire/${m.to_id}/${m.house_id}" class="col-12">
				<input type="hidden" name="csrfmiddlewaretoken" value="${$.cookie('csrftoken')}">
				<div class="form-group">
					<label class="sr-only" for="id_message">Message
					</label>
					<textarea name="message" cols="40" rows="10" minlength="15" class="form-control" placeholder="Message" title="" required="" id="id_message">
					</textarea>
				</div>
				<div class="form-group text-center">
					<button type="submit" class="btn btn-success">Reply</button>
				</div>
				<input type="hidden" name="to" value="${m.sender}">
				<input type="hidden" name="to_id" value="${m.sender_id}">
				<input type="hidden" name="to_email" value="${m.sender_email}">
				<input type="hidden" name="house_id" value="${m.house_id}">
				<input type="hidden" name="house_name" value="${m.house_name}">
				<input type="hidden" name="sender" value="${m.to}">
				<input type="hidden" name="sender_id" value="${m.to_id}">
				<input type="hidden" name="sender_email" value="${m.to_email}">	
			</form>
		</div>
	`
}
