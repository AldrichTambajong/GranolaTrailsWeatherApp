import React, { useEffect } from 'react'
import { Card, Button, Container, Row, Col } from "react-bootstrap"
import { Link } from 'react-router-dom'

function ActivityList() {
    const listOfActivities =
        [{
            "park_name": "Talluah Gorge",
            "park_temp": 40,
            "park_precipitation": 10,
            "park_cloud_coverage": 20,
            "park_condition": "cloudy",
            "Park_URL": "https://www.atlantatrails.com/hiking-trails/wooded-serenity-the-appalachian-trail-at-blood-mountain/",
            "park_image": "https://www.exploregeorgia.org/sites/default/files/styles/slideshow_large/public/2019-02/tallulah-gorge-thegreatoutdoorsphoto-instagram.jpg?itok=mq1BQs3M",
            "Park_Description": "Big rocks and big waterfall, come here!"
        },
        {
            "park_name": "blood mountain",
            "park_temp": 5,
            "park_precipitation": 10,
            "park_cloud_coverage": 30,
            "park_condition": "Windy",
            "Park_URL": "https://www.atlantatrails.com/hiking-trails/wooded-serenity-the-appalachian-trail-at-blood-mountain/",
            "park_image": "https://www.atlantatrails.com/wp-content/uploads/2019/02/blood-mountain-loop-hiking-appalachian-trail-freeman-trail-1024x683.jpg",
            "Park_Description": "Big mountain!"

        },
        {
            "park_name": "vogel state park",
            "park_temp": 5,
            "park_precipitation": 10,
            "park_cloud_coverage": 30,
            "park_condition": "Windy",
            "Park_URL": "https://www.atlantatrails.com/hiking-trails/wooded-serenity-the-appalachian-trail-at-blood-mountain/",
            "park_image": "https://www.atlantatrails.com/wp-content/uploads/2018/08/trahlyta-lake-trail-vogel-state-park-06.jpg",
            "Park_Description": "Waterfall!"

        },
        {
            "park_name": "Providence Canyon State Park",
            "park_temp": 5,
            "park_precipitation": 10,
            "park_cloud_coverage": 30,
            "park_condition": "Windy",
            "Park_URL": "https://www.atlantatrails.com/hiking-trails/wooded-serenity-the-appalachian-trail-at-blood-mountain/",
            "park_image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Providence_Canyon_from_rim.jpg/1200px-Providence_Canyon_from_rim.jpg",
            "Park_Description": "Big mountain!"

        },

        ]

    // park: 
    //     weather: 
    //         temperature:
    //         precipitation:
    //         cloud coverage:
    //     Park URL official page:
    //     Description:


    return (
        <Container>
            <Row>
                {listOfActivities.map((item, index) => (
                    <Col>
                        <Card style={{ width: '18rem' }}>
                            <Card.Img variant="top" src={item["park_image"]} />
                            <Card.Body>
                                <Card.Title>{item["park_name"]}</Card.Title>
                                <Card.Text>
                                    Temperature: {item["park_temp"]}° Farenheight
                                    <br />
                                    Precipitation: {item["park_precipitation"]}%
                                    <br />
                                    Cloud Coverage: {item["park_cloud_coverage"]}%
                                    <br />
                                    Condition: {item["park_condition"]}
                                    <br />
                                    {item["Park_Description"]}
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
