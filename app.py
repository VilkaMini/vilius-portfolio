from flask import Flask, render_template

app = Flask(__name__, static_url_path = "", static_folder = 'static/')

@app.route("/", methods=["GET"])
def portfolio():
    return render_template('index.html')

@app.route("/firegadget/", methods=["GET"])
def firegadget():
    return render_template('firegadget.html')

@app.route("/wildlandsinteractiveexperience/", methods=["GET"])
def wildlandsexperience():
    return render_template('wildlandsexperience.html')

@app.route("/terranova/", methods=["GET"])
def terranova():
    return render_template('terranova.html')

@app.route("/wordweaver/", methods=["GET"])
def wordweaver():
    return render_template('wordweaver.html')

@app.route("/aboutme/", methods=["GET"])
def aboutme():
    return render_template('aboutme.html')

@app.route("/cv/", methods=["GET"])
def cv():
    return render_template('cv.html')


if __name__ == "__main__":
    app.run(debug=True)