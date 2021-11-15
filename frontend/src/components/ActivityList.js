import { React, useState, useEffect } from 'react'
import { Card, Button, Container, Row, Col } from "react-bootstrap"

function ActivityList(props) {

    let activities = {
        'user_state': props.userState
    }

    // let rendered = false;

    // let listOfActivities = ''
    const [listOfActivities, setListOfActivities] = useState([])

    // componentDidMount(){

    // }

    useEffect(() => {
        fetch('/parks', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(activities)
        })
            .then(response => response.json())
            .then((data) => {
                setListOfActivities([...data])
            })
    }, [])



    console.log(listOfActivities)

    // const listOfActivities = response.json()

    // description: "Big enough to be overwhelming, still intimate enough to feel the pulse of time, Black Canyon of the Gunnison exposes you to some of the steepest cliffs, oldest rock, and craggiest spires in North America. With two million years to work, the Gunnison River, along with the forces of weathering, has sculpted this vertical wilderness of rock, water, and sky."
    // id: "BDBD573F-97EF-44E7-A579-471679F2C42A"
    // img: "https://www.nps.gov/common/uploads/structured_data/3C81655F-1DD8-B71B-0B4BCFFDB74EE723.jpg"
    // name: "Black Canyon Of The Gunnison National Park"
    // url: "https://www.nps.gov/blca/index.htm"
    // weather:
    // clouds: 100
    // condition: "Clouds"
    // precipitation: 0
    // temperature: 51.39

    // const listOfActivities =
    //     [{
    //         "park_name": "Talluah Gorge",
    //         "park_temp": 40,
    //         "park_precipitation": 10,
    //         "park_cloud_coverage": 20,
    //         "park_condition": "cloudy",
    //         "Park_URL": "https://www.atlantatrails.com/hiking-trails/wooded-serenity-the-appalachian-trail-at-blood-mountain/",
    //         "park_image": "https://www.exploregeorgia.org/sites/default/files/styles/slideshow_large/public/2019-02/tallulah-gorge-thegreatoutdoorsphoto-instagram.jpg?itok=mq1BQs3M",
    //         "Park_Description": "Big rocks and big waterfall, come here!"
    //     },
    //     {
    //         "park_name": "blood mountain",
    //         "park_temp": 5,
    //         "park_precipitation": 10,
    //         "park_cloud_coverage": 30,
    //         "park_condition": "Windy",
    //         "Park_URL": "https://www.atlantatrails.com/hiking-trails/wooded-serenity-the-appalachian-trail-at-blood-mountain/",
    //         "park_image": "https://www.atlantatrails.com/wp-content/uploads/2019/02/blood-mountain-loop-hiking-appalachian-trail-freeman-trail-1024x683.jpg",
    //         "Park_Description": "Big mountain!"

    //     },
    //     {
    //         "park_name": "vogel state park",
    //         "park_temp": 5,
    //         "park_precipitation": 10,
    //         "park_cloud_coverage": 30,
    //         "park_condition": "Windy",
    //         "Park_URL": "https://www.atlantatrails.com/hiking-trails/wooded-serenity-the-appalachian-trail-at-blood-mountain/",
    //         "park_image": "https://www.atlantatrails.com/wp-content/uploads/2018/08/trahlyta-lake-trail-vogel-state-park-06.jpg",
    //         "Park_Description": "Waterfall!"

    //     },
    //     {
    //         "park_name": "Providence Canyon State Park",
    //         "park_temp": 5,
    //         "park_precipitation": 10,
    //         "park_cloud_coverage": 30,
    //         "park_condition": "Windy",
    //         "Park_URL": "https://www.atlantatrails.com/hiking-trails/wooded-serenity-the-appalachian-trail-at-blood-mountain/",
    //         "park_image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Providence_Canyon_from_rim.jpg/1200px-Providence_Canyon_from_rim.jpg",
    //         "Park_Description": "Big mountain!"

    //     },

    //     ]

    return (
        <Container>
            <Row>
                {listOfActivities.map((item, index) => (
                    <Col>
                        <Card key={index} style={{ width: '18rem' }}>
                            <Card.Img variant="top" src={item["img"]} />
                            <Card.Body>
                                <Card.Title>{item["name"]}</Card.Title>
                                <Card.Text>
                                    Temperature: {item["weather"]["temperature"]}° Farenheight
                                    <br />
                                    Precipitation: {item["weather"]["precipitation"]}%
                                    <br />
                                    Cloud Coverage: {item["weather"]["clouds"]}%
                                    <br />
                                    Condition: {item["weather"]["condition"]}
                                    <br />
                                    {item["description"]}
                                    {/* // description: "Big enough to be overwhelming, still intimate enough to feel the pulse of time, Black Canyon of the Gunnison exposes you to some of the steepest cliffs, oldest rock, and craggiest spires in North America. With two million years to work, the Gunnison River, along with the forces of weathering, has sculpted this vertical wilderness of rock, water, and sky."
                                    // id: "BDBD573F-97EF-44E7-A579-471679F2C42A"
                                    // img: "https://www.nps.gov/common/uploads/structured_data/3C81655F-1DD8-B71B-0B4BCFFDB74EE723.jpg"
                                    // name: "Black Canyon Of The Gunnison National Park"
                                    // url: "https://www.nps.gov/blca/index.htm"
                                    // weather:
                                    // clouds: 100
                                    // condition: "Clouds"
                                    // precipitation: 0
                                    // temperature: 51.39 */}
                                    {/* user state = {localStorage.getItem("user_state")} */}
                                </Card.Text>
                                <Button variant="primary" onClick={() => {
                                    window.location.href = item["Park_URL"];
                                    return null;
                                }}>Go To Site</Button>
                            </Card.Body>
                        </Card>
                    </Col>
                ))}
            </Row>
        </Container>
    )
}

export default ActivityList
