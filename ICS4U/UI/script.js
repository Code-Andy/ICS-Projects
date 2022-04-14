document
  .getElementById("startContainer")
  .addEventListener("click", clickToLogin);

function clickToLogin() {
  document.getElementById("welcome").innerHTML = "Login in with Google";
  document.getElementById("welcome").style.fontSize = 35 + "px";
  document.getElementById("welcome").style.fontStyle = "normal";
  document.getElementById("welcome").style.fontWeight = 300;
  document.getElementById("logo").style.display = "flex";
  document.getElementById("logo").animate(
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

  document.getElementById("welcome").animate(
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
