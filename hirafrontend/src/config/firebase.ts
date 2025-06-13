// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// import { getAnalytics } from "firebase/analytics";
import { getAuth } from "firebase/auth";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCPCfgYM6jiol-T6AzB5sxSxmMWXiN9K0Q",
  authDomain: "hira-application-75c25.firebaseapp.com",
  projectId: "hira-application-75c25",
  storageBucket: "hira-application-75c25.firebasestorage.app",
  messagingSenderId: "779215956668",
  appId: "1:779215956668:web:2e2e63285c4bac07ddbeb9",
  measurementId: "G-S4LYFPTBD3"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
// const analytics = getAnalytics(app);


export const auth = getAuth(app);