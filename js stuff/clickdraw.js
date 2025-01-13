//access canvas & buttons via DOM
var c = document.getElementById("playground");
var dotButton = document.getElementById("circle");
var stopButton = document.getElementById("stop");

var ctx = c.getContext("2d"); //prepare to interact with 2d

ctx.fillStyle = "#00ffff"; //set fill color (cyan)

var requestID;

var clear = function(e){
    e.preventDefault();
    ctx.clearRect(0, 0, 500, 500);
};

var radius = 0;
var growing = true;

var drawDot = function() {
    window.cancelAnimationFrame( requestID );
    ctx.clearRect(0, 0, c.width, c.height);
    if (growing) {
        radius += 1;
    }
    else {
        radius -= 1;
    }
    if (radius == (c.width / 2)){
        growing = false;
    }
    else if (radius == 0) {
        growing = true;
    }
    //draw the dot
    ctx.beginPath(); //.beginPath() is a built-in function
    ctx.arc(c.width/2, c.height/2, radius, 0, 2*Math.PI);
    ctx.stroke();
    ctx.fill();
    requestID = window.requestAnimationFrame(drawDot);
};

dotButton.addEventListener("click", drawDot);
