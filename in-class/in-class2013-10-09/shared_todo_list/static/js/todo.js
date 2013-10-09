


// Insert code here to run when the DOM is ready
$(document).ready( function() {
	$(".delete-btn").click( {
		
		var URL = this.attr("item-id");
		
		window.location="/shared-todo-list/delete-item/"+"URL";
		this.css("visibility","hidden");
		this.remove();
	
	}	
	)
	
});
