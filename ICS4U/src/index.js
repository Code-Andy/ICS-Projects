// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getFirestore, collection, getDocs, addDoc } from "firebase/firestore";

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

initializeApp(firebaseConfig);

const db = getFirestore();

// collection ref
const colRef = collection(db, "books");

// get collection data
getDocs(colRef)
  .then((snapshot) => {
    // console.log(snapshot.docs)
    let books = [];
    snapshot.docs.forEach((doc) => {
      books.push({ ...doc.data(), id: doc.id });
    });
    console.log(books);
  })
  .catch((err) => {
    console.log(err.message);
  });

const addValues = document.querySelector(".add");

document.getElementById("add").addEventListener("submit", submitForm);

function submitForm(e) {
  e.preventDefault();
  var value1 = getFormValues("val1");
  var value2 = getFormValues("val2");
  var value3 = getFormValues("val3");
  var value4 = getFormValues("val4");
  console.log(value1, value2, value3, value4);
  addDoc(colRef, {
    val1: value1,
    val2: value2,
    val3: value3,
    val4: value4,
  });

  // .then(() => {
  //   addValues.reset();
  // });
}

function getFormValues(id) {
  return document.getElementById(id).value;
}

// addValues.addEventListener("submit", (e) => {
//   e.preventDefault();
//   console.log(addValues.val1.data);

// });
