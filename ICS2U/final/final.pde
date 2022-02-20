/* 
 Title: Create Task(AP CSP)
 Last Changed: 1/21/2020
 Created By: Andy Zhang
 Inspired by League of Legends, based on dodging game objects
 */
 
//character values
float charX, charY, charPosX, charPosY, charSpeed, charAngle;
//projectile values
float projSizeX, projSizeY, projSpeed;
//hold mouseX and mouseY in a constant value
float mousePointX, mousePointY;
//to store the random projectiles
FloatList projectileX, projectileY, projectileAngle, charLastPosX, charLastPosY;
//toggle values for screens, antimations, diffculty, etc.
boolean die = false;
boolean spawned = false;
boolean increaseDif = false;
boolean start = false;
boolean help = true;
boolean fade = false;
boolean moveFast = false;
boolean arrow;
//difficulty settings
int spawnRate = 1500;
int lastProj = 0;
//time counts
int currentTime, lastTime, randomTime, startTime, moveFastTime;

//game counters and toggle values
int frames = 1;
int score, highScore;
int fadeVal = 255;
int life = 3;

//images 
PImage cursor, midLane, skillShot, character, moveQuick, lives;
//animation image
PImage a1, a2, a3, a4, a5, a6;

void setup() {
  size(1000, 750);

  //loading in images
  cursor = loadImage("cursor.png");
  midLane = loadImage("midlane.png");
  skillShot = loadImage("skillshot.png");
  character = loadImage("teemo.png");
  moveQuick = loadImage("moveQuick.png");
  lives = loadImage("heart.png");

  a1 = loadImage("1.png");
  a2 = loadImage("2.png");
  a3 = loadImage("3.png");
  a4 = loadImage("4.png");
  a5 = loadImage("5.png");
  a6 = loadImage("6.png");

  //creating 5 lists to hold positions of projectiles and character, along with projectile angles(for movement)
  projectileX = new FloatList();
  projectileY = new FloatList();
  projectileAngle = new FloatList();
  charLastPosX = new FloatList();
  charLastPosY = new FloatList();

  //defining character values
  charX = 55;
  charY = 55;
  charSpeed = 6;
  charPosX = width/2;
  charPosY = height/2;
  
  //defining projectiles values
  projSizeX = 55;
  projSizeY = 55;
  projSpeed = 8;
  
  //default mouse position before we click
  mousePointX = width/2;
  mousePointY = height/2;
  
  spawned = false;
}

void draw() {
  //keeps track of current time from beginning program
  currentTime = millis();
  background(midLane);
  //draws the character and projectiles using functions
  character();
  projectile();
  difficulty();
  //custom cursor
  cursor(cursor, 0, 0);
  gameStart();

  //this runs the help screen when click
  if (help && !start) {
    helpScreen();
  } else {
    //if not this runs the death commands and some loop command that do not need to be in a function
    if (die) {
      projectileX.clear();
      projectileY.clear();
      projectileAngle.clear();
      charLastPosX.clear();
      charLastPosY.clear();
      lastProj = 0;
      life--;
      die = false;
    } 
    if (life == 0) {
      start= false;
      projSpeed = 8;
      spawnRate = 1500;
      score = 0;
      life = 3;
    }
    if (fadeVal >= 255) {
      fade = true;
    }
    if (fadeVal <= 40) {
      fade = false;
    }
    if (fade) {
      fadeVal-=8;
    } else {
      fadeVal+=8;
    }

    scoreBoard();
    //allows for a animation by counting every frame
    frames++;
  }
}

//displays the score by subtract previous score if higher
void scoreBoard() {
  if (score > highScore) {
    highScore = score;
  }
  textSize(30);
  fill(255, 255, 255);
  text("Highscore: " + highScore, width/2, 15);
  text(score, width/2, 50);
}

 //increases the speed and spawnrate of the projectiles every time it spawns 5, and this stops at a limit.
void difficulty() {
  if (projectileX.size() - lastProj > 5) {
    increaseDif = true;
  }
  
  //caps the max projectile speed and spawnrate
  if (increaseDif && spawnRate > 900) {
    spawnRate-=120;
    projSpeed+=2;
    lastProj = projectileX.size();   
    increaseDif = false;
  }
}

//draws and moves the character at the correct angle and position
void character() {
  //this runs the click animation, which allows the click indicator to run
  if (arrow) {
    arrowAnimation();
  }
  //uses the moveChar command to update the x and y
  charPosX = moveChar(charPosX, charPosY, mousePointX, mousePointY, false);
  charPosY = moveChar(charPosX, charPosY, mousePointX, mousePointY, true);
  //pushes the image out of frame, which it then moves it to the current position and then rotates it towards the cursor and brings it back into frame
  pushMatrix();
  translate(charPosX, charPosY);
  if (abs(charPosX - mousePointX) > 5 || abs(charPosY - mousePointY) > 5) {
    charAngle = atan2(mousePointY - charPosY, mousePointX - charPosX);
  }
  rotate(charAngle-PI/2);
  imageMode(CENTER);
  image(character, 0, 0, 65, 65);
  popMatrix();
}

