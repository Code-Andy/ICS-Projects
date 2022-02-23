function setup() {
  createCanvas(400, 400);
}

var x = 5;
var y = 5;

function draw() {
  background(220);

  circle(x, y, 5);
  x += 1;
  y += 1;
}
