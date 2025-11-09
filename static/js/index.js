var title = ['Speed', 'Money', 'Adventure', 'Airplane', 'Ironman', 'Banana'];

var i = 0;  // the index of the current item to show

setInterval(function() {            // setInterval makes it run repeatedly
    document
        .getElementById('things')
        .innerHTML = title[i++];    // get the item and increment i to move to the next
    if (i == title.length) i = 0;   // reset to first element if you've reached the end
}, 1000);  

function myFunction() {
  var x = document.getElementById("links");
  if (x.style.display === "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
}