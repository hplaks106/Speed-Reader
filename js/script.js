var string = "Hey there delilah"
list = string.trim().split(" ")
var delayInMilliseconds = 3000; //1 second
// function printWords(list) {
//   var canvas = document.getElementById("myCanvas");
//   var ctx = canvas.getContext("2d");
//   ctx.font = "24px Times";
//   var delayInMilliseconds = 3000; //1 second
//   for (var word in list) {
//     setTimeout(function() {
//       ctx.fillText(list[word], 10, 50);
//     }, delayInMilliseconds);
//   }
// }
function printWords(list) {
  for (var word in list) {
    var temp = temp + list[word];
    document.getElementById("canvas").innerHTML = temp;
  }
}
