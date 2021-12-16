from flask import Flask, render_template

app = Flask(__name__, static_url_path = "", static_folder = 'static/')

@app.route("/", methods=["GET"])
def portfolio():
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)