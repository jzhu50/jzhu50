//Michelle Zhu
//SoftDev pd4
//K27 - Basic functions in JavaScript
//2025-01-06m

//JavaScript implementations of Day0 recursive Scheme functions

//factorial:

function fact(n) {
    if (n === 0) {
        return 1;
    }
    return n * fact(n - 1);
};

//TEST CALLS
fact (1) //"...should be  1"
fact (2) //"...should be  2"
fact (3) //"...should be  6"
fact (4) //"...should be  24"
fact (5) //"...should be  120"

let fac = fact(1)

//-----------------------------------------------------------------

//fib:

function fib(n) {
    if (n <= 1) {
        return n;
    }
    return fib(n - 1) + fib(n - 2);
};

//TEST CALLS
fib (0) //"...should be  0"
fib (1) //"...should be  1"
fib (2) //"...should be  1"
fib (3) //"...should be  2"
fib (4) //"...should be  3"

let fib = fib(0)

// Display the results in the HTML
document.getElementById("fac").textContent = `Factorial of 0 is: ${fac}`;
document.getElementById("fib").textContent = `Fibonacci of 0 is: ${fib}`;

//=================================================================