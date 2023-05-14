from flask import Flask, render_template

app = Flask(__name__, static_url_path = "", static_folder = 'static/')

@app.route("/", methods=["GET"])
def portfolio():
    return render_template('index.html')

"""
@app.route("/gamedev", methods=["GET"])
def gamedev():
    return render_template('gamedev.html')

@app.route("/datascientist", methods=["GET"])
def datascientists():
    return render_template('index.html')
"""

if __name__ == "__main__":
    app.run(debug=True)