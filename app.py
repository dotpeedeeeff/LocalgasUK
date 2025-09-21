import gasify
import postcode as pc
from flask import Flask, render_template, request

app = Flask(__name__)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)


@app.route("/")
def home():
 
    return render_template("home.html", len=0)


@app.route("/submit", methods=['POST'])
def local_generation():

    postcode = request.form['postcode']
    outgoing = pc.extract_outer(postcode)
    gas_amount = gasify.local_gas(outgoing)

    return gas_amount
