import React from 'react'
import { useState } from 'react'
function Login(props) {
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [error, setError] = useState(false)
    function submit(e) {
        let user = {
            'email': email,
            'password': password
        }
        // Obtains response from /login route in app
        fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(user)
        })
            .then(response => response.json())
            .then((data) => {
                // Based on response, checks to see whether the user provided valid user id or not
                console.log(data)
                if (data.login === "valid") {
                    console.log("user state " + data.user_state)
                    // Need both setItem and state variable method (i.e setName) declared
                    // setItem used to make the storage variable

                    localStorage.setItem("email", data.email)
                    console.log("user state in login.js" + localStorage.getItem('user_state'))
                    // window.localStorage.setItem('string', "stored string")

                    sessionStorage.setItem('state', data.user_state)
                    sessionStorage.setItem('loggedIn', true)
                    // State variables WILL NOT CHANGE unless changed using their setChange methods.
                    // if props.setChange() isn't used, there will be an empty value for the props variable
                    // (take props.setName(sessionStorage.getItem("name")) out and login for example)
                    // props.setName(sessionStorage.getItem("name"))
                    props.setLoggedIn(sessionStorage.getItem('loggedIn'))
                    props.setUserState(data.user_state)
                    // console.log("logged in = " + sessionStorage.getItem('loggedIn'))

                    // console.log("email = " + email)
                }
                else {
                    setError(true)
                }
            })
        e.preventDefault()
    }


    return (
        <div>
            <div className="login-container">
                <form method="POST" onSubmit={(e) => submit(e)}>
                    <h2>Login</h2>
                    <div className="inputDiv">
                        <label>Email:</label>
                        <br />
                        <input type="email" name="email" placeholder="email" className="inputCenter"
                            value={email} onChange={e => setEmail(e.target.value)} />
                    </div>
                    <div className="inputDiv">
                        <label>Password:</label>
                        <br />
                        <input type="password" name="password" placeholder="password" className="inputCenter"
                            value={password} onChange={e => setPassword(e.target.value)} />
                    </div>
                    <input type="submit" value="Login" />
                </form>
            </div>
            <div className="suggest">
                {error === true ?
                    <p style={{ color: "red" }}>Incorrect email or password</p>
                    :
                    <p></p>
                }
            </div>
            <script src="/static/script.js">

            </script>
        </div>
    )
}

export default Login
