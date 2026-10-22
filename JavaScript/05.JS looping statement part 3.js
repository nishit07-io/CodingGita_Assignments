// D] Reverse For Loop

// Q1.
for (let i = 50; i >= 1; i--) {
    if (i % 3 == 0 && i % 9 != 0) {
        console.log(i);
    }
}

// Q2.
let num = 4729;
let mul = 1;
let found = false;

for (; num > 0;) {
    let digit = num % 10;
    if (digit % 2 !== 0) {
        mul *= digit;
        found = true;
    }
    num = Math.floor(num / 10)
}
console.log(found ? mul : "No odd digits");

// Q3.
let word = "Programming"
word = word.toLowerCase()
let rev = ""
for(let n = word.length - 1 ; n >= 0; n--){
    let ch = word[n]
    if (ch !== "a" && ch !== "e" && ch !== "i" && ch !== "o" && ch !== "u"){
        rev = rev + word[n]
    }
}
console.log(rev)

// Q4.
let arr = [0, 1];
for (let i = 2; i < 15; i++) {
    arr[i] = arr[i - 1] + arr[i - 2];
}
for (let i = 14; i >= 0; i--) {
    console.log(arr[i]);
}

// Q5.
let num = 121;
let original = num;
let reverse = 0;
for (; num > 0; num = Math.floor(num / 10)) {
    let digit = num % 10;
    reverse = reverse * 10 + digit;
}
if (original === reverse) {
    console.log("Palindrome");
}
else {
    console.log("Not a palindrome");
}

// Q6.
let arr = [12, 45, 7, 23, 56, 89, 34];
let largest = -Infinity;
for (let i = arr.length - 1; i >= 0; i--) {
    if (arr[i] < 50 && arr[i] > largest) {
        largest = arr[i];
    }
}
console.log(largest);

// Q7.
let temp = [32, 28, 41, 19, 35, 27, 38];
let count = 0;
for (let i = temp.length - 1; i >= 0; i--) {
    if (temp[i] < 30) {
        count++;
    }
}
console.log(count);

// Q8.
let num = 13;
let binary = "";
for (; num > 0; ) {
    binary += num % 2;
    num = Math.floor(num / 2)
}
console.log(binary);

// Q9.
let scores = [90, 85, 70, 95, 60, 88, 75];

for (let i = scores.length - 1; i >= 0; i--) {
    if (scores[i] > 80) {
        console.log("Score:", scores[i]);
        console.log("Index:", i);
        break;
    }
}

// Q10.
for (let i = 40; i >= 1; i--) {
    let square = false;
    for (let j = 1; j * j <= i; j++) {
        if (j * j === i) {
            square = true;
            break;
        }
    }
    if (square) {
        continue;
    }
    console.log(i);
}
