int numShapes = 200;
int currentShape = 0;                   // counter
float[] shapeX = new float[numShapes];  // x coordinates
float[] shapeY = new float[numShapes];  // y coordinates
float[] shapeA = new float[numShapes];  // alpha values
int shapeSize = 10;
boolean contrails = false; //contrails
float x = 2;
float y = 2;


PShape c1, c2, c3, c4, c5, c6, c7, c8, c9;
PGraphics cloud;

float degree = 0;

boolean accel;
float scale = 1.25;
float setScale = 1.25;
float thrusters = 35;

float contrailX = 0;
float contrailY = 0;


void settings() { 
  size(800, 800);
}
void setup() {
  frameRate(120);
}


void draw() {
  smooth();
  fill(20, 70, 120);

  float color1 = 0;
  float color2 = 220.0;
  float color3 = 120;

  for (int i = 0; i<450; i++) {
    stroke(color1, color3, color2, 200);
    line(0, i, 800, i);
    color2= color2-(255/450.0);
    color1=color1+(255/450.0);
    color3 = color3-(255/450);
  }
  noStroke();
  cloud(60, 100, 140, 240);  
  cloud(600, 150, 160, 240);
  fill(255, 240, 130);
  ellipse(400, 450, 100, 100);
  fill(20, 70, 120);
  rect(0, 450, 800, 400);

  pushMatrix();

  degree = calAngle(400, 350);
  if (accel == true) {
    if (scale > 0.65) {
      scale = scale - 0.008;
      thrusters+=0.6;
    }
  } else if (scale < setScale) {
    scale = scale + 0.01;
    thrusters-=0.6;
  } else {
    thrusters = 35;
  }





  translate(mouseX, mouseY);
  scale(scale);
  rotate(degree);
  plane();
  popMatrix();
  contrails();
}

float calAngle(float x, float y) {
  float tempX = x - mouseX;
  float tempY = y - mouseY;
  float angle;

  angle = atan2(tempY, tempX) + 1.52;
  return angle;
}


void plane() {

  //back wings
  strokeWeight(4);
  stroke(180);
  beginShape(); 
  fill(150);
  vertex(-30, 0);
  vertex(-30, 12);
  vertex(-50, 15);
  vertex(-70, 25);
  vertex(-110, 25);
  vertex(-110, 15);
  vertex(-60, 0);
  endShape(CLOSE);

  beginShape();
  fill(150);
  vertex(30, 0);
  vertex(60, 0);
  vertex(110, 15);
  vertex(110, 25);
  vertex(70, 25);
  vertex(50, 15);
  vertex(30, 12);
  endShape(CLOSE);

  //wings
  quad(-180, -10, -50, -40, -50, 0, -170, 0);

  quad(50, -40, 50, 0, 170, 0, 180, -10);

  //thursters bottom
  beginShape();
  fill(80);
  strokeWeight(0);
  vertex(-30, -2);
  vertex(-30, 15);
  vertex(-15, 20);
  vertex(0, 15);
  vertex(0, -2);
  endShape(CLOSE);

  beginShape();
  fill(80);
  strokeWeight(0);
  vertex(30, -2);
  vertex(30, 15);
  vertex(15, 20);
  vertex(0, 15);
  vertex(0, -2);
  endShape(CLOSE);

  //engine burner
  fill(255, 165, 0, 170);
  ellipse(15, 10, 25, thrusters);
  fill(255, 165, 0, 170);
  ellipse(-15, 10, 25, thrusters);

  //thrusters top
  beginShape();
  fill(120);
  strokeWeight(0);
  vertex(30, -2);
  vertex(30, 9);
  vertex(15, 14);
  vertex(0, 9);
  vertex(0, -2);
  endShape(CLOSE);

  beginShape();
  fill(120);
  strokeWeight(0);
  vertex(-30, -2);
  vertex(-30, 9);
  vertex(-15, 14);
  vertex(0, 9);
  vertex(0, -2);
  endShape(CLOSE);

  noStroke();


  fill(150);
  rect(-52, -51, 104, 49);
  //rect body
  fill(180);
  triangle(-52, -51, 0, -70, 52, -51);
  //cockpit
  fill(40, 40, 40, 160);
  ellipse(0, -60, 30, 60);
  //grey ring
  fill(180);
  ellipse(0, -50, 50, 60);
  //grey center circle
  fill(150);
  ellipse(0, -40, 55, 60);
  //center circle
  fill(150);
  ellipse(0, -55, 40, 50);
  //shading
  fill(140);
  ellipse(0, -20, 3, 40);

  //rudders
  beginShape();
  fill(185);
  stroke(175);
  strokeWeight(2);
  vertex(-50, 6);
  vertex(-65, -55);
  vertex(-60, -65);
  vertex(-40, -20);
  endShape(CLOSE);

  beginShape();
  fill(185);
  stroke(175);
  strokeWeight(2);
  vertex(50, 6);
  vertex(65, -55);
  vertex(60, -65);
  vertex(40, -20);
  endShape(CLOSE);

  stroke(170);
  strokeWeight(3);
  line(0, 0, 0, 15);

  fill(255, 0, 0, 125);
  noStroke();
  ellipse(-180, -7, 10, 10);
}

