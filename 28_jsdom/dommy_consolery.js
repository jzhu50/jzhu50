// Michelle Zhu
// SoftDev pd4
// K28 -- Getting more comfortable with the dev console and the DOM
// 2025-01-07t
// --------------------------------------------------

//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;

//assign an anonymous fxn to a var
var f = function(x)
{
    var j=30;
    return j+x;
};

console.log(f); //returns the function
console.log(f(1)); //returns the numeric output

//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
              return x+30;
          }
        };

console.log(o);
console.log(o['name']);
console.log(o['items'][0]); //returns 10
console.log(o['morestuff'][0]);
console.log(o['morestuff'][0]); //returns undefined
console.log(o['func']);

//create a new node in the tree
var addItem = function(text)
{
    var list = document.getElementById("thelist");
    var newitem = document.createElement("li");
    newitem.innerHTML = text; //creates new <li> element
    list.appendChild(newitem); //appends new <li> element as the last child of the list
};

//prune a node from the tree
var removeItem = function(n)
{
    var listitems = document.getElementsByTagName('li');
    listitems[n].remove();
};

//color selected elements red
var red = function()
{
    var items = document.getElementsByTagName("li");
    for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
    }
};

//color a collection in alternating colors
var stripe = function()
{
    var items = document.getElementsByTagName("li");
    for(var i = 0; i < items.length; i++) {
    if (i%2==0) {
        items[i].classList.add('red');
    } else {
        items[i].classList.add('blue');
    }
    }
};

//insert your implementations here for...
// FIB
var fib = function(n)
{
    if (n<=1){
        return n;
    } else {
        return fib(n-1) + fib(n-2);
    }
}

console.log(fib(0));
console.log(fib(1));
console.log(fib(2));
console.log(fib(3));
console.log(fib(4));
console.log(fib(5));

// FAC
var fac = function(n)
{
    if (n<=1) {
        return 1;
    } else {
        return n * fac(n-1);
    }
}

console.log(fac(0));
console.log(fac(1));
console.log(fac(2));
console.log(fac(3));
console.log(fac(4));
console.log(fac(5));

// GCD
var gcd = function(a, b) {
    while (b !== 0) {
        let temp = b;
        b = a % b;
        a = temp;
    }
    return a;
};

//display each of the results
document.getElementById("fib_result").textContent = `fib of 0 is ${fib(0)}`;
document.getElementById("fac_result").textContent = `fac of 5 is ${fib(5)}`;
document.getElementById("gcd_result").textContent = `GCD of 4 and 6 is ${gcd(4,6)}`;

// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
    retVal = param1 + param2;
    return retVal;
};

/*
//send an alert message
alert("hello!");

//color the background purple
document.querySelector("html").style.backgroundColor = "purple";

//add a login image
const loginImage = document.createElement("img");
loginImage.setAttribute(
  "src",
  "https://raw.githubusercontent.com/mdn/learning-area/master/html/forms/image-type-example/login.png",
);
document.querySelector("h1").appendChild(loginImage);
*/
