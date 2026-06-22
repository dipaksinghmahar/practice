const button = document.getElementById("btn");

button.addEventListener("click", function () {
    alert("Button Clicked!");
});

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
    return a / b;
}

console.log(add(10, 5));
console.log(subtract(10, 5));
console.log(multiply(10, 5));
console.log(divide(10, 5));

const students = [
    "Dipak",
    "Ram",
    "Shyam",
    "Hari",
    "Sita"
];

students.forEach(student => {
    console.log(student);
});

for(let i = 1; i <= 10; i++){
    console.log(i);
}