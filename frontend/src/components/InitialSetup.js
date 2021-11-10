import React from 'react'

function ActivityList() {
    return (
        <div >
            <h1> Account Creation </h1>
            <h2> Where are you from? </h2>

            <select class="form-select" aria-label="Default select example">
                <option selected>Choose your State (Abbreviated)</option>
                <option value="1">AL</option>
                <option value="2">AK</option>
                <option value="3">AZ</option>
                <option value="4">AR</option>
                <option value="5">CA</option>
                <option value="6">CO</option>
                <option value="7">CT</option>
                <option value="8">DE</option>
                <option value="9">FL</option>
                <option value="10">GA</option>
                <option value="11">HI</option>
                <option value="12">ID</option>
                <option value="13">IL</option>
                <option value="14">IN</option>
                <option value="15">IA</option>
                <option value="16">KS</option>
                <option value="17">KY</option>
                <option value="18">LA</option>
                <option value="19">ME</option>
                <option value="20">MD</option>
                <option value="21">MN</option>
                <option value="22">MS</option>
                <option value="23">MO</option>
                <option value="24">MT</option>
                <option value="25">NE</option>
                <option value="26">NV</option>
                <option value="27">NH</option>
                <option value="28">NJ</option>
                <option value="29">NM</option>
                <option value="30">NY</option>
                <option value="31">NC</option>
                <option value="32">ND</option>
                <option value="33">OH</option>
                <option value="34">OK</option>
                <option value="35">OR</option>
                <option value="36">PA</option>
                <option value="37">RI</option>
                <option value="38">SC</option>
                <option value="39">SD</option>
                <option value="40">TN</option>
                <option value="41">TX</option>
                <option value="42">UT</option>
                <option value="43">VT</option>
                <option value="44">VA</option>
                <option value="45">WA</option>
                <option value="46">WV</option>
                <option value="47">WI</option>
                <option value="48">WY</option>
            </select>

            <h2> What are your favorite activities? </h2>
            <div class="form-check">
                <input class="form-check-input" type="checkbox" value="" id="checkHiking"></input>
                <label class="form-check-label" for="checkHiking">
                    Hiking
                </label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="checkbox" value="" id="checkOffroading"></input>
                <label class="form-check-label" for="checkOffroading">
                    Offroading
                </label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="checkbox" value="" id="checkFishing"></input>
                <label class="form-check-label" for="checkFishing">
                    Fishing
                </label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="checkbox" value="" id="checkBouldering"></input>
                <label class="form-check-label" for="checkBouldering">
                    Bouldering
                </label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="checkbox" value="" id="checkCamping"></input>
                <label class="form-check-label" for="checkCamping">
                    Camping
                </label>
            </div>

            <input class="btn btn-primary" type="submit" value="Submit"></input>

        </div>
    )
}

export default ActivityList
