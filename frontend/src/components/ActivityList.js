import { React, useState, useEffect } from "react";
import { Card, Button, Container, Row, Col, Spinner } from "react-bootstrap";

function ActivityList(props) {
  let activities = {
    user_state: props.userState,
  };

  const [listOfActivities, setListOfActivities] = useState([]);

  useEffect(() => {
    fetch("/parks", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(activities),
    })
      .then((response) => response.json())
      .then((data) => {
        setListOfActivities([...data]);
      });
    console.log(listOfActivities);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  if (listOfActivities.length !== 0) {
    return (
      <Container>
        <Row>
          {listOfActivities.map((item, index) => (
            <Col>
              <Card key={index} style={{ width: "18rem" }}>
                <Card.Img variant='top' src={item["img"]} />
                <Card.Body>
                  <Card.Title>{item["name"]}</Card.Title>
                  <Card.Text>
                    <p>
                      <b>Temperature:</b> {item["weather"]["temperature"]}° F
                    </p>
                    <p>
                      <b>Precipitation:</b> {item["weather"]["precipitation"]}%
                    </p>
                    <p>
                      <b>Cloud Coverage:</b> {item["weather"]["clouds"]}%
                    </p>
                    <p>
                      <b>Condition:</b> {item["weather"]["condition"]}
                    </p>
                    {item["description"]}
                  </Card.Text>
                  <Button
                    variant='primary'
                    onClick={() => {
                      console.log(item);
                      window.open(item["url"], "_blank");
                      return null;
                    }}>
                    Go To Site
                  </Button>
                </Card.Body>
              </Card>
            </Col>
          ))}
        </Row>
      </Container>
    );
  } else {
    return (
      <Spinner animation='border' role='status' className='bruv'>
        <span className='visually-hidden'>Loading...</span>
      </Spinner>
    );
  }
}

export default ActivityList;
