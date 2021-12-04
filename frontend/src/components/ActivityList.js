import { React, useState, useEffect } from "react";
import {
  Card,
  Button,
  Container,
  Row,
  Col,
  Spinner,
  ListGroup,
  ListGroupItem,
} from "react-bootstrap";

import "bootstrap-icons/font/bootstrap-icons.css";

function capitalize(str) {
  return str.charAt(0).toUpperCase() + str.slice(1);
}

const EMOJI = {
  bouldering: "🧗",
  camping: "🏕️",
  fishing: "🎣",
  hiking: "🥾",
  offroading: "🚗",
};

function ActivityList(props) {
  let activities = {
    user_state: props.userState,
  };

  const [listOfActivities, setListOfActivities] = useState([]);

  useEffect(() => {
    // console.log(JSON.stringify(activities));
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
                <Card.Img
                  style={{ width: "100%", height: "200px" }}
                  variant='top'
                  src={item["img"]}
                />
                <Card.Body>
                  <Card.Title>{item["name"]}</Card.Title>
                  <Card.Text>
                    <p>
                    <i class="bi bi-thermometer-high"></i>{item["weather"]["high"]}° F &nbsp;&nbsp; <i class="bi bi-thermometer-low"></i>{item["weather"]["low"]}° F  
                    </p> 
                    <p>
                    <i class="bi bi-droplet"></i>{item["weather"]["precipitation"]}% &nbsp;&nbsp;&nbsp;&nbsp;  <i class="bi bi-cloud"></i>{item["weather"]["clouds"]}%
                    </p>            
                    {/* {item["description"]} */}
                  </Card.Text>
                  <Button
                    variant='success'
                    onClick={() => {
                      window.open(item["url"], "_blank");
                      return null;
                    }}>
                    Go To Site
                  </Button>
                </Card.Body>
                <ListGroup className='list-group-flush'>
                  <ListGroupItem>
                    <b>Activity Status</b>
                  </ListGroupItem>
                  {/* <ListGroupItem>
                    Bouldering{" "}
                    {item["activities"]["bouldering"]
                      ? <i class="bi bi-flag-fill" style = {{color:'green'}}></i>
                      : <i class="bi bi-flag-fill" style = {{color: 'red'}}></i>
                      }
                  </ListGroupItem>
                  <ListGroupItem>
                    Camping:{" "}
                    {item["activities"]["camping"]
                      ? <i class="bi bi-flag-fill" style = {{color:'green'}}></i>
                      : <i class="bi bi-flag-fill" style = {{color:'red'}}></i>}
                  </ListGroupItem>
                  <ListGroupItem>
                    Fishing:{" "}
                    {item["activities"]["fishing"]
                      ? <i class="bi bi-flag-fill" style = {{color:'green'}}></i>
                      : <i class="bi bi-flag-fill" style = {{color:'red'}}></i>}
                  </ListGroupItem>
                  <ListGroupItem>
                    Hiking:{" "}
                    {item["activities"]["hiking"]
                      ? <i class="bi bi-flag-fill" style = {{color:'green'}}></i>
                      : <i class="bi bi-flag-fill" style = {{color:'red'}}></i>}
                  </ListGroupItem>
                  <ListGroupItem>
                    Off-Roading:{" "}
                    {item["activities"]["offroading"]
                      ? <i class="bi bi-flag-fill" style = {{color:'green'}}></i>
                      : <i class="bi bi-flag-fill" style = {{color:'red'}}></i>}
                  </ListGroupItem> */}
                  {Object.entries(item["activities"]).map(
                    (activity_weather, index) => {
                      return (
                        <ListGroupItem>
                          {capitalize(activity_weather[0])}:{" "}
                          {activity_weather[1]
                            ? "Good to go " + EMOJI[activity_weather[0]] + "!"
                            : "Do not go today."}
                        </ListGroupItem>
                      );
                    }
                  )}
                </ListGroup>
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
