from flask import *
from flask_socketio import SocketIO

# Create flask app, SocketIO object, and global pi 'thing' object.
app = Flask(__name__)
socketio = SocketIO(app)

# Define app routes.
# Index route renders the main HTML page.
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/learn/")
def learn():
    return render_template('learn.html')

@app.route("/practice/")
def practice():
    return render_template('practice.html')

@app.route("/settings/")
def settings():
    return render_template('settings.html')

@app.route("/about/")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    # Run the flask development web server with SocketIO.
    socketio.run(app, host='0.0.0.0', debug=True)
