var n1 = 0;
var n2 = 1;

function nextNumber() {
	document.getElementById("sequence").innerHTML += n1 + " " + n2 + " ";
	n1 += n2;
	n2 += n1;
}

window.setInterval(function() { nextNumber(); }, 1000);