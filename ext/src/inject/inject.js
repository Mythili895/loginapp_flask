chrome.extension.sendMessage({}, function(response) {
	var readyStateCheckInterval = setInterval(function() {
	if (document.readyState === "complete") {
		clearInterval(readyStateCheckInterval);

		// ----------------------------------------------------------
		// This part of the script triggers when page is done loading
		console.log("Hello. This message was sent from scripts/inject.js");
		// ----------------------------------------------------------
		
		
		

		$( "p" ).click(function() {
			var message = "You clicked a paragraph!"
			chrome.extension.sendMessage(message);
    		
	
	});
	$( ".star-off" ).click(function() {
			var message = "You clicked to make it favourite!"
			chrome.extension.sendMessage(message);
    		
	
	});
	$( "a" ).click(function() {
			var message = "You clicked a link!"
			chrome.extension.sendMessage(message);
    		
	
	});
	
	$( ".-img" ).click(function() {
			var message = "You clicked an image!"
			chrome.extension.sendMessage(message);
    		
	
	});
	
	$( ".page-numbers" ).click(function() {
			var message = "You changed to different page !"
			chrome.extension.sendMessage(message);
    		
	
	});
	
	$( "question-hyperlink" ).click(function() {
			var message = "You changed to different question !"
			chrome.extension.sendMessage(message);
    		
	
	});
	
	$( ".vote-up-off" ).click(function() {
			var message = "You clicked a upvote!"
			chrome.extension.sendMessage(message);
    		
	
	});
	
	
	
	$( ".vote-down-off" ).click(function() {
			var message = "You clicked a downvote!"
			chrome.extension.sendMessage(message);
    		
	
	});
	$( window ).scroll(function() {
			var message = "You scrolled!"
			chrome.extension.sendMessage(message);
    		
});
	
	$("p").hover(function(){
		var message = "Your mouse over a paragraph!"
		chrome.extension.sendMessage(message);
        
    });
	
	

    $("input").select(function(){
    	var message = "You selected input text!"
		chrome.extension.sendMessage(message);
        
    });
	
	
	
	$('textarea').on('mouseup', function() { 
	    var message = "You selected text area!"
		chrome.extension.sendMessage(message);
		$("textarea").keypress(function(){
        chrome.extension.sendMessage("you are typing in text area!!")});
        
	});
	
	$( "div" ).mousemove(function( event ) {
  var pageCoords = "( " + event.pageX + ", " + event.pageY + " )";
  var clientCoords = "( " + event.clientX + ", " + event.clientY + " )";
  console.log( "mouse movement trajectory: " + pageCoords);
  var message = "mouse movement trajectory: " + pageCoords
  chrome.extension.sendMessage(message);
});
	
	
	
	$('.views.supernova').hover(function(){
		var message = "you noticed the views!"
		chrome.extension.sendMessage(message);
        console.log("you noticed the views!");
    });
	
	$('.views.hot').hover(function(){
		var message = "you noticed the views!"
		chrome.extension.sendMessage(message);
        console.log("you noticed the views!");
    });
	
	$('.status.answered-accepted').hover(function(){
		var message = "you noticed the answers accepted!"
		chrome.extension.sendMessage(message);
        console.log("you noticed the answers accepted!");
    });
	
	$('.viewcount').hover(function(){
		var message = "you noticed the vote count of the post!"
		chrome.extension.sendMessage(message);
        
    });

    $("p").dblclick(function(){
        var message = "You double clicked!"
		chrome.extension.sendMessage(message);
        
    });
	
	$( window ).unload(function() {
		var message = "You closed the page"
		
	chrome.extension.sendMessage(message); });
		
	$( window ).load(function() {
		var message = "You opened the page"
		
		chrome.extension.sendMessage(message);	
        
  
});

	

	

	}
	}, 10);
});