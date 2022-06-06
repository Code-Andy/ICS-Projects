let img;
let stored;
const pointSize = 40;
var dict = new Object();

/* Paste Range List for [X Coord] then [Y Coord] */
const pasteRange = {
  stress: [
    [20, 220],
    [20, 220],
  ],
  depression: [
    [220, 470],
    [20, 220],
  ],
  anxiety: [
    [20, 220],
    [220, 470],
  ],
  pessimism: [
    [220, 470],
    [220, 470],
  ],
};

/* Initiating Image compiler */
let initialRun = 0;
function setup(inputValueArray) {
  let c = createCanvas(500, 500);
  c.parent("heatMap");
  //console.log(localStorage.getItem("canvas"));
  localStorageCheck = localStorage.getItem("canvas");

  if (initialRun === 0 || localStorageCheck === null) {
    /* Loading base (default) */
    img = loadImage("baseCanvas.png", (result) => {
      localStorage.setItem("canvas", result);
      image(img, 0, 0, width, height);

      /* Gradient Border Setup */
      colorMode(HSB, 360, 100, 100, 100);
      rectMode(CENTER);
      noFill();
      strokeWeight(20);
      let gradientBorder = drawingContext.createLinearGradient(
        width / 2 - 200,
        height / 2 - 200,
        width / 2 + 200,
        height / 2 + 200
      );
      gradientBorder.addColorStop(0, color(316, 100, 100, 60));
      gradientBorder.addColorStop(1, color(260, 100, 100, 50));
      drawingContext.strokeStyle = gradientBorder;
      rect(width / 2, height / 2, width - 30, height - 30, 10);

      /* Category Assignment */
      for (let value in inputValueArray) {
        console.log(value + " value was pasted:");
        const pasteRangeX = pasteRange[value];
        const pasteRangeY = pasteRange[value];

        /* Range of possible X-values for data point */
        let rangeX = {
          min: pasteRangeX[0][0],
          max: pasteRangeX[0][1],
        };

        /* Random X-coordinate within range */
        let deltaX = rangeX.max - rangeX.min;
        const randX = Math.round(rangeX.min + Math.random() * deltaX);

        /* Range of possible Y-values for data point */
        let rangeY = {
          min: pasteRangeY[1][0],
          max: pasteRangeY[1][1],
        };

        /* Random Y-coordinate within range */
        let deltaY = rangeY.max - rangeY.min;
        const randY = Math.round(rangeY.min + Math.random() * deltaY);

        /* Point Coordinate */
        let x = randX;
        let y = randY;

        /* Points per Category */
        colorMode(RGB);
        noStroke();
        if (value == "stress") {
          fill(255, 0, 0, surveyData[value]);
          strokeWeight(pointSize / 4);
          stroke(255, 0, 0, surveyData[value] - 50);
          circle(x, y, pointSize);
        }
        if (value == "depression") {
          fill(0, 255, 0, surveyData[value]);
          strokeWeight(pointSize / 4);
          stroke(0, 255, 0, surveyData[value] - 50);
          circle(x, y, pointSize);
        }
        if (value == "anxiety") {
          fill(0, 0, 255, surveyData[value]);
          strokeWeight(pointSize / 4);
          stroke(0, 0, 255, surveyData[value] - 50);
          circle(x, y, pointSize);
        }
        if (value == "pessimism") {
          fill(255, 200, 60, surveyData[value]);
          strokeWeight(pointSize / 4);
          let colourGrad;
          colourGrad = surveyData[value] - 50;
          stroke(255, 200, 60, surveyData[value] - 50);
          circle(x, y, pointSize);
        }
        console.log("Printed circle at (" + x + "," + y + ")");
        initialRun = 1;
      }
      localStorage.setItem("canvas", canvas.toDataURL());
      //localStorage.removeItem('canvas', canvas.toDataURL())
      console.log("\n- - - - Task Complete - - - - ");
    });
    console.log("SET NEW LOCAL STORAGE");
  } else {
    /* Loading base (from previous survey) */
    img = loadImage(localStorage.getItem("canvas"), () => {
      image(img, 0, 0, width, height);

      /* Gradient Border Setup */
      colorMode(HSB, 360, 100, 100, 100);
      rectMode(CENTER);
      noFill();
      strokeWeight(20);
      let gradientBorder = drawingContext.createLinearGradient(
        width / 2 - 200,
        height / 2 - 200,
        width / 2 + 200,
        height / 2 + 200
      );
      gradientBorder.addColorStop(0, color(316, 100, 100, 60));
      gradientBorder.addColorStop(1, color(260, 100, 100, 50));
      drawingContext.strokeStyle = gradientBorder;
      rect(width / 2, height / 2, width - 30, height - 30, 10);

      /* Category Assignment */
      for (let value in inputValueArray) {
        console.log(value + " value was pasted:");
        const pasteRangeX = pasteRange[value];
        const pasteRangeY = pasteRange[value];

        /* Range of possible X-values for data point */
        let rangeX = {
          min: pasteRangeX[0][0],
          max: pasteRangeX[0][1],
        };

        /* Random X-coordinate within range */
        let deltaX = rangeX.max - rangeX.min;
        const randX = Math.round(rangeX.min + Math.random() * deltaX);

        /* Range of possible Y-values for data point */
        let rangeY = {
          min: pasteRangeY[1][0],
          max: pasteRangeY[1][1],
        };

        /* Random Y-coordinate within range */
        let deltaY = rangeY.max - rangeY.min;
        const randY = Math.round(rangeY.min + Math.random() * deltaY);

        /* Point Coordinate */
        let x = randX;
        let y = randY;

        /* Points per Category */
        colorMode(RGB);
        noStroke();
        if (value == "stress") {
          fill(255, 0, 0, surveyData[value]);
          strokeWeight(pointSize / 4);
          stroke(255, 0, 0, surveyData[value] - 50);
          circle(x, y, pointSize);
        }
        if (value == "depression") {
          fill(0, 255, 0, surveyData[value]);
          strokeWeight(pointSize / 4);
          stroke(0, 255, 0, surveyData[value] - 50);
          circle(x, y, pointSize);
        }
        if (value == "anxiety") {
          fill(0, 0, 255, surveyData[value]);
          strokeWeight(pointSize / 4);
          stroke(0, 0, 255, surveyData[value] - 50);
          circle(x, y, pointSize);
        }
        if (value == "pessimism") {
          fill(255, 200, 60, surveyData[value]);
          strokeWeight(pointSize / 4);
          let colourGrad;
          colourGrad = surveyData[value] - 50;
          stroke(255, 200, 60, surveyData[value] - 50);
          circle(x, y, pointSize);
        }
        console.log("Printed circle at (" + x + "," + y + ")");
        initialRun = 1;
      }
      /* Saving survey graph to localStorage */
      localStorage.setItem("canvas", canvas.toDataURL());
      console.log("\n- - - - Task Complete - - - - ");
    });
  }
}
