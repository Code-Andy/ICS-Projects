document
  .getElementById("startContainer")
  .addEventListener("click", clickToLogin);

document.getElementById("googleLogo").addEventListener("click", clickToLogin);

function fadeElement(elementName) {
  document.getElementById(elementName).animate(
    [
      // keyframes
      { opacity: 0 },
      { opacity: 1 },
    ],
    {
      // timing options
      duration: 1000,
    }
  );
}

let welcomeState = "hello";

function clickToLogin() {
  if (welcomeState == "hello") {
    document.getElementById("welcome").innerHTML = "Login in with Google";
    document.getElementById("welcome").style.fontSize = 35 + "px";
    document.getElementById("welcome").style.fontStyle = "normal";
    document.getElementById("welcome").style.fontWeight = 500;
    document.getElementById("googleLogo").style.display = "flex";

    fadeElement("homePage");
    welcomeState = "login";
  } else if (welcomeState == "login") {
    questionPage();
    fadeElement("questionPage");
  }
}

document.getElementById("ourProject").addEventListener("click", aboutPage);

document.getElementById("dotLogo").addEventListener("click", homePage);

function aboutPage() {
  document.getElementById("aboutPage").style.display = "flex";
  document.getElementById("homePage").style.display = "none";
  document.getElementById("questionPage").style.display = "none";
}

function homePage() {
  document.getElementById("aboutPage").style.display = "none";
  document.getElementById("homePage").style.display = "flex";
  fadeElement("homePage");
  document.getElementById("questionPage").style.display = "none";
}

function questionPage() {
  document.getElementById("aboutPage").style.display = "none";
  document.getElementById("homePage").style.display = "none";
  document.getElementById("questionPage").style.display = "flex";
  document.getElementById("questionText").innerHTML = questions[questionNumber];
}

const questions = [
  "1. Do you care a lot about the way people around you view you?",
  "2. Do you feel like you are always under a lot of pressure from your parents?",
  "3. Do you feel like you put yourself under a lot of pressure?",
  "4. Do you compare your success and achievements to others around you?",
  "5. Do you have overwhelming family responsibilities?",
  "6. Do you have a weak friendship with your peers?",
  "7. Do you often spend most of your free time alone?",
  "8. Have you seen a therapist or talked to a guardian about any mental health issues?",
  "9. Do you create ambitious goals for yourself in regards to education or work?",
  "10. Do you spend more time at work or studying than you do spending with family and friends?",
  "11. Have you been facing big changes in your family?",
  "12. Have you been facing big changes in regards to your everyday life (ex. new school)?",
  "13. Do you often regret the decisions you make and look back at what could be done better?",
  "14. Do you dislike trying new things and getting out of your comfort zone?",
  "15. Do you like to look at the negative sides of things when facing issues in your everyday life?",
  "16. When faced with severe adversity, do you often back down easily?",
  "17. Do you despise going to school or work?",
  "18. Your friends and family don’t support you when it comes to achieving goals in regards to post-secondary education (yes they don’t support me; no they do support me)?",
  "19. Do you or your family members set high standards for you and your achievements?",
  "20. Do you dislike the life you live?",
];
const stress = [0, 7, 7, 4, 5, 0, 0, 3, 1, 6, 3, 2, 0, 2, 0, 0, 4, 6, 7, 2];
// Totals allow for the values in each array to be added and set to a individual variable
let stressTotal = 0;
const depression = [0, 2, 2, 0, 1, 5, 3, 3, 0, 3, 5, 2, 0, 2, 2, 1, 5, 3, 1, 5];
let depressionTotal = 0;
const anxiety = [5, 3, 3, 1, 5, 5, 6, 3, 0, 2, 2, 0, 5, 4, 2, 2, 5, 4, 2, 4];
let anxietyTotal = 0;
const pessimism = [1, 0, 0, 4, 0, 0, 2, 3, 0, 0, 0, 2, 8, 2, 9, 6, 6, 0, 0, 7];
let pessimismTotal = 0;

const surveyData = {
  stress: null,
  depression: null,
  anxiety: null,
  pessimism: null,
};

let questionNumber = 0;

document.getElementById("yes").addEventListener("click", yesClick);

function yesClick() {
  if (questionNumber == 19) {
    submitForm();
  } else {
    questionNumber += 1;
    stressTotal = stressTotal + stress[questionNumber];
    depressionTotal = depressionTotal + depression[questionNumber];
    anxietyTotal = anxietyTotal + anxiety[questionNumber];
    pessimismTotal = pessimismTotal + pessimism[questionNumber];
    document.getElementById("questionText").innerHTML =
      questions[questionNumber];
  }
}

document.getElementById("no").addEventListener("click", noClick);

function noClick() {
  if (questionNumber == 19) {
    submitForm();
  } else {
    questionNumber += 1;
    document.getElementById("questionText").innerHTML =
      questions[questionNumber];
  }
}

function displayHeatmap() {
  document.getElementById("tiltWrapper").style.display = "none";
  document.getElementById("heatMap").style.display = "flex";
}

function submitForm() {
  stressPercentage = (stressTotal / 59) * 100;
  depressionPercentage = (depressionTotal / 45) * 100;
  anxietyPercentage = (anxietyTotal / 63) * 100;
  pessimismPercentage = (pessimismTotal / 50) * 100;
  surveyData["pessimism"] = 255 * (pessimismPercentage / 100);
  surveyData["anxiety"] = 255 * (anxietyPercentage / 100);
  surveyData["depression"] = 255 * (depressionPercentage / 100);
  surveyData["stress"] = 255 * (stressPercentage / 100);
  setup(surveyData);
  displayHeatmap();
}
