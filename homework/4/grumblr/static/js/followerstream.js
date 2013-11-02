var req;

// Sends a new request to update the to-do list
function sendRequest() {
    if (window.XMLHttpRequest) {
        req = new XMLHttpRequest();
    } else {
        req = new ActiveXObject("Microsoft.XMLHTTP");
    }
    
    var pathArray = window.location.pathname.split( '/' );
	pathArray[2]="xml_response_for_grumblr_stream";
	
	var newPathname = "/grumblr";
	for ( i = 2; i < pathArray.length; i++ ) {
	  newPathname += "/";
	  newPathname += pathArray[i];
	}
	
    req.onreadystatechange = handleResponse;
    req.open("GET", newPathname, true);
    req.send(); 
}

// This function is called for each request readystatechange,
// and it will eventually parse the XML response for the request
function handleResponse() {
    if (req.readyState != 4 || req.status != 200) {
        return;
    }

    // Removes the old to-do list items
    var list = document.getElementById("refresh_target");
    while (list.hasChildNodes()) {
        list.removeChild(list.firstChild);
    }

    // Parses the XML response to get a list of DOM nodes representing items
    var xmlData = req.responseXML;
    var items = xmlData.getElementsByTagName("item");

    // Adds each new todo-list item to the list
    for (var i = 0; i < items.length; ++i) {
        // Parses the item id and text from the DOM
        var comment = items[i].getElementsByTagName("comment")[0].textContent
        var author = items[i].getElementsByTagName("author")[0].textContent
  
        // Builds a new HTML list item for the todo-list item
        var newItem = document.createElement("li");
        
        
        newItem.innerHTML = 
        	 "Slayer<div class=\"col-lg-4\">  <h2> <font class=\"fancytext_big\"> Grumbl:</font></h2> <div class=\"fancytext1\"><p>"+grumbl+"</p> <img src=\""+picture+"\" alt=\"picture\"	max-width=\"300px\" height=\"200px\">" +
        	 "</div><a href=\"/grumblr/add_comment_redirect/"+grumblid+"/\"> <button type=\"Submit\" value=\"Comment\" class=\"btn btn-sm btn-primary\">Comment</button></a>" +
        	 "<a href=\"/grumblr/dislike_grumbl/"+grumblid+"/\"><button type=\"button\" class=\"btn btn-sm btn-danger\">Dislike</button></a><br/>" +
        	 "author: <a href=\"/grumblr/profile/"+author+"/\">"+author+" </a>| Disliked by:"+dislikecounter+"<br/> "+datetime+"</div>"
        	 
        	
        // Adds the todo-list item to the HTML list
        list.appendChild(newItem);
    }
}






// causes the sendRequest function to run every 10 seconds
window.setInterval(sendRequest, 10000);
