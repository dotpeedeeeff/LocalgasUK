import gasify
from flask import Flask, render_template

app = Flask(__name__)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)


@app.route("/")
def home():

    gas_string = gasify.fuel_percentage()    

    gas = f"{gas_string}"

    return render_template("home.html", len=0,gas=gas)
