const months = [
"jenuary",
"february",
"march",
"april",
"may",
"june",
"july",
"august",
"september",
"october",
"november",
"december",


];
const weekdays = [
  "sunday",
  "monday",
  "tuesday",
  "wednesday",
  "thursday",
  "friday",
  "saturday",  
];

const giveaway = document.querySelector(".giveaway");
const deadline = document.querySelector(".deadline");
const items = document.querySelectorAll(".deadline-format h4");

let futureDate = new Date(2023,10,5,11,50,0);

const year = futureDate.getFullYear();
const hours = futureDate.getHours();
const minutes = futureDate.getMinutes();
let month = futureDate.getMonth();
month = months[month];
const date = futureDate.getDate();
const weekday = weekdays [futureDate.getDay()];

giveaway.textContent = `give away ends on ${weekday} ${date} ${month} ${year} ${hours}:
${minutes}`; 

//future time in ms
const futureTime = futureDate.getTime();


//run a funtion for remaining time 

function getRemainingTime() {
    const today = new Date() .getTime();
    const t = futureTime - today;
    console.log(t);
    //1s = 1000ms
    //1m = 60s
    //1hr = 60m
    //1d = 24hr

    //values in ms
    const oneDay = 24 * 60 * 60 * 1000;
    const oneHour = 60 * 60 * 1000;
    const oneMinute = 60 * 1000; 
    //calculate all values 
    let days = t / oneDay;
    days = Math.floor(days);
    let hours =Math.floor((t % oneDay) / oneHour);
    let minutes = Math.floor((t % oneHour) / oneMinute);
    let seconds = Math.floor((t % oneMinute) / 1000);
    console.log(minutes)

    //set value arrays
    const values = [days, hours, minutes, seconds];
   
    items.forEach(function(item,index ){
        item.innerHTML = values[index];
    });
}
getRemainingTime();