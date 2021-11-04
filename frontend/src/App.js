import './App.css';
import {BrowserRouter as Router, Route, Routes, Navigate, NavLink} from 'react-router-dom'
import { useState } from 'react';
import "bootstrap/dist/css/bootstrap.min.css"
import Navbar from './components/Navbar';
import Login from './components/Login';
import Signup from './components/Signup';

function App() {
  const [loggedIn,setLoggedIn] = useState(sessionStorage.getItem('loggedIn'))
  const [signedUp,setSignedUp] = useState()
  return (
      <div className="App">
        <Router>
          <Routes>
            <Route path="" element={<Navigate to="/login"></Navigate>}/>

            <Route path="/login" element={
              loggedIn === "true"?
              <Navigate to="/home"></Navigate>
              :
              <div>
                <Login></Login>
                <div className="signUpLink">
                  <p>Don't have an account?</p>
                  <NavLink to="/signUp">Sign Up</NavLink>
                </div>
              </div>
            }></Route>

            <Route path="/home" element={
              <div>
                <Navbar></Navbar>
              </div>
            }></Route>

            <Route path="/signUp" element={
              signedUp === true?
              <Navigate to ="/login"></Navigate>
              :
              <div>
                <Signup setSignedUp={setSignedUp}></Signup>
                <div className="loginLink">
                  <p>Already have an account?</p>
                  <NavLink to="/login">Login</NavLink>
                </div>
              </div>
            }></Route>

          </Routes>
        </Router>
      </div>
  );
}

export default App;
