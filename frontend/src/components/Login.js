import React from "react";
import { useState } from "react";
function Login(props) {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState(false);
    function submit(e) {
        let user = {
            email: email,
            password: password,
        };
        // Obtains response from /login route in app
        fetch("/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(user),
        })
            .then((response) => response.json())
            .then((data) => {
                // Based on response, checks to see whether the user provided valid user id or not
                if (data.login === "valid") {
                    // Need both setItem and state variable method (i.e setName) declared
                    // setItem used to make the storage variable

                    localStorage.setItem("email", data.email);
                    // window.localStorage.setItem('string', "stored string")

                    sessionStorage.setItem("state", data.user_state);
                    sessionStorage.setItem("loggedIn", true);
                    // State variables WILL NOT CHANGE unless changed using their setChange methods.
                    // if props.setChange() isn't used, there will be an empty value for the props variable
                    // (take props.setName(sessionStorage.getItem("name")) out and login for example)
                    // props.setName(sessionStorage.getItem("name"))
                    props.setLoggedIn(sessionStorage.getItem("loggedIn"));
                    props.setUserState(data.user_state);
                } else {
                    setError(true);
                }
            });
        e.preventDefault();
    }

  return (
    
    <div>
    <h1>Granola Travels</h1>
    <p>Planning the next outdoor adventure.</p>
      <div className='login-container'>
        <form method='POST' onSubmit={(e) => submit(e)}>
          <div className='inputDiv'>
            {/* <label>Email:</label> */}
            <br />
            <input
              type='text'
              name='email'
              placeholder='Enter email'
              className='inputCenter'
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>
          <div className='inputDiv'>
            {/* <label>Password:</label> */}
            <br />
            <input
              type='password'
              name='password'
              placeholder='Enter password'
              className='inputCenter'
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>
        {/* <div class = "text-center mb-3"> */}
          <br />
          <br />
          {/* <input type='submit' value='Login'/> */}
          <div class="text-center mb-3">
            <button type="submit" class="btn btn-success login-btn mb-3">Login</button>
            <br />
        </div>
        {/* </div> */}
        </form>
      </div>
      <div className='suggest'>
        {error === true ? (
          <p style={{ color: "red" }}>Incorrect email or password</p>
        ) : (
          <p></p>
        )}
       
      </div>
      <script src='/static/script.js'></script>
    </div>
  );
}

export default Login;
