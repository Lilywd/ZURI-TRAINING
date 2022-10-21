const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const prompt = require("prompt-sync")();
const alert = require("prompt-sync")();
var value = 2;
var points = 0;
var wins = true;
var lives = 3;

function guess() {
  rl.question("are you ready ? (Yes or NO)" ,(reply) => {
    let userName = prompt("whats your name: ");
    console.log(userName);
    while (wins && lives != 0) {
      var numbers = Math.floor(Math.random() * value) + 1;
      var userGuess = prompt(
        `guess the number between the range 1 and ${value}: `
      );
      if (numbers == userGuess) {
        alert("you got it right");
        value++;
        points++;
        alert(`you have ${lives} lives`);
        alert(`you have ${points} points`);
        increment();
      } else if (numbers != userGuess) {
        alert("try again");
        lives--;
        points--;
        alert(`you have ${lives} lives`);
        alert(`you have ${points} points`);
      } else {
        wins = false;
      }
    }
    alert(`game over !!!\nyour total points is: ${points}  \ntry again`);
    rl.close();
  });
}
function increment() {
  if (wins == true) {
    alert("congrtulations! you have won, time to move to the next stage !");
  }
}
guess(value);