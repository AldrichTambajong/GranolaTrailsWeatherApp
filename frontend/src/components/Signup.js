import React from 'react'
import {useState} from 'react'

function Signup(props) {
    const [error,setError] = useState('') // Shows error message upon invalid info being registered
    const [flag,setFlag] = useState() // Condition for showing error message shown below
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [firstName,setFirstName] = useState('')
    const[lastName,setLastname] = useState('')

    function register(e){
        // Json object passed as body fetch methods with POST can be passed a body
        let newUser = {
            'email': email,
            'password': password,
            'firstName':firstName,
            'lastName':lastName
        }
        fetch('/signUp',{
            method:'POST',
            headers:{
                'Content-Type':'application/json'
            },
            body:JSON.stringify(newUser)
        })
        .then(response => response.json())
        .then((data) => {
            console.log(data)
            // Sets setSignedUp to true to redirect to login page
            if(data.status === 200){
                props.setSignedUp(true)
            }
            // Shows error message
            else{
                setFlag(true)
                setError(data.message)
            }
        })
        // Prevents json object from showing up on blank page instead of expected output
        // (based on my experience)
        e.preventDefault()
    }
    return (
        <div>
            <div className="signUp">
                <form method = "POST" onSubmit={e => register(e)}>
                    <h2>Create an account</h2>
                    <div class ="signUpInput">
                        <label>First Name:</label>
                        <br/>
                        <input type="text" name="firstName" placeholder="first name" value={firstName} onChange={e => setFirstName(e.target.value)}/>
                    </div>
                    <div class ="signUpInput">
                        <label>Last Name:</label>
                        <br/>
                        <input type="text" name="lastName" placeholder="last name" value={lastName} onChange={e => setLastname(e.target.value)}/>
                    </div>
                    <div class ="signUpInput">
                        <label>Email:</label>
                        <br/>
                        <input type="email" name="email" placeholder="email" value={email} onChange={e => setEmail(e.target.value)}/>
                    </div>
                    <div class ="signUpInput">
                        <label>Password:</label>
                        <br/>
                        <input type="password" name="password" placeholder="password" value={password} onChange={e => setPassword(e.target.value)}/>
                    </div>
                    <input type="submit" value="Sign Up" style={{marginLeft: "auto" ,marginRight: "auto"}}></input>
                </form>
            </div>
            {/*Displays error message*/}
            <div className="accErrMess">
                {flag === true?
                    <p style={{color:"red"}}>{error}</p>
                :
                    <p></p>
                }
            </div>
        </div>
    )
}

export default Signup
