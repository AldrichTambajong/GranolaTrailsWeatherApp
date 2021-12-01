import { React, useState, useEffect } from "react";
import { Card, Button, Container, Row, Col, Spinner, ListGroup, ListGroupItem } from "react-bootstrap";

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
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  if (listOfActivities.length !== 0) {
    return (
      <Container>
        <Row>
          {listOfActivities.map((item, index) => (
            <Col>
              <Card key={index} style={{ width: "18rem" }}>
                <Card.Img style={{ width: "100%", height: "200px" }} variant='top' src={item["img"]} />
                <Card.Body>
                  <Card.Title>{item["name"]}</Card.Title>
                  <Card.Text>
                    <p>
                      <b>Temp High:</b> {item["weather"]["high"]}° F
                    </p>
                    <p>
                      <b>Temp Low:</b> {item["weather"]["low"]}° F
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
                      window.open(item["url"], "_blank");
                      return null;
                    }}>
                    Go To Site
                  </Button>
                </Card.Body>
                <ListGroup className="list-group-flush">
                  <ListGroupItem>Bouldering Status: {item["activities"]["bouldering"] ? 'Good to go bouldering!' : 'Do not go bouldering today.'}</ListGroupItem>
                  <ListGroupItem>Camping Status: {item["activities"]["camping"] ? 'Good to go camping!' : 'Do not go camping today.'}</ListGroupItem>
                  <ListGroupItem>Fishing Status: {item["activities"]["fishing"] ? 'Good to go fishing!' : 'Do not go fishing today.'}</ListGroupItem>
                  <ListGroupItem>Hiking Status: {item["activities"]["hiking"] ? 'Good to go hiking!' : 'Do not go hiking today.'}</ListGroupItem>
                  <ListGroupItem>Off-Roading Status: {item["activities"]["offroading"] ? 'Good to go off-roading!' : 'Do not go offroading today.'}</ListGroupItem>
                </ListGroup>
              </Card>
            </Col>
          ))}
        </Row>
      </Container >
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
