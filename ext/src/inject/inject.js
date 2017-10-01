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
			var pageURL = $(location).attr("href");
			chrome.extension.sendMessage(message + " , " +pageURL);
    		
	
	});
	$( ".star-off" ).click(function() {
			var message = "You clicked to make it favourite!"
			var pageURL = $(location).attr("href");
			chrome.extension.sendMessage(message + " , " +pageURL);
    		
	
	});
	$( "a" ).click(function() {
			var message = "You clicked a link!"
			var pageURL = $(location).attr("href");
			chrome.extension.sendMessage(message + " , " +pageURL);
			
    		
	
	});
	
	$( ".-img" ).click(function() {
			var message = "You clicked an image!"
			var pageURL = $(location).attr("href");
			chrome.extension.sendMessage(message + " , " +pageURL);
    		
	
	});
	
	$( ".page-numbers" ).click(function() {
			var message = "You changed to different page !"
			var pageURL = $(location).attr("href");
			chrome.extension.sendMessage(message + " , " +pageURL);
    		
	
	});
	
	$( "question-hyperlink" ).click(function() {
			var message = "You changed to different question !"
			var pageURL = $(location).attr("href");
			chrome.extension.sendMessage(message + " , " +pageURL);
    		
	
	});
	
	$( ".vote-up-off" ).click(function() {
			var message = "You clicked a upvote!"
			var pageURL = $(location).attr("href");
			chrome.extension.sendMessage(message + " , " +pageURL);
    		
	
	});
	
	
	
	$( ".vote-down-off" ).click(function() {
			var message = "You clicked a downvote!"
			var pageURL = $(location).attr("href");
			chrome.extension.sendMessage(message + " , " +pageURL);
    		
	
	});
	$( window ).scroll(function() {
			var message = "You scrolled!"
			var pageURL = $(location).attr("href");
			chrome.extension.sendMessage(message + " , " +pageURL);
    		
});
	
	$("p").hover(function(){
		var message = "Your mouse over a paragraph!"
		var pageURL = $(location).attr("href");
		chrome.extension.sendMessage(message + " , " +pageURL);
        
    });
	
	

    $("input").select(function(){
    	var message = "You selected input text!"
		var pageURL = $(location).attr("href");
		chrome.extension.sendMessage(message + " , " +pageURL);
        
    });
	
	
	
	$('textarea').on('mouseup', function() { 
	    var message = "You selected text area!"
		var pageURL = $(location).attr("href");
		chrome.extension.sendMessage(message + " , " +pageURL);
		$("textarea").keypress(function(){
        message = "you are typing in text area!!"
		var pageURL = $(location).attr("href");
		chrome.extension.sendMessage(message + " , " +pageURL);
		
		});
        
	});
	
	$( "div" ).mousemove(function( event ) {
  var pageCoords = "( " + event.pageX + ", " + event.pageY + " )";
  var clientCoords = "( " + event.clientX + ", " + event.clientY + " )";
  console.log( "mouse movement trajectory: " + pageCoords);
  var message = "mouse movement trajectory: " + pageCoords
  var pageURL = $(location).attr("href");
  chrome.extension.sendMessage(message + "--" +pageURL);
});
	
	
	
	$('.views.supernova').hover(function(){
		var message = "you noticed the views!"
		var pageURL = $(location).attr("href");
		chrome.extension.sendMessage(message + " , " +pageURL);
        console.log("you noticed the views!");
    });
	
	$('.views.hot').hover(function(){
		var message = "you noticed the views!"
		var pageURL = $(location).attr("href");
		chrome.extension.sendMessage(message + " , " +pageURL);
        console.log("you noticed the views!");
    });
	
	$('.status.answered-accepted').hover(function(){
		var message = "you noticed the answers accepted!"
		var pageURL = $(location).attr("href");
		chrome.extension.sendMessage(message + " , " +pageURL);
        console.log("you noticed the answers accepted!");
    });
	
	$('.viewcount').hover(function(){
		var message = "you noticed the vote count of the post!"
		var pageURL = $(location).attr("href");
		chrome.extension.sendMessage(message + " , " +pageURL);
        
    });

    $("p").dblclick(function(){
        var message = "You double clicked!"
		var pageURL = $(location).attr("href");
		chrome.extension.sendMessage(message + " , " +pageURL);
        
    });
	
	$( window ).unload(function() {
		var message = "You closed the page"
		
	var pageURL = $(location).attr("href");
	chrome.extension.sendMessage(message + " , " +pageURL); });
		
	$( window ).load(function() {
		var message = "You opened the page"
		
		var pageURL = $(location).attr("href");
		chrome.extension.sendMessage(message + " , " +pageURL);	
        
  
});

	

	

	}
	}, 10);
});