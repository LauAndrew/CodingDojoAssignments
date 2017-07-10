
var HOUR = 7;
var MINUTE = 45;
var PERIOD = "AM";
var SENTENCE = "It's";

if (MINUTE < 30) {
  // console.log("just after");
  SENTENCE += " just after "
  SENTENCE += HOUR
}

else{
  // console.log("almost");
  SENTENCE += " almost ";
  SENTENCE += HOUR+1;
}

if (PERIOD = "AM"){
  // console.log("in the morning");
  SENTENCE += " in the morning "
}

else{
  // console.log("in the evening");
  SENTENCE += " in the evening. "
}

// SENTENCE = SENTENCE +"akdsnvajdsa";
// SENTENCE += "djsdasjkj";

console.log(SENTENCE);
// console.log(HOUR,MINUTE,PERIOD);