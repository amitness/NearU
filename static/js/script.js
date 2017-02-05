$(function() {

	$('#submitmsg').click(function() {
		
		var userMessage = $('#usermsg').val(); 
		userMessage = userMessage.replace(/</g, '&lt;');
		var box = '<li class="collection-item avatar"><i class="material-icons circle blue">perm_identity</i><span class="title">'+ userMessage + '</span></li>'
		var bot = '<li class="collection-item avatar"><i class="material-icons circle green">navigation</i><span class="title">';
		var bot_end = '</span></li>';
		

		$('.conversation').append(box);
	    	$.ajax({
            url: '/response',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
            	console.log(response);
                reply = bot + response['text'] + bot_end;
                $('.conversation').append(reply);
            },
            error: function(error) {
                console.log(error);
            }
        });
		//$('.conversation').append(bot);
		// $.getJSON('/message', {
		// 	clientmsg: userMessage
		// }, function(data) {
		// 	$('.conversation').append('<li class="bot"><span class="avatar"><img src="static/ambulance.png"/></span><div class="message">' + data.result + '</div></li>');
		// });
		
		// Empty the text in input box
		$('#userMessage').val(""); 
		
		return false;	
	});
});
