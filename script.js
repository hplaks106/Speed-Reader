function printWords(input) {
  var canvas = document.getElementById("myCanvas");
  var ctx = canvas.getContext("2d");
  ctx.font = "24px Times";
  for (i in input) {
    ctx.fillText(input[i], 10, 50);
  }

}
