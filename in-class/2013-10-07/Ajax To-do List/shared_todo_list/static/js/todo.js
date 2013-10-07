var req;

// Sends a new request to update the to-do list
function sendRequest() {
    if (window.XMLHttpRequest) {
        req = new XMLHttpRequest();
    } else {
        req = new ActiveXObject("Microsoft.XMLHTTP");
    }
    req.onreadystatechange = handleResponse;
    req.open("GET", "/shared-todo-list/get-list", true);
    req.send(); 
}

// This function is called for each request readystatechange,
// and it will eventually parse the XML response for the request
function handleResponse() {
    if (req.readyState != 4 || req.status != 200) {
        return;
    }

    // Removes the old to-do list items
    var list = document.getElementById("todo-list");
    while (list.hasChildNodes()) {
        list.removeChild(list.firstChild);
    }

    // Parses the XML response to get a list of DOM nodes representing items
    var xmlData = req.responseXML;
    var items = xmlData.getElementsByTagName("item");

    // Adds each new todo-list item to the list
    for (var i = 0; i < items.length; ++i) {
        // Parses the item id and text from the DOM
        var id = items[i].getElementsByTagName("id")[0].textContent
        var itemText = items[i].getElementsByTagName("text")[0].textContent
  
        // Builds a new HTML list item for the todo-list item
        var newItem = document.createElement("li");
        newItem.innerHTML = "<a href=\"/shared-todo-list/delete-item/" + id + "\">X</a> " + itemText;

        // Adds the todo-list item to the HTML list
        list.appendChild(newItem);
    }
}

// causes the sendRequest function to run every 10 seconds
window.setInterval(sendRequest, 10000);
