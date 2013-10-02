function add() {
  var x = parseInt(document.getElementById("x").value);
  var y = parseInt(document.getElementById("y").value);
  document.getElementById("ans").value = x + y;
}

function subtract() {
  var x = parseInt(document.getElementById("x").value);
  var y = parseInt(document.getElementById("y").value);
  document.getElementById("ans").value = x - y;
}

function multiply() {
   var x = parseInt(document.getElementById("x").value);
   var y = parseInt(document.getElementById("y").value);
   document.getElementById("ans").value= x * y;
}

function divide() {
    var x = parseInt(document.getElementById("x").value);
    var y = parseInt(document.getElementById("y").value);
    document.getElementById("ans").value= x / y;
}
