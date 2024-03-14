from flask import Flask, render_template, request, redirect, url_for
from flight_data import FlightData

app = Flask(__name__)


@app.route("/")
def render_home_page():
    return render_template("start.html")


@app.route("/deal", methods=["POST"])
def single_deal():

    json_data = request.json
    print(type(json_data))
    flights = FlightData(json_data).find_best_fly()
    print(flights)

    return render_template("index.html")


@app.route("/newsletter")
def subscription():
    return render_template("newsletter.html")


@app.route("/subscription/deals", methods=["POST"])
def subscription_deals():

    json_data = request.json
    # print(type(json_data))
    flights = FlightData(json_data).find_best_fly()
    print(flights)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
