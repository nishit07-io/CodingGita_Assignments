//  E: switch statement

// Q1.
// let monthnumber = 12
// switch(monthnumber){
//     case 1:
//         console.log(31)
//         break;
//     case 2:
//         console.log(28)
//         break;
//     case 3:
//         console.log(31)
//         break;
//     case 4:
//         console.log(30)
//         break;
//     case 5:
//         console.log(31)
//         break;
//     case 6:
//         console.log(30)
//         break;
//     case 7:
//         console.log(31)
//         break;
//     case 8:
//         console.log(31)
//         break;
//     case 9:
//         console.log(30)
//         break;
//     case 10:
//         console.log(31)
//         break;
//     case 11:
//         console.log(30)
//         break;
//     case 12:
//         console.log(31)
//         break;
//         default:
//             console.log("Please enter valid month number.");
//             break;
// }

// Q2.
// let char = v;
// switch(char){
//     case "a":
//         console.log("vowel");
//         break;
//     case "e":
//         console.log("vowel");
//         break;
//     case "i":
//         console.log("vowel");
//         break;
//     case "o":
//         console.log("vowel");
//         break;
//     case "u":
//         console.log("vowel");
//         break;
//     default:
//         console.log("consonant");
//         break;
// }

// Q3.
// let number = 3;
// switch(true){
//     case number == 1 || number == 2:
//         console.log("Winter");
//         break;
//     case number == 3 || number == 4:
//         console.log("Winter");
//         break;
//     default:
//         console.log("Please enter valid month number!!")
//         break;
// }

// Q4.
// let marks = 75;
// switch(true){
//     case marks >= 75 && marks <= 100:
//         console.log("Distinction");
//         break;
//     case marks >= 60:
//         console.log("1st class");
//         break;
//     case marks >= 50:
//         console.log("2nd class");
//         break;
//     case marks >= 60:
//         console.log("3rd class");
//         break;
//     case marks < 35 && marks >= 0:
//         console.log("Failed");
//         break;
//     default:
//         console.log("Please enter valid marks!!")
//         break;
//     }   

// Q5.
// let role = "admin";
// let action = "create"
// switch(role){
//     case "admin":
//         switch(action){
//             case "create":
//                 console.log("You are now in creating mode.")
//                 break;
//             case "edit":
//                 console.log("You are switching in editing mode.")
//                 break;
//             case "delete":
//                 console.log("Confirm delete !!")
//                 break;
//         }
//     case "user":
//         console.log("You are in limited access only.")
//         break;
//     default:
//         console.log("Please enter valid role.")
//         break;
// }

// Q6.
// let fruit = "mango";

// switch (fruit) {
//   case "apple":
//     console.log("Apple is red");
//   case "mango":
//     console.log("Mango is yellow");
//   case "banana":
//     console.log("Banana is yellow");
//   default:
//     console.log("Unknown fruit");
// }
// Output:
// Apple is red
// Mango is yellow
// Banana is yellow
// Unknown fruit
// REASON: this is print all things because of afte every case break is missind so JS print all case.

// CORRECT CODE
// let fruit = "mango";
// switch (fruit) {
//   case "apple":
//     console.log("Apple is red");
//     break;
//   case "mango":
//     console.log("Mango is yellow");
//     break;
//   case "banana":
//     console.log("Banana is yellow");
//     break;
//   default:
//     console.log("Unknown fruit");
//     break;
// }

// Q7.
// let num = "0";
// switch(num){
//     case 0:
//         console.log("Number zero");
//         break;
//     case "0":
//         console.log("String zero");
//         break;
//     case false:
//         console.log("Boolean false");
//         break;
//     case null:
//         console.log("null value type object");
//         break;
//     case undefined:
//         console.log("value is not defined type undefined");
//         break;
//     default:
//         console.log("Unknown value.");
//         break;
// }

