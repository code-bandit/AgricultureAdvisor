// Get the container element
var btnContainer = document.getElementById("linksIndexPage");

// Get all buttons with class="btn" inside the container
var btns = btnContainer.getElementsByClassName("nav-link");

// Loop through the buttons and add the active class to the current/clicked button
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function() {
    var current = btnContainer.getElementsByClassName("active");
    // document.getElementById("demo").innerHTML = "hello" + current[0].className;
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
  });
} 