# Assignment: Introduction to JavaScript
---

## Section A: Short Answer Questions (1 Mark each)

**Q1.** What is JavaScript?

**Ans** JavaScript is high level  dynamically type programming language. 

**Q2.** Who created JavaScript and in which year?

**Ans** JavaScript is created in 1995 by Brendan Eich.

**Q3.** What was the original name of JavaScript?

**Ans** Mocha is the orignal name of JavsScript.

**Q4.** Is JavaScript the same as Java? Give one major difference.

**Ans** No JAVA and JavaScript is not same because java is statically type language and javascript is dynamically type lenguage.

**Q5.** What does it mean when we say JavaScript is a **high-level** programming language?

**Ans**When we say javascript is **high-level** programming language it means it is human readable language.

**Q6.** Is JavaScript a compiled language or an interpreted language? Explain briefly.

**Ans** JavaScript is interpreted language. javascript engine is execute code at a runtime.

**Q7.** Name the JavaScript engines used by the following browsers:
- Google Chrome -- V8 engine
- Mozilla Firefox -- Spidermonkey
- Apple Safari --javascriptcore

**Q8.** What is **Dynamic Typing** in JavaScript?

**Ans** We do not declare data type of any variable this is identifying data type when program is running.

**Q9.** What is the main difference between a **static** website and a **dynamic** website?

**Ans** In static website content is fixed and in dynamic website content is changed by user.

**Q10.** Name the three pillars of Front-end Web Development and write one line about each.

**Ans** HTMl5 , CSS3 , JavaScript is three pillars of front-end development.
- HTML5: Defines sturucture and content of website
- CSS3: Defines style and presentation of website.
- JavaScript: Adds interactivity and dynamic behavior to a webpage.

**Q11.** What is the difference between Frontend and Backend?

**Ans**
- Frontend: The part of a website that users see and interact with, such as buttons, menus, and pages. It mainly uses HTML, CSS, and JavaScript.
- Backend: The part that works behind the scenes, handling server logic, databases, authentication, and APIs.

**Q12.** What is Node.js?

**Ans** Node.js is run time environment for Javascript outside the browser.

**Q13.** Explain **ECMAScript**. What is its relation with JavaScript?

**Ans** ECMAScript is the specification that defines how a scripting language should work. JavaScript is only programmig language it's rule is defined by ECMAScript.

---

## Section B: True or False  
(Write True or False. If False, correct the statement)

1. JavaScript is a statically typed language.  -- False
2. JavaScript can only run inside the browser. -- False
3. HTML is responsible for the behaviour of a webpage. -- False
4. Node.js allows JavaScript to run outside the browser. -- True
5. JavaScript is case-insensitive. -- True
6. `let name` and `let Name` are the same variable. -- False
7. ECMAScript is a programming language. -- False
8. React, Angular, and Vue.js are used for Backend development. -- False

---

## Section C: Fill in the Blanks

1. JavaScript was created by ___Brendan Eich___ in the year __1995__.
2. The three technologies used in Front-end development are ___HTML5___, ___CSS3___, and ___JavaScript___.
3. JavaScript engines: Chrome uses ___V8 engine___, Firefox uses ___Spidermonkey___.
4. In the restaurant analogy: Customer = ___Frontend___, Waiter = ___Backend___, Chef = ___Database___.
5. JavaScript file extension is ___.js___.

---

## Section D: Conceptual Questions (2 Marks each)

**Q14.** Differentiate between a **static website** and a **dynamic website**. Give one real-world example of each.

**Ans** 
| Static Website                          | Dynamic Website                                 |
| --------------------------------------- | ----------------------------------------------- |
| Content is mostly fixed.                | Content can change based on user input or data. |
| Usually uses HTML, CSS, and JavaScript. | Uses frontend, backend, and often a database.   |
| **Example:** Personal portfolio website | **Example:** Amazon                             |


**Q15.** Explain any two features of JavaScript that make it suitable for creating interactive web pages.

**Ans**
- Eventhandling: JavaScript can respond to user actions like clicks, typing, and mouse movements.
- DOM manipulation: JavaScript can change HTML elements and content dynamically without reloading the page

**Q16.** List any four areas (apart from web browsers) where JavaScript is used today. Mention one popular framework/library for each (if applicable).

**Ans**
- Server side development -node.js library is used
- Mobile app development
- Desktop app development
- Game development


**Q17.** What is the difference between writing JavaScript code:
- Inside an HTML file using `<script>` tag, and
- In an external `.js` file?  
Mention two advantages of using an external JavaScript file.

**Ans**
| Inside HTML using `<script>`                              | External `.js` file                                  |
| --------------------------------------------------------- | ---------------------------------------------------- |
| JavaScript code is written directly inside the HTML file. | JavaScript code is written in a separate `.js` file. |
| Example: `<script> console.log("Hello"); </script>`       | Example: `<script src="script.js"></script>`         |

