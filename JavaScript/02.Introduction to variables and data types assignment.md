# Assignment : Introduction to Variables and Datatypes
---
## Part I : Variables (let, var, const)

### Part a — 4 Questions

**1. Personal Information**<br>
Declare variables for `name`, `age`, and `city` using appropriate variable keywords. Assign values and print all three variables.
<br>
Ans==>>>
let name = Nishit;
let age = 18;
let city = "Ahmedabad";

console.log(name);
console.log(age);
console.log(city);
**2. Change the Score**
Create a variable `score` with the value `50`. Change its value to `80` and print the final value. Use the appropriate keyword for a value that can change.
<br> 
Ans==>>
let score = 50;

score = 80;

console.log(score);

**3. Constant Value**
Create a constant variable `PI` with the value `3.14`. Print its value. Do not try to change the value.<br>
Ans==>>
let PI=3.14;
console.log(PI);
**4. Uninitialized Variables**
Declare one variable having name `num1` using `var` and one having name `num2` using `let` without assigning values. Print both variables. Then assign values to them and print the values again.<br>
Ans===>>>
var num1;
let num2;

console.log(num1);
console.log(num2);

num1 = 10;
num2 = 20;

console.log(num1);
console.log(num2);

### Part b — 4 Questions

**5. Choose the Correct Keyword**
Create the following variables using the most appropriate keyword:

* `studentName` — the value will not change
* `marks` — the value may change
* `schoolName` — the value will not change

Assign values to all three variables. Change `marks` and print all variables.
<br>
Ans===>>>>
let studentName= "Nishit";
var marks= 40;
const schoolName="codinggita";
console.log(studentName);
console.log(marks);
console.log(schoolName);

**6. Understand Scope**
Write a program where `var`, `let`, and `const` variables are declared inside an `if` block. Try to access all three variables outside the block. Observe and identify which variables can be accessed.<br>
Ans==>>>
if (true) {
    var a = 10;
    let b = 20;
    const c = 30;
}

console.log(a); // 10
console.log(b); 
console.log(c); 

**7. Test Re-declaration**
Declare a variable named `user` using `var` and declare it again with a different value. Then perform the same experiment using `let`. Observe what happens and identify which declaration allows re-declaration.<br>
Ans==>>
var user="Nishit";
var user="Nishu";
console.log(user);
let user="Nishit";
let user="Nishu";
console.log(user);

**8. Test Re-assignment**
Create three variables using `var`, `let`, and `const`. Assign an initial value to each. Try to change the value of all three variables. Observe which variables allow re-assignment and which one produces an error.<br>
Ans==>>>
var a = 10;
let b = 20;
const c = 30;
console.log(a);
console.log(b);
console.log(c);
### Part c — 2 Questions

**9. Predict and Explain**
Without running the code, predict the output of each `console.log()` and identify which lines cause errors. Explain your answer using the rules of scope, re-assignment, and variable declaration.

```javascript
var x = 10;

if (true) {
    var x = 20;
    let y = 30;
    const z = 40;
}

console.log(x);
console.log(y);
console.log(z);
```
<br>
### Answer:=
The var is a functional scope but let and const are block scope thst's why only x will print and let and const will give error

**10. Fix the Program**
The following program contains multiple errors. Fix the code so that it runs correctly. Make sure your solution follows the rules for **initialization, re-declaration, re-assignment, and scope**.

```javascript
const name;

let age = 20;
let age = 25;

if (true) {
    var city = "Delhi";
    let country = "India";
}

console.log(country);

const score = 50;
score = 80;
```
<br>
Ans:-
const name = "Sumit";

let age = 20;
age = 25;

if (true) {
    var city = "Delhi";
    let country = "India";
    console.log(country);
}

console.log(city);

let score = 50;
score = 80;

console.log(name);
console.log(age);
console.log(city);
console.log(score);
