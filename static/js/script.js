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
        	var dummyLocations = [[27.67933, 85.34634],
        					   	[27.67936, 85.34734]]
        	var coordinates = [];
        	coordinates = dummyLocations; // For local dev

        	console.log(response);
            reply = botMessage + response.text + botEnd;
            $('.chat-history').append(reply);

    		// Scroll down the chat history to latest message
	        var elem = document.getElementById('chatHist');
			elem.scrollTop = elem.scrollHeight;
			if(coordinates.length != 0) {
				for(var i=0; i < coordinates.length; i++) {
					addPinpoint(coordinates[i]);
				}
			}
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


function addPinpoint(coordinates) {
	// Adds a pinpoint to Leafleft map
	L.marker(coordinates).addTo(mymap)
    .bindPopup("<b>Hello world!</b><br />I am a popup.");
}


(function() {

  $('#live-chat header').on('click', function() {
    $('.chat').slideToggle(300, 'swing');
    $('.chat-message-counter').fadeToggle(300, 'swing');

  });
}) ();