//character's ability to move fast on "w"
void moveFaster() {
  //when true, the character becomes faster and a countdown begins, which shows the cooldown time of the "ability"
  image(moveQuick, 850, 600, 100, 100);
  int moveTimeDif = 0; 
  if (moveFast) {
    moveTimeDif =   currentTime - moveFastTime;
    charSpeed = 10;
    //time difference allows us to determine how long to do things for(ie text, etc);
    if (moveTimeDif > 0 && moveTimeDif < 1000) {
      text("5", 850, 600);
    } else if (moveTimeDif > 1000 && moveTimeDif < 2000) {
      text("4", 850, 600);
    } else if (moveTimeDif > 2000 && moveTimeDif < 3000) {
      text("3", 850, 600);
    } else if (moveTimeDif > 3000 && moveTimeDif < 4000) {
      tint(100);
      image(moveQuick, 850, 600, 100, 100);
      tint(255);
      text("2", 850, 600);
      charSpeed = 8;
    } else if (moveTimeDif > 4000 && moveTimeDif < 5000) {
      tint(100);
      image(moveQuick, 850, 600, 100, 100);
      tint(255);
      text("1", 850, 600);
      charSpeed = 8;
    } else if (moveTimeDif > 5000) {
      moveFast = false;
      charSpeed = 8;
    }
  }
}

//lots of collective commands that only begin once the game starts
void gameStart() {
  int timeDif = 0; 
  //moves the timestart to the when players hits space not when the program runs
  if (start) {
    timeDif =   currentTime - startTime;
    //draws the hearts
    for (int i = 0; i < life; i++) {
      image(lives, 100 + i * 60, 600, 50, 50);
    }
    moveFaster();
  } else {
    textSize(60);
    textAlign(CENTER, CENTER);
    fill(255, 255, 255, fadeVal);
    text("Press Space to begin", 500, 350);
    fill(100, 200, 80, fadeVal);
    rect(800, 550, 100, 100);
    textSize(20);
    fill(255, 255, 255, fadeVal);
    text(" PRESS 'H'\n FOR HELP", 847, 600);
  }

  textSize(150);
  textAlign(CENTER, CENTER);

  //begin spawning 3 seconds after clicking space
  if (timeDif > 3000) {
    randomSpawn();
  } else {
    fill(0, 0, 0, 150);
    rect(0, 0, width, height);
  }  

  //countdown 
  fill(255, 0, 0);
  if (timeDif > 0 && timeDif < 1000) {
    text("3", width/2, height/2-20);
  } else if (timeDif > 1000 && timeDif < 2000) {
    text("2", width/2, height/2-20);
  } else if (timeDif > 2000 && timeDif < 3000) {
    text("1", width/2, height/2-20);
  }
}

//Using millis, I compare the difference of the current time and last projectile spawn time to a random number
//If it is equal or greater, a new projectile spawns.
void randomSpawn() {
  if (spawned) {
    lastTime = millis();
    spawned = false;
    randomTime = int(random(0, spawnRate));
  }
  if ((currentTime - lastTime) > randomTime) {
    spawnProjectile();
    spawned = true;
  }
}

//To EVERY(IN A LIST)calculate and draw the projectile and see if it collides with the player.
//For loops are used to evaluate every value in the list
void projectile() {
  for (int num = 0; num<projectileX.size(); num++) {
    projectileX.set(num, moveProj(projectileX.get(num), projectileY.get(num), false, projectileAngle.get(num)));
    projectileY.set(num, moveProj(projectileX.get(num), projectileY.get(num), true, projectileAngle.get(num)));
  }
  for (int num = 0; num<projectileX.size(); num++) {
    imageMode(CENTER);
    //creates a new layer to move the projectile image over to a new point, while rotating it but not affect other things in the program.
    pushMatrix();
    translate(projectileX.get(num), projectileY.get(num));
    rotate(projectileAngle.get(num));
    imageMode(CENTER);
    image(skillShot, 0, 0);
    popMatrix();
  }
  for (int num = 0; num<projectileX.size(); num++) {
    if (collision(projectileX.get(num), projectileY.get(num), charPosX, charPosY)) {
      die = true;
    }
  }
}

//determines the projectile spawn point and angle of attack(direction it goes to player)
void spawnProjectile() {
  //random number to determine edge
  int edge = int(random(0, 4));
  score++;
  switch(edge) {
  case 0:
    projectileX.append(random(0, 1000));
    projectileY.append(0);
    charLastPosX.append(charPosX);
    charLastPosY.append(charPosY);
    break;
  case 1:
    projectileX.append(random(0, 1000));
    projectileY.append(750);
    charLastPosX.append(charPosX);
    charLastPosY.append(charPosY);
    break;
  case 2:
    projectileX.append(0);
    projectileY.append(random(0, 750));
    charLastPosX.append(charPosX);
    charLastPosY.append(charPosY);
    break;
  case 3:
    projectileX.append(1000);
    projectileY.append(random(0, 750));
    charLastPosX.append(charPosX);
    charLastPosY.append(charPosY);
    break;
  }
  int listSize = charLastPosX.size() - 1;
  projectileAngle.append(atan2(charLastPosY.get(listSize) - projectileY.get(listSize), charLastPosX.get(listSize) - projectileX.get(listSize)));
}

