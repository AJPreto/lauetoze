from flask import Flask, render_template


app = Flask(__name__)

@app.route("/", endpoint='home')
def home():
    return render_template("index.html")  # Render the index.html template

@app.route("/rsvp", endpoint='rsvp')
def rsvp():
    return render_template("rsvp.html")  # Render the index.html template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)