### Two Advantages of External JavaScript

1. **Reusability:** The same `.js` file can be linked to multiple HTML pages.
2. **Easy Maintenance:** HTML and JavaScript are separated, making the code cleaner and easier to manage.


**Q18.** Explain the difference between Frontend and Backend using the **restaurant analogy** in your own words.

**Ans** 
|Restaurant                                                   |
|-------------------------------------------------------------|
|Coustomer sees and place order                               |
|Waiter takes the order to the kitchen and brings the food back.|
The frontend is like the restaurant area the customer interacts with, while the backend is like the kitchen where the actual processing happens.

**Q19.** Why should a beginner learn JavaScript? Write at least 4 points.

**Ans** ### Why Should a Beginner Learn JavaScript?

1. **Easy to Start:** JavaScript is beginner-friendly and easy to run in a web browser.
2. **Interactive Websites:** It helps create interactive and dynamic web pages.
3. **Wide Range of Uses:** JavaScript can be used for frontend, backend, mobile, and desktop development.
4. **Popular Language:** JavaScript is widely used, so there are many learning resources and job opportunities.


---

## Section E: Code-Based Questions (3 Marks each)

**Q20.** Predict the output of the following code and explain why:

```javascript
let value = 25;
console.log(typeof value);
value = "JavaScript";
console.log(typeof value);
value = false;
console.log(typeof value);
```

**Ans**
### Output

```text
number
string
boolean
```

### Explanation

* Initially, `value = 25`, so `typeof value` returns **`number`**.
* Then, `value = "JavaScript"`, so its type becomes **`string`**.
* Finally, `value = false`, so its type becomes **`boolean`**.

JavaScript is **dynamically typed**, which means a variable can hold values of different data types at different times.


**Q21.** Write a simple HTML + JavaScript program that displays an alert box with the message **"Welcome to JavaScript!"** when a button is clicked.

**Ans** 
```html
<!DOCTYPE html>
<html>
<head>
    <title>JavaScript Alert</title>
</head>
<body>

    <button onclick="showMessage()">Click Me</button>

    <script>
        function showMessage() {
            alert("Welcome to JavaScript!");
        }
    </script>

</body>
</html>
```

### Explanation

When the button is clicked, the `showMessage()` function runs and displays an alert box with the message **"Welcome to JavaScript!"**.


**Q22.** Write JavaScript code to demonstrate **event-driven programming**.  
When a user clicks a button with id `"myBtn"`, the text of a paragraph with id `"demo"` should change to `"Button was clicked!"`.

**Ans**
```script
document.getElementById("myBtn").addEventListener("click", function() {
    document.getElementById("demo").textContent = "Button was clicked!";
});
```


---

## Section F: Practical / Application Based (5 Marks)

**Q23.** Create a complete web page (HTML + JavaScript) that includes the following:

1. A heading: **"My First JavaScript Page"**
2. A button labeled **"Click Me"**
3. When the button is clicked:
   - Show an alert: `"Hello, B.Tech Student!"`
   - Change the background color of the page to light blue
4. Also print `"JavaScript is running successfully!"` in the browser console.

**Ans**
```html
<!DOCTYPE html>
<html>
<head>
    <title>My First JavaScript Page</title>
</head>

<body>

    <h1>My First JavaScript Page</h1>

    <button id="myBtn">Click Me</button>

    <script>
        console.log("JavaScript is running successfully!");

        document.getElementById("myBtn").addEventListener("click", function() {
            alert("Hello, B.Tech Student!");
            document.body.style.backgroundColor = "lightblue";
        });
    </script>

</body>
</html>
```

---

## Section G: Higher Order Thinking (Bonus - 3 Marks)

**Q24.** JavaScript was originally created only for browsers. Today it is used in frontend, backend, mobile apps, desktop apps, and even AI/ML.  
In your own words, explain why JavaScript became so popular and multipurpose. Mention the role of **Node.js** and **ECMAScript** updates in this growth.

**Ans**
### Why JavaScript Became Popular and Multipurpose

JavaScript became popular because it is easy to learn, widely supported, and can be used for many types of applications.

1. **Frontend Development:** JavaScript makes web pages interactive and dynamic.
2. **Node.js:** Node.js allowed JavaScript to run outside the browser, making it possible to build backend servers and APIs.
3. **ECMAScript Updates:** Regular ECMAScript updates introduced new features and improvements, making JavaScript more powerful and modern.
4. **Many Platforms:** JavaScript can now be used for mobile apps, desktop applications, servers, and other types of software.
5. **Large Ecosystem:** Many libraries, frameworks, and tools such as React, Angular, Vue.js, and Express.js have made development easier.

**In short:** JavaScript became multipurpose because Node.js expanded it beyond browsers, while continuous ECMAScript updates improved its features and capabilities.


---
