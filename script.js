// ================================
// Button Click Event
// ================================

const button = document.getElementById("btn");

if (button) {
    button.addEventListener("click", () => {
        alert("🎉 Button Clicked Successfully!");
    });
}

// ================================
// Calculator Functions
// ================================

function add(a, b) {
    return a + b;
}

function subtract(a, b) {
    return a - b;
}

function multiply(a, b) {
    return a * b;
}

function divide(a, b) {
    if (b === 0) {
        return "Cannot divide by zero.";
    }
    return a / b;
}

// ================================
// Display Calculator Results
// ================================

const num1 = 10;
const num2 = 5;

console.log("Addition:", add(num1, num2));
console.log("Subtraction:", subtract(num1, num2));
console.log("Multiplication:", multiply(num1, num2));
console.log("Division:", divide(num1, num2));

// ================================
// Student List
// ================================

const students = [
    "Dipak",
    "Ram",
    "Shyam",
    "Hari",
    "Sita"
];

console.log("Student List:");

students.forEach((student, index) => {
    console.log(`${index + 1}. ${student}`);
});

// ================================
// Number Loop
// ================================

console.log("Numbers from 1 to 10:");

for (let i = 1; i <= 10; i++) {
    console.log(i);
}

// ================================
// Array Methods
// ================================

// Convert names to uppercase
const upperCaseStudents = students.map(student => student.toUpperCase());

console.log("Uppercase Names:");
console.log(upperCaseStudents);

// Find a student
const foundStudent = students.find(student => student === "Hari");

console.log("Found Student:");
console.log(foundStudent);

// ================================
// Current Date & Time
// ================================

const now = new Date();

console.log("Current Date:", now.toDateString());
console.log("Current Time:", now.toLocaleTimeString());

// ================================
// Greeting Function
// ================================

function greet(name) {
    return `Welcome, ${name}!`;
}

console.log(greet("Dipak"));

// ================================
// Random Number Generator
// ================================

const randomNumber = Math.floor(Math.random() * 100) + 1;

console.log("Random Number:", randomNumber);

// ================================
// End of Program
// ================================

console.log("JavaScript executed successfully.");
