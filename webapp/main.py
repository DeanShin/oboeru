from flask import *
from flask_socketio import SocketIO


# Create flask app, SocketIO object, and global pi 'thing' object.
app = Flask(__name__)
socketio = SocketIO(app)


# Define app routes.
# Index route renders the main HTML page.
@app.route("/")
def index():
    switch = 1
    # Render index.html template.
    return render_template('index.html', switch=switch)


if __name__ == "__main__":
    # Run the flask development web server with SocketIO.
    socketio.run(app, host='0.0.0.0', debug=True)
