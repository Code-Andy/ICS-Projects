// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getFirestore, collection, getDocs, addDoc } from "firebase/firestore";
import { getAuth, signInWithPopup, GoogleAuthProvider } from "firebase/auth";

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyASZgii0k99yeGB1vaIxaXHkWAZgH4CmQU",
  authDomain: "dot-test-1de86.firebaseapp.com",
  projectId: "dot-test-1de86",
  storageBucket: "dot-test-1de86.appspot.com",
  messagingSenderId: "266594375880",
  appId: "1:266594375880:web:07db376ec0107afe882dfd",
  measurementId: "G-9VP86KXK57",
};

// starts the firebase webapp
initializeApp(firebaseConfig);

// starts the firestore database
const db = getFirestore();
// starts the google auth

const provider = new GoogleAuthProvider();
provider.addScope("https://www.googleapis.com/auth/contacts.readonly");

const auth = getAuth();

document.getElementById("signIn").addEventListener("click", logIn);

function logIn() {
  signInWithPopup(auth, provider)
    .then((result) => {
      // This gives you a Google Access Token. You can use it to access the Google API.
      const credential = GoogleAuthProvider.credentialFromResult(result);
      const token = credential.accessToken;
      // The signed-in user info.
      const user = result.user;
      console.log(user);
      // ...
    })
    .catch((error) => {
      // Handle Errors here.
      const errorCode = error.code;
      const errorMessage = error.message;
      // The email of the user's account used.
      const email = error.email;
      // The AuthCredential type that was used.
      const credential = GoogleAuthProvider.credentialFromError(error);
      // ...
    });
}

// collection ref
const colRef = collection(db, "values");

window.x = []; //need to use dictionary
window.y = [];

//function to pull data out of the ref and add it into local server variables
getDocs(colRef)
  .then((snapshot) => {
    let values = [];
    snapshot.docs.forEach((doc) => {
      values.push(doc.data());
    });
    //push all elements (firebase dict) into a new array
    for (let x = 0; x < Object.keys(values).length; x++) {
      window.x.push(values[x].val1);
      window.y.push(values[x].val2);
    }
  })
  .catch((err) => {
    console.log(err.message);
  });

//listener for button press
document.getElementById("add").addEventListener("submit", submitForm);

//takes form data and adds it to firebase and website array
function submitForm(e) {
  e.preventDefault();
  window.x.push(shortAlgo(getFormValues("val1")));
  window.y.push(shortAlgo(getFormValues("val2")));
  addDoc(colRef, {
    val1: shortAlgo(getFormValues("val1")),
    val2: shortAlgo(getFormValues("val2")),
  });
  document.getElementById("add").reset();
}

// converts simple -10 - 10 input and maps it to 0 - 400
function shortAlgo(factor) {
  let coordinate = (10 + Number(factor)) * 20;
  return coordinate;
}

// gets values from documents within 'add'
function getFormValues(id) {
  return document.getElementById(id).value;
}

//REFERENCE getDocs. delete whenever

// Get data from firestore with id value
// getDocs(colRef)
//   .then((snapshot) => {
//     // console.log(snapshot.docs)
//     let values = [];
//     snapshot.docs.forEach((doc) => {
//       values.push({ ...doc.data(), id: doc.id });
//     });
//     console.log(values);
//   })
//   .catch((err) => {
//     console.log(err.message);
//   });
