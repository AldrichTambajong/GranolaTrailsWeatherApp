"""
    creates the app
"""

import os
import json
import flask

app = flask.Flask(__name__)

def main():
    """
    starts the app
    """

    app.run(
        debug=True,
        host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", str(8081))),
    )


if __name__ == "__main__":
    main()
