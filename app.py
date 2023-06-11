from flask import Flask, render_template, redirect

app = Flask(__name__, static_url_path = "", static_folder = 'static/')

@app.route("/", methods=["GET"])
def portfolio():
    return render_template('chatgpt.html')

@app.route("/wildlandsinteractiveexperience/", methods=["GET"])
def wildlandsexperience():
    return render_template('wildlandsexperience.html')

@app.route("/terranova/", methods=["GET"])
def terranova():
    return render_template('terranova.html')

@app.route("/wordweaver/", methods=["GET"])
def wordweaver():
    return render_template('wordweaver.html')


if __name__ == "__main__":
    app.run(debug=True)