void contrails() {

  
  
  
  
  
  contrailX = mouseX - 400;
  contrailY = mouseY - 350;
  
  if (contrailX < 3){
    contrailX = contrailX / 2;
    contrailY = contrailY / 2;
  
    //find way to reduce slope to under 5 at all times.

  }
  
  
  println(contrailX);
  x+=3;
  y+=3;
  shapeX[currentShape] = mouseX+x;
  shapeY[currentShape] = mouseY+y;
  shapeA[currentShape] = 0;

  for (int i=0; i<numShapes; i++) {
    fill(255, shapeA[i]);
    ellipse(shapeX[i], shapeY[i], shapeSize, shapeSize);
    shapeA[i] = 120;
  }


  // increment counter
  currentShape++;
  
  currentShape %= numShapes;

  
  
  
}


void cloud(float x, float y, float opac, float colour) {

  c1 = createShape(ELLIPSE, x, y, 55, 50);
  c1.setFill(color(colour, colour, colour, opac));
  c2 = createShape(ELLIPSE, x+20, y+10, 40, 45);
  c2.setFill(color(colour, colour, colour, opac));
  c3 = createShape(ELLIPSE, x+60, y+5, 70, 45);
  c3.setFill(color(colour, colour, colour, opac));
  c4 = createShape(ELLIPSE, x+25, y-15, 55, 45);
  c4.setFill(color(colour, colour, colour, opac));
  c5 = createShape(ELLIPSE, x+50, y-40, 80, 50);
  c5.setFill(color(colour, colour, colour, opac));
  c6 = createShape(ELLIPSE, x+70, y-45, 80, 65);
  c6.setFill(color(colour, colour, colour, opac));
  c7 = createShape(ELLIPSE, x+100, y+5, 60, 65);
  c7.setFill(color(colour, colour, colour, opac));
  c8 = createShape(ELLIPSE, x+100, y-15, 80, 50);
  c8.setFill(color(colour, colour, colour, opac));
  c9 = createShape(ELLIPSE, x+110, y, 95, 50);
  c9.setFill(color(colour, colour, colour, opac));

  fill(colour, colour, colour, 0);
  stroke(colour-50, colour-50, colour-50, 200);
  arc(x+55, y-20, 60, 60, 3.14, 4);
  arc(x+85, y-5, 60, 60, 0.2, 1.2);
  noStroke();

  cloud=createGraphics(800, 800);
  cloud.beginDraw();
  cloud.blendMode(REPLACE);
  cloud.shape(c1);
  cloud.shape(c2);
  cloud.shape(c3);
  cloud.shape(c4);
  cloud.shape(c5);
  cloud.shape(c6);
  cloud.shape(c7);
  cloud.shape(c8);
  cloud.shape(c9);
  cloud.endDraw();

  image(cloud, 0, 0);
}

void mousePressed() {
  accel = true;
}
void mouseReleased() {
  accel = false;
}
