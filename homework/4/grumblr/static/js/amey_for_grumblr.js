var req;

// Sends a new request to update the to-do list
function sendRequest() {
    if (window.XMLHttpRequest) {
        req = new XMLHttpRequest();
    } else {
        req = new ActiveXObject("Microsoft.XMLHTTP");
    }
    
    var pathArray = window.location.pathname.split( '/' );
	pathArray[2]="xml_response_for_comments";
	
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
    var list = document.getElementById("comment-list");
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
        
        
        newItem.innerHTML = "<div style=\"max-width: 400px; max-height: 150px;	 overflow: default;\">" +
        		comment +
        		"</div>" +
        		"<div style=\"width: 300px\">- <a href=\"/grumblr/profile/{{item.user}}\">" +
        		"Grumbled by  " +
        		author +
        		"</a></div>";
        // Adds the todo-list item to the HTML list
        list.appendChild(newItem);
    }
}



$("#submitButtonId").click(function() {

	
    $.ajax({
           type: "POST",
           url: window.location.pathname,
           data: $("#commentform").serialize(), // serializes the form's elements.
           success: function(data)
           {
               alert("submitted via ajax!");
        	   sendRequest(); // show response from the php script.
           }
         });

    return false; // avoid to execute the actual submit of the form.
});


function submitComment()
{
	if(document.forms["commentform"]["commenttext"].value =="")
		{
		alert("Enter some string!");
		return false;
		}
	else
		{return true;}
	
	

}	



// causes the sendRequest function to run every 10 seconds
window.setInterval(sendRequest, 10000);
