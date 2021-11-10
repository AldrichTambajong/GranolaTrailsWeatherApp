import React from 'react'
// import { Link } from 'react-router-dom'

function ActivityList() {
    const listOfActivities = ["Talluah Gorge", "Blood Mountain", "Camp Creek Park", "Bouldering", "Amicaola Falls"]

    return (
        <div >
            <h2> Recommended Activities </h2>
            {listOfActivities.map((item, index) => (
                <li key={item}>
                    {item}
                </li>
            ))}
        </div>
    )
}

export default ActivityList
