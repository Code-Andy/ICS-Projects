//npm to setup webpack firebase and tiltjs

document
  .getElementById("startContainer")
  .addEventListener("click", clickToLogin);

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

function clickToLogin() {
  document.getElementById("welcome").innerHTML = "Login in with Google";
  document.getElementById("welcome").style.fontSize = 35 + "px";
  document.getElementById("welcome").style.fontStyle = "normal";
  document.getElementById("welcome").style.fontWeight = 500;
  document.getElementById("googleLogo").style.display = "flex";

  fadeElement("googleLogo");
  fadeElement("welcome");
}

let activePage = "homePage";
let lastActive = "";

document.getElementById("ourProject").addEventListener("click", aboutPage);

document.getElementById("dotLogo").addEventListener("click", homePage);

function aboutPage() {
  document.getElementById("aboutPage").style.display = "flex";
  document.getElementById("homePage").style.display = "none";
  lastActive = activePage;
  activePage = "aboutPage";
}

function homePage() {
  document.getElementById("aboutPage").style.display = "none";
  document.getElementById("homePage").style.display = "flex";
  lastActive = activePage;
  activePage = "homePage";
}

VanillaTilt.init(document.getElementById("questionPage"), {
  max: 25,
  speed: 400,
});