//simple animation that runs depending on the "frame" number
void arrowAnimation() {
  imageMode(CENTER);
  switch(frames) {
  case 1:
    image(a1, mousePointX, mousePointY, 70, 70);
    break;
  case 2:
    image(a2, mousePointX, mousePointY, 70, 70);
    break;
  case 3:
    image(a3, mousePointX, mousePointY, 70, 70);
    break;
  case 4:
    image(a4, mousePointX, mousePointY, 70, 70);
    break;
  case 5:
    image(a5, mousePointX, mousePointY, 70, 70);
    break;
  case 6:
    image(a6, mousePointX, mousePointY, 70, 70);
    arrow = false;
    frames = 1;
    break;
  }
}

//draws a help screen using hardcode and lots of images and text
void helpScreen() {
  background(0);
  int colorCount = 0;
  float  colorMultiplier = 0.2;
  int backgroundX = 0, backgroundY = 0;
  //double while loop to create a background gradient of sqaures. Compares its x and y to width and height and draws squares.
  //Color is done using the x and y divided by a square to create a gradient
  while (backgroundY < height) {
    backgroundX = 0;
    colorMultiplier += 0.2;
    while (backgroundX < width) {
      colorCount = backgroundX / 100 + 1;
      noStroke();
      fill(colorCount*4*colorMultiplier, colorCount*16*colorMultiplier, colorCount*10 *colorMultiplier);
      rect(backgroundX, backgroundY, 100, 100);
      backgroundX+=100;
    }
    backgroundY+=100;
  }
  fill(255);
  textSize(50);
  textAlign(CENTER);
  text("How to play", width/2, 80);
  textAlign(LEFT);
  text("Right click to move", 50, 175);
  imageMode(CORNER);
  image(character, 700, 100, 100, 100);
  image(cursor, 800, 130);
  text("Dodge the projectiles", 50, 275);
  image(character, 700, 200, 100, 100);
  //rotates the image using push/pop matrix.
  pushMatrix();
  translate(940, 275);
  rotate(radians(180));
  image(skillShot, 0, 0);
  popMatrix();
  text("Press 'W' to move faster \nfor a short period", 50, 375);
  image(moveQuick, 700, 350, 100, 100);
  text("W", 730, 415);
  text("You have 3 Lives", 50, 550);
  for (int x = 0; x < 3; x++) {
    image(lives, 700 + x * 60, 500, 50, 50);
  }
  text("Beat my highscore", 50, 650);
  text("57", 700, 650);
  textSize(40);
  fill(255, 10, 0);
  textAlign(CENTER);
  text("Press Space to Continue", 500, 715);
}

//abstraction created to determine if 2 circles collide.
boolean collision(float x, float y, float x2, float y2) {
  float distance;

  distance = dist(x, y, x2, y2);

  if (distance < (charX+projSizeX)/2) {
    return true;
  } else {
    return false;
  }
}

//abstraction created to move a object to a point specified.
float moveChar(float x, float y, float x2, float y2, boolean returnY) {
  float finalX = x;
  float finalY = y;
  float angle;

  if (abs(x - x2) > 5 || abs(y - y2) > 5) {
    angle = atan2(y2 - y, x2 - x);
    finalX = x + charSpeed * cos(angle);
    finalY = y + charSpeed * sin(angle);
  }
  if (returnY) {
    return(finalY);
  } else {
    return(finalX);
  }
}

//abstraction created to move a object in a direction(angle) specified.
float moveProj(float x, float y, boolean returnY, float angle) {
  float finalX = x;
  float finalY = y;

  finalX = x + projSpeed  * cos(angle);
  finalY = y + projSpeed  * sin(angle);
  if (returnY) {
    return(finalY);
  } else {
    return(finalX);
  }
}

void keyPressed() {
  //extra statements to not allow buttons to be pressed on certain screens
  //if moveFast is true, players cannot use the ability again until it is off cooldown
  if (key == 'w' && moveFast == false && start) {
    moveFastTime = millis();
    moveFast = true;
  }
  if (key == 'W' && !moveFast == false&& start) {
    moveFastTime = millis();
    moveFast = true;
  }

  if (key == 'h') {
    help = true;
  }
  if (key == 'H') {
    help = true;
  }

  if (key == ' ' && start == false) {
    if (help) {
      help = false;
    } else {
      start = true;
      die = false;
      startTime = millis();
    }
  }
}

void mousePressed() {
  if (mouseButton == RIGHT && !die) {
    mousePointX = mouseX;
    mousePointY = mouseY;
    arrow = true;
    frames = 1;
  }
}

void mouseDragged() {
  if (mouseButton == RIGHT && !die) {
    mousePointX = mouseX;
    mousePointY = mouseY;
  }
}
