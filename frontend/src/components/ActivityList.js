import { React, useState, useEffect } from 'react'
import { Card, Button, Container, Row, Col } from "react-bootstrap"

function ActivityList(props) {

    let activities = {
        'user_state': props.userState
    }

    const [listOfActivities, setListOfActivities] = useState([])

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
