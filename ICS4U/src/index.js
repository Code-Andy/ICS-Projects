// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getFirestore, collection, getDoc, addDoc } from "firebase/firestore";

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
getDoc(colRef)
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

addValues.addEventListener("submit", (e) => {
  e.preventDefault();
  await addDoc(colRef, {
    val1: addValues.val1.number,
    val2: addValues.val2.number,
    val3: addValues.val3.number,
    val4: addValues.val4.number,
  }).then(() => {
    addValues.reset();
  });
});
