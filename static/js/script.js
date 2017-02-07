$(function() {

	$('#submitmsg').click(function() {
		
		var userMessage = $('#usermsg').val(); 
		console.log(userMessage);
		userMessage = userMessage.replace(/</g, '&lt;');

		var sentMessage='<div class="chat-message clearfix"><img src="static/img/user.png" alt="" width="32" height="32"><div class="chat-message-content clearfix"><h5>User</h5><p>' + userMessage + '</p></div></div><hr>';
		
		var botMessage='<div class="chat-message clearfix"><img src="static/img/nearu.png" alt="" width="32" height="32"><div class="chat-message-content clearfix"><h5>NearU</h5><p>';
		var botEnd = '</p></div></div><hr>';

		$('.chat-history').append(sentMessage);

    	$.ajax({
        url: '/response',
        data: $('form').serialize(),
        type: 'POST',
        success: function(response) {
        	var replyMessage = 'Not found text.';
        	console.log(response);
            if(response.hasResults) {
            	replyMessage = response.botReply;
            	var places = response.results;
            	if(places.length !== 0) {
            		for(var i = 0; i < places.length; i++) {
            			addPinpoint(places[i]);
            		}
            	}
            }

        	reply = botMessage + replyMessage + botEnd;
            $('.chat-history').append(reply);

    		// Scroll down the chat history to latest message
	        var elem = document.getElementById('chatHist');
			elem.scrollTop = elem.scrollHeight;
        },
        error: function(error) {
            console.log(error);
        }
    });

		// Empty the text in input box
		$('#usermsg').val(""); 

		return false;	
	});
});


function addPinpoint(place) {
	// Adds a pinpoint to Leafleft map
	L.marker([place.lat, place.long])
	.addTo(mymap)
	.bindPopup(generateDetails(place), {className: 'card'});	
}

function generateDetails(place) {
   return "<div class='card--small'><div class='card__image' style='background-image: url(https://placeimg.com/640/480/nature)'></div><h2 class='card__title'>" + place.title + "</h2><span class='card__subtitle'>" + place.desc + "</span><div class='card__action-bar'><a href='#'><button class='card__button button_sliding_bg'>SEE MORE</button></a></div>";
}


(function() {

  $('#live-chat header').on('click', function() {
    $('.chat').slideToggle(300, 'swing');
    $('.chat-message-counter').fadeToggle(300, 'swing');

  });
}) ();