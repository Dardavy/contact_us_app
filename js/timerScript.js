// Getting formated date from date string
let endTimer = new Date('nov 30,2023 23:59:59').getTime();

// Calling defined function at certain interval
let x = setInterval(function () {

  // Getting curent date and time in required format
  let dateNow = new Date().getTime();

  // Calculating difference
  let diff = endTimer - dateNow;
  
  // Getting values of days, hours, minutes, seconds
  let days = Math.floor(diff / (1000 * 60 * 60 * 24));

let hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));

let minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));

let seconds = Math.floor((diff % (1000 * 60)) / 1000);

// Show the output time
document.getElementById('day').innerHTML = days;
document.getElementById('hour').innerHTML = hours;
document.getElementById('minute').innerHTML = minutes;
document.getElementById('second').innerHTML = seconds;

// Show overtime output

if (diff < 0) {
  clearInterval(x);
  document.getElementById('demo').innerHTML = 'IT IS FINALLY HERE!';
  document.getElementById('day').innerHTML = '0';
  document.getElementById('hour').innerHTML = '0';
  document.getElementById('minute').innerHTML = '0';
  document.getElementById('second').innerHTML = '0';  
}

}, 1000);