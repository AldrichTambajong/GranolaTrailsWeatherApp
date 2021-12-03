import React from 'react'
import { useState } from 'react'
import { Form } from 'react-bootstrap'

function Signup(props) {
    const [error, setError] = useState('') // Shows error message upon invalid info being registered
    const [flag, setFlag] = useState() // Condition for showing error message shown below
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [location, setLocation] = useState('')
    const [hiking, setHiking] = useState(false)
    const [offroading, setOffroading] = useState(false)
    const [fishing, setFishing] = useState(false)
    const [bouldering, setBouldering] = useState(false)
    const [camping, setCamping] = useState(false)

    function register(e) {
        // Json object passed as body fetch methods with POST can be passed a body
        let newUser = {
            'email': email,
            'password': password,
            'user_state': location,
            'hiking': hiking,
            'fishing': fishing,
            'offroad': offroading,
            'camping': camping,
            'bouldering': bouldering
        }


        fetch('/signUp', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(newUser)
        })
            .then(response => response.json())
            .then((data) => {
                // Sets setSignedUp to true to redirect to login page
                if (data.status === 200) {
                    props.setSignedUp(true)
                }
                // Shows error message
                else {
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
            <h1>Create Account</h1>
            <div className="signUp">
                <form method="POST" onSubmit={e => register(e)}>
                    <div class="signUpInput">
                        <input type="email" name="email" placeholder="Enter Email" style = {{width: "250px"}} value={email} onChange={e => setEmail(e.target.value)} />
                    </div>
                    <br />
                    <br />
                    <div class="signUpInput">
                        <input type="password" name="password" placeholder="Enter Password" style = {{width: "250px"}} value={password} onChange={e => setPassword(e.target.value)} />
                    </div>
                    <br />
                    <br />
                    {/* <Form.Group class="form-select" aria-label="Default select example"> */}
                        <Form.Control
                            class="form-select" 
                            aria-label="Default select example"
                            as="select"
                            value={location}
                            onChange={e => {
                                setLocation(e.target.value);
                            }}
                        >
                            <option selected>Choose your State</option>
                            <option value="AL">Alabama</option>
                            <option value="AK">Alaska</option>
                            <option value="AZ">Arizona</option>
                            <option value="AR">Arkansas</option>
                            <option value="CA">California</option>
                            <option value="CO">Colorado</option>
                            <option value="CT">Connecticuit</option>
                            <option value="DE">Delaware</option>
                            <option value="FL">Florida</option>
                            <option value="GA">Georgia</option>
                            <option value="HI">Hawaii</option>
                            <option value="ID">Idaho</option>
                            <option value="IL">Illinois</option>
                            <option value="IN">Indiana</option>
                            <option value="IA">Iowa</option>
                            <option value="KS">Kansas</option>
                            <option value="KY">Kentucky</option>
                            <option value="LA">Louisiana</option>
                            <option value="ME">Maine</option>
                            <option value="MD">Maryland</option>
                            <option value="MN">Minnesota</option>
                            <option value="MS">Mississippi</option>
                            <option value="MO">Missouri</option>
                            <option value="MT">Montana</option>
                            <option value="NE">Nebraska</option>
                            <option value="NV">Nevada</option>
                            <option value="NH">New Hampshire</option>
                            <option value="NJ">New Jersey</option>
                            <option value="NM">New Mexico</option>
                            <option value="NY">New York</option>
                            <option value="NC">North Carolina</option>
                            <option value="ND">North Dakota</option>
                            <option value="OH">Ohio</option>
                            <option value="OK">Oklahoma</option>
                            <option value="OR">Oregon</option>
                            <option value="PA">Pennsylvania</option>
                            <option value="RI">Rhode Island</option>
                            <option value="SC">South Carolina</option>
                            <option value="SD">South Dakota</option>
                            <option value="TN">Tennessee</option>
                            <option value="TX">Texas</option>
                            <option value="UT">Utah</option>
                            <option value="VT">Vermont</option>
                            <option value="VA">Virginia</option>
                            <option value="WA">Washigton</option>
                            <option value="WV">West Virginia</option>
                            <option value="WI">Wisconinsin</option>
                            <option value="WY">Wyoming</option>
                        </Form.Control>
                    {/* </Form.Group> */}
                    <br />
                    <br />
                    <p>Choose your favorite Activities:</p>
                    <Form.Group class="form-check">
                        <input class="form-check-input" type="checkbox" value={hiking} id="checkHiking" onChange={(e) => {
                            setHiking(true);
                        }}></input>
                        <label class="form-check-label" for="checkHiking">
                            Hiking
                        </label>
                    </Form.Group>
                    <Form.Group class="form-check">
                        <input class="form-check-input" type="checkbox" value={offroading} id="checkOffroading" onChange={(e) => {
                            setOffroading(true);
                        }}></input>
                        <label class="form-check-label" for="checkOffroading">
                            Offroading
                        </label>
                    </Form.Group>
                    <Form.Group class="form-check">
                        <input class="form-check-input" type="checkbox" value={fishing} id="checkFishing" onChange={(e) => {
                            setFishing(true);
                        }}></input>
                        <label class="form-check-label" for="checkFishing">
                            Fishing
                        </label>
                    </Form.Group>
                    <Form.Group class="form-check">
                        <input class="form-check-input" type="checkbox" value={bouldering} id="checkBouldering" onChange={(e) => {
                            setBouldering(true);
                        }}></input>
                        <label class="form-check-label" for="checkBouldering">
                            Bouldering
                        </label>
                    </Form.Group>
                    <Form.Group class="form-check">
                        <input class="form-check-input" type="checkbox" value={camping} id="checkCamping" onChange={(e) => {
                            setCamping(true);
                        }}></input>
                        <label class="form-check-label" for="checkCamping">
                            Camping
                        </label>
                    </Form.Group>
                    <br />
                    <br />
                    {/* <input type="submit" value="Sign Up" style={{ marginLeft: "auto", marginRight: "auto" }}></input> */}
                    <div class="text-center mb-3">
                        <button type="submit" class="btn btn-success login-btn mb-3">Sign Up</button>
                    </div>
                </form>
            </div>
            {/*Displays error message*/}
            <div className="accErrMess">
                {flag === true ?
                    <p style={{ color: "red" }}>{error}</p>
                    :
                    <p></p>
                }
            </div>
        </div>
    )
}

export default Signup
