import React from 'react'
// import { Link } from 'react-router-dom'

function ActivityMonitor() {
    const hiking = "Good to Hike!"
    const offroading = "Can't go Off-roading."
    const bouldering = "Good to go bouldering!"
    const fishing = "Good to go fishing!"
    const camping = "Good to go camping!"

    return (
        <div>
            <h2>Activity Monitor</h2>
            {hiking}
            <br />
            {offroading}
            <br />
            {bouldering}
            <br />
            {fishing}
            <br />
            {camping}
        </div>
    )
}

export default ActivityMonitor
