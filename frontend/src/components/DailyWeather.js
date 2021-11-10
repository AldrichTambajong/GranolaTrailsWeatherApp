import React from 'react'
// import { Link } from 'react-router-dom'

function DailyWeather() {
    const temperature = "53"
    const condition = "sunny"
    const high = "70"
    const low = "30"

    return (
        <div>
            <h2>Current Conditions</h2>
            Current Temp: {temperature}
            <br />
            Condition: {condition}
            <br />
            High: {high}
            <br />
            Low: {low}
        </div>
    )
}

export default DailyWeather