// Q8.
// let a = 10;
// let b = 0;
// let opr = "+";
// switch(opr){
//     case "+":
//         console.log("In this case you add number");
//         break;
//     case "-":
//         console.log("In this case subtract number");
//         break;
//     case "*":
//         console.log("In this case multiply each number.");
//         break;
//     case "/":
//         switch(true){
//             case b === 0:
//                 console.log("Please enter valid number.")
//                 break;
//             default:
//                 console.log("In this case devide a number.");
//                 break;
//         }
//     case "%":
//         switch(true){
//             case b === 0:
//                 console.log("Please enter valid number.")
//                 break;
//             default:
//                 console.log("In this case devide a number and you get remainder of this number.");
//                 break;
//         }
//     case "**":
//         console.log("In this case exponentiation of a  number.")
//         break;
//     default:
//         console.log("Please enter valid oprater.")
//         break;
// }

// Q9.
// let daynum = 9;
// switch(true){
//     case daynum >= 1 && daynum <= 10 :
//         console.log("Beginning of the month");
//         break;
//     case daynum >= 11 && daynum <= 20 :
//         console.log("Middle of the month");
//         break;
//     case daynum >= 21 && daynum <= 31 :
//         console.log("End of the month");
//         break;
//     default:
//         console.log("Please enter valid day number.");
//         break;
// }

// Q10.
// let cat = "veg";
// let size = "half";
// switch(cat){
//     case "veg":
//         switch(size){
//             case "half":
//                 console.log("Half orderd is confirmed.");
//                 break;
//             case "full":
//                 console.log("Full veg orderd com=nfimed.");
//                 break;
//         }
//         break;
//     case "nonveg":
//         switch(size){
//             case "half":
//                 console.log("Half orderd is confirmed.");
//                 break;
//             case "full":
//                 console.log("Full nonveg orderd com=nfimed.");
//                 break;
//         }
//         break;
// }


//  F:Ternary Operator


// Q1.
// let num = 7;
// let result = (num % 7 === 0 ? "Divisible by 7" : "Not Divisible by 7")
// console.log(result)

// Q2.
// let temp = 30;
// let result = (temp > 35 ? "Hot day" : "Pleasent day")
// console.log(result)

// Q3.
// let age = 18;
// let ans = age<13 ? "child" : (age>=13 && age<=19) ? "Teenage" : "adult"
// console.log(ans)

// Q5.
// let a = 20;
// let b = 35;
// let c = 25;
// console.log(a >= b && a >= c ? a : b >= c ? b : c);
// Output: 35

// Q6.
// let studentMarks = 65;
// console.log(
//     studentMarks >= 75 ? "Distinction" :
//     studentMarks >= 60 ? "First Class" :
//     studentMarks >= 50 ? "Second Class" :
//     studentMarks >= 35 ? "Pass" : "Fail");
// // Output: First Class

// Q7.
// let number2 = -7;
// console.log(
//     number2 === 0 ? "Zero" :
//     number2 > 0 ?
//         (number2 % 2 === 0 ? "Positive Even" : "Positive Odd") :
//         (number2 % 2 === 0 ? "Negative Even" : "Negative Odd") );
// Output: Negative Odd

// Q8.
// let year = 2024;
// console.log(
//     year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0)
//         ? "Leap Year"
//         : "Not a Leap Year");
// // Output: Leap Year

// Q9.
// let role1 = "admin";
// let action1 = "edit";
// console.log(
//     role1 === "admin" ?
//         (action1 === "delete" ? "Admin Delete" :
//         action1 === "edit" ? "Admin Edit" : "Admin Other") :
//     role1 === "user" ?
//         (action1 === "view" ? "User View" : "User Restricted") :
//         "Invalid Role");
// Output: Admin Edit

// Q10.
// let cartTotal = 6000;
// let orderSummary = cartTotal >= 5000
//     ? { discount: "20%", payable: cartTotal * 0.80 }
//     : cartTotal >= 2000
//         ? { discount: "10%", payable: cartTotal * 0.90 }
//         : cartTotal >= 1000
//             ? { discount: "5%", payable: cartTotal * 0.95 }
//             : { discount: "0%", payable: cartTotal };
// console.log(orderSummary);
// Output: { discount: '20%', payable: 4800 }