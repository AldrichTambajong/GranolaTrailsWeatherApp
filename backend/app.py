import flask
import os

app = flask.Flask(__name__)

app.run(
    debug=True,
    host=os.getenv("IP", "0.0.0.0"),
    port=int(os.getenv("PORT", 8081)),
)
