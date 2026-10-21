// B]  For Loop (Additional advanced questions)

// Q1.
let temp = [28, 32, 25, 40, 18, 35]
let count = 0;
for (let i=0; i<temp.length; i++){
    if (temp[i]>=30){
        count+=1
    }
}
console.log("Days Hotter than 30°C:",count)

// Q2.
let num = 4729;
let sum = 0;
for (let i=0; i<=num; i++){
    let digit = num%10
    sum+=digit
    num = Math.floor(num/10)
}
console.log("Sum of Digits:",sum)

// Q3.
for (let i=1; i<=100; i++){
    if (i%15==0 && i%7!=0){
        console.log(i)
    }
}

// Q4.
let word = "JavaScript";
for (let i=0; i<word.length; i++){
    if (word[i]!="a"&&word[i]!="e"&&word[i]!="i"&&word[i]!="o"&&word[i]!="u"){
        console.log(word[i])
    }
}

// Q5.
let arr = [23, 55, 21, 66, 42, 63]
let maxNum = 0
for (let i=0; i<arr.length; i++){
    if (arr[i]>maxNum){
        maxNum = arr[i]
    }
}
console.log(maxNum)

// Q6.
let num = 28;
let sum = 0;
for (let i=1; i<28; i++){
    if (num%i==0){
        sum+=i
    }
}
if (sum==num){
    console.log("Perfect Number")
}

// Q7.
let num = 1
let str = ""
for (let i=1; i<=8; i++){
    str+=num+" "
    num*=2
}
console.log(str)

// Q8.
let a = 0;
let b = 1;
for (let i=1; i<=20; i++){
    console.log(a)
    next = a+b
    a=b
    b=next
}

// Q9.
let arr = [45, 78, 90, 32, 56, 88];
let sum = 0;
for (let i=1; i<arr.length; i++){
    sum+=arr[i]
}
let avg = sum/arr.length
console.log("Average:",avg)
let count=0
for (let i=1; i<arr.length; i++){
    if (arr[i]>=avg){
        count+=1
    }
}
console.log(count)

// Q10.
let num = 13;
let binary = ""
for (;num>0; num = Math.floor(num/2)){
    let rem = num%2
    binary+=rem
}
console.log(binary)

// C_A] break inside a for Loop

// Q1.
let arr = [45,5,7,5,2,6,95]
for (let i=0; i<arr.length; i++){
    if (arr[i]==7){
        console.log("Index:",i)
        break
    }
}

// Q2.
let pass = "abc@123"
let upass = "abc@123"
let i=0
for (; i<5; i++){
    if (pass===upass){
        console.log("Access granted")
        break
    }
}
if (i==5){
    console.log("Account Blocked")
}

// Q3.
let sum=0;
for (let i=0; sum<100; i++){
    sum+=i
    if (sum>=100){
        console.log(i-1)
        break
    }
}

// Q4.
let name = ["Vishal", "Grency", "Freya", "Nayan", "Sweni", "Utsav", "Chetan"]
for (let i=0; i<name.length; i++){
    if (name[i][0]=="S"){
        console.log(name[i])
        break
    }
}

// Q5.
for (let i=1; i<=50; i++){
    console.log(i)
    if (i>20 && i**(1/2)===Math.floor(i**(1/2))){
        break
    }
}

// C_B] continue inside a for Loop

// Q1.
for (let i=1; i<=30; i++){
    if (i%4==0){
        continue
    }
    console.log(i)
}

// Q2.
let arr = [-3, 53, -12, 23, 21, -123]
let sum=0
for (let i=1; i<arr.length; i++){
    if (arr[i]<0){
        continue
    }
    sum+=arr[i]
}
console.log(sum)

// Q3.
let str = "Hello World"
for (let i=1; i<str.length; i++){
    if (str[i]==" "){
        continue
    }
    console.log(str[i])
}

// Q4.
for (let i=1; i<=12; i++){
    let num = 6*i
    if (num%5==0){
        continue
    }
    console.log(num)
}

// Q5.
let age=[12, 18, 25, 15, 30, 17, 22]
for (let i=1; i<age.length; i++){
    if (age[i]<18){
        continue
    }
    console.log(age[i])
}
