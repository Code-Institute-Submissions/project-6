/* 
Nav
*/

$(function() {
	$("#user-messages").click(function() {
		$("#message-inner .card-body").slideUp();
		$("#message-inner .fa-caret-up")
			.parent()
			.parent()
			.html(
				`
			<button onclick="expand_message(this)" class="btn btn-secondary "type="button">
				<i class="fas fa-eye"></i>
				<i class="fas fa-caret-down"></i>
			</button>
			`
			);
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
					let conversations = new Conversations(data);
					return conversations.create_conversations();
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
Class for creating conversations for user 
*/

class Conversations {
	constructor(data) {
		this.json = data;
		this.user_id = parseInt($("input[name=user_id]").val());
		this.conversations_id = $("input[name=conversations_id]")
			.val()
			.split(",");
	}
	parseData = function() {
		let parsedData = [];
		this.json.forEach(ele => {
			parsedData.push(JSON.parse(ele));
		});
		if (parsedData) {
			return parsedData;
		} else {
			return [];
		}
	};

	is_sender = function(conversation) {
		if (this.user_id == conversation.sender_id) {
			return true;
		} else {
			return false;
		}
	};

	sort_conversations = function() {
		let new_conversations = [];
		let old_conversations = [];
		let conversations = this.parseData();
		for (let i = 0; i < conversations.length; i++) {
			for (let z = 0; z < conversations[i].length; z++) {				
				let message = conversations[i][z].fields;
				if (this.user_id == message.to_id && message.new_to) {
					new_conversations.push(conversations[i]);
					break;
				}
				if (z == conversations[i].length - 1) {
					old_conversations.push(conversations[i]);
				}
			}
		}
		return {
			new_conversations: new_conversations,
			old_conversations: old_conversations
		};
	};
	nav_btn = function(counter) {
		if (counter == 0) {
			$("#user-messages button").html(`
			<i class="fas fa-envelope fa-fw"></i>
			<i class="fas fa-caret-down"></i>
		`);
		} else {
			$("#user-messages button").html(`
			<i class="fas fa-envelope fa-fw"></i>
			<span class="badge badge-danger">${
				this.sort_conversations().new_conversations.length
			}</span>
			<i class="fas fa-caret-down"></i>
		`);
		}
	};
	no_conversations = function() {
		$("#message-inner").html(`
		<div class="col-12 loader">
				<div class="row justify-content-center py-5">
					<i class="fas fa-check fa-10x text-secondary"></i>
					<h4 class="col-12 text-center font-weight-bold py-3">No conversations...</h4>
				</div>
			</div>
	`);
	};
	create_conversations = function() {
		if (this.json.length == 0) {
			this.nav_btn(0);
			this.no_conversations();
		} else {
			if (this.sort_conversations().new_conversations.length == 0) {
				this.nav_btn(0);
			} else {
				this.nav_btn(this.sort_conversations().new_conversations.length);
			}
			let c = this.sort_conversations();
			for (let i = 0; i < c.new_conversations.length; i++) {
				if (
					$.inArray(
						c.new_conversations[i][0].pk.toString(),
						this.conversations_id
					) == -1
				) {
					new Templates(c.new_conversations[i], true).message_template();
					this.conversations_id += c.new_conversations[i][0].pk + ",";
					$("input[name=conversations_id]").val(this.conversations_id);
				}
			}
			for (let i = 0; i < c.old_conversations.length; i++) {
				if (
					$.inArray(
						c.old_conversations[i][0].pk.toString(),
						this.conversations_id
					) == -1
				) {
					new Templates(c.old_conversations[i], false).message_template();
					this.conversations_id += c.old_conversations[i][0].pk + ",";
					$("input[name=conversations_id]").val(this.conversations_id);
				}
			}
		}
	};
}

/* 
Class for innering conversarions Header / Messages / Reply form
*/
class Templates {
	constructor(conversation, new_conversation) {
		this.conversation = conversation;		
		this.text_color = function() {
			if (new_conversation != true) {
				return "text-secondary";
			} else {
				return "";
			}
		};
		this.eye_btn_color = function () {
			if (new_conversation == true) {
				return "btn-success";
			} else {
				return "btn-secondary";
			}
		};
	}
	message_template() {
		let user_id = parseInt($("input[name=user_id]").val());
		let header_data = this.conversation[0].fields;
		let message_id = this.conversation[0].pk;
		function posted() {
			let data = header_data.posted;
			data = new Date(data);
			data = data.toLocaleDateString("en-UK");
			return data;
		}
		function conversation_member () {
			if (user_id == header_data.to_id) {
				return header_data.sender_id
			} else {
				return header_data.to_id
			}
		}
		$("#message-inner").append(`
		<div id="message-${message_id}" class="col-12">
			<div class="row pb-3 justify-content-around">
				<div class="col-md-10 mr-1 card bg-transparent border-0">
					<div class="row card-header border-0 bg-light pb-3 pb-lg-4 ${this.text_color()}">
						<div class="my-3 col-5 font-weight-bold">
							<p>
								<i class="fas fa-calendar-alt"></i> ${posted()}
							</p>
							<p>
								<i class="fas fa-pencil-alt"></i> Enquire
							</p>
						</div>
						<div class="my-3 col-7 font-weight-bold">
							<p>
								<i class="fas fa-user-friends"></i> ${header_data.sender}
							</p>
							<p class="mb-3">
								<i class="fas fa-home"></i> ${header_data.house_name}
							</p>
						</div>
						<a class="dropdown-message-delete">
							<button class="btn btn-outline-secondary" type="button" 
							onclick="create_delete_btn_url('${user_id}/${conversation_member()}/${header_data.house_id}')">
								<i class="fas fa-trash"></i>
							</button>
						</a>
						<div class="dropdown-message-btn">
							<button onclick="expand_message(this, '${user_id}/${conversation_member()}/${header_data.house_id}', '#message-${message_id} .d-none')" class="btn  ${this.eye_btn_color()}"type="button">
								<i class="fas fa-eye"></i>
								<i class="fas fa-caret-down"></i>
							</button>
						</div>
					</div>
					<div class="row card-body">
						<div class="container">
							<div class="row">
								<p class="d-none">${this.conversation_template().ids}</p>
								${this.conversation_template().c}
								<div class="col-12 mt-5">
									${this.reply_message_form()}
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>	
	`);
	}
	conversation_template() {
		let conversation = [];
		let messages_ids = []
		for (let i = 0; i < this.conversation.length; i++) {
			let message = `
			<div class="col-12 pt-5">				
				<h5 class="text-success text-capitalize">
				${this.conversation[i].fields.sender} 
				<p class="py-2 text-secondary">
					<i class="fas fa-calendar-alt"></i> ${posted(this.conversation[i].fields)}
				</p>
				</h5>
				<hr>
				<pre>${this.conversation[i].fields.message}</pre>
			</div>
		`;
			conversation += message;
			messages_ids += this.conversation[i].pk + ",";
		}
		function posted(message) {
			var data = message.posted;
			data = new Date(data);
			data = data.toLocaleDateString("en-UK");
			return data;
		}
		return {
			c: conversation,
			ids : messages_ids
		};
	}

	reply_message_form() {
		let m = this.conversation[0].fields;
		let user_id = parseInt($("input[name=user_id]").val());
		if (user_id == m.sender_id) {
			return `
			<div class="row justify-content-center">
			<form method="POST" action="/enquiries/send_enquire/${m.to_id}/${m.house_id}" class="col-12">
				<input type="hidden" name="csrfmiddlewaretoken" value="${$.cookie("csrftoken")}">
				<div class="form-group">
					<label class="sr-only" for="message-${this.conversation[0].pk}">Message
					</label>
					<textarea name="message" cols="40" rows="10" minlength="15" class="form-control" placeholder="Message" required id="message-${this.conversation[0].pk}">
					</textarea>
				</div>
				<div class="form-group text-center">
					<button type="submit" class="btn btn-success">Reply</button>
				</div>
				<input type="hidden" name="to" value="${m.to}">
				<input type="hidden" name="to_id" value="${m.to_id}">
				<input type="hidden" name="to_email" value="${m.to_email}">
				<input type="hidden" name="house_id" value="${m.house_id}">
				<input type="hidden" name="house_name" value="${m.house_name}">
				<input type="hidden" name="sender" value="${m.sender}">
				<input type="hidden" name="sender_id" value="${m.sender_id}">
				<input type="hidden" name="sender_email" value="${m.sender_email}">	
				<input type="checkbox" name="new_to" class="form-check-input d-none" checked>
			</form>
		</div>
			`
		} else {
			return `
			<div class="row justify-content-center">
				<form method="POST" action="/enquiries/send_enquire/${m.to_id}/${m.house_id}" class="col-12">
					<input type="hidden" name="csrfmiddlewaretoken" value="${$.cookie("csrftoken")}">
					<div class="form-group">
						<textarea name="message" cols="40" rows="10" minlength="15" class="form-control" placeholder="Message" required id="message-${this.conversation[0].pk}">
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
					<input type="checkbox" name="new_to" class="form-check-input d-none" checked>
				</form>
			</div>
			`
		};
	} 
}

/* 
Expand messages
*/

function expand_message(btn, url, conversation_id) {
	$("#message-inner .card-body").slideUp();
	$("#message-inner .fa-caret-up")
		.parent()
		.parent()
		.html(
			`
			<button onclick="expand_message(this)" class="btn btn-secondary "type="button">
				<i class="fas fa-eye"></i>
				<i class="fas fa-caret-down"></i>
			</button>
			`
		);
	toggle_read(url, conversation_id)
	setTimeout(() => {
		$(btn)
			.addClass('btn-secondary')
			.removeClass('btn-success')
			.parent()
			.html(
				`
				<button onclick="hide_message(this)" class="btn btn-secondary "type="button">
					<i class="fas fa-eye"></i>
					<i class="fas fa-caret-up"></i>
				</button>
			`
			)
			.parent()
			.addClass("text-secondary")
			.next()
			.slideDown();
	}, 500);
}

/* 
Hide message
*/

function hide_message(btn) {
	$("#message-inner .card-body").slideUp();
	$("#message-inner .fa-caret-up")
		.parent()
		.parent()
		.html(
			`
			<button onclick="expand_message(this)" class="btn btn-secondary "type="button">
				<i class="fas fa-eye"></i>
				<i class="fas fa-caret-down"></i>
			</button>
			`
		);
	setTimeout(() => {
		$(btn)
			.parent()
			.parent()
			.next()
			.slideUp();
	}, 500);
}

/* 
Toggle read
*/

function toggle_read(url_id, conversation_id) {
	let url = `/enquiries/toggle_read/${url_id}`
	let ids = $(conversation_id).text().split(',').slice(0, -1)
	$.ajax({
		type: "POST",
		url: url,
		data: { "ids": ids },
		beforeSend: function (xhr) {
			xhr.setRequestHeader("X-CSRFToken", $.cookie("csrftoken"));
		},
		success: function (data) {
			if (data) {
				console.log(data);
			}
		},
		error: function (xhr) {
			console.log(xhr);
		}
	});
}

/* 
Delete message modal
*/

function create_delete_btn_url(target) {
	let url = `/enquiries/delete_message/${target}`;
	let id = target.split('/')[1];
	$("#delete-message-modal .modal-footer").html(`
		<button onclick="delete_message('${url}', '#message-${id} .d-none')" type="button" class="btn btn-danger">Delete</button>
		<button type="button" class="btn btn-secondary" data-dismiss="modal">Back</button>
	`);
	toggle_modal("#delete-message-modal");
}

function delete_message(url, conversation_id) {
	$("#delete-message-modal .modal-footer .btn").attr("disabled", "disabled");
	let ids = $(conversation_id).text().split(',').slice(0, -1)
	$.ajax({
		type: "POST",
		url: url,
		data: {"ids" : ids},
		beforeSend: function(xhr) {
			xhr.setRequestHeader("X-CSRFToken", $.cookie("csrftoken"));
		},
		success: function(data) {
			if (data) {
				$('#message-inner').html(`
					<div class="col-12 loader">
						<div class="row justify-content-center py-5">
							<i class="fas fa-sync-alt fa-10x text-secondary"></i>
							<h4 class="col-12 text-center font-weight-bold py-3">Updating...</h4>
						</div>				
					</div>
				`);
				toggle_modal("#delete-message-modal");
				$("#delete-message-modal .modal-footer").empty();
			}
		},
		error: function(xhr) {
			console.log(xhr);
		}
	});
}