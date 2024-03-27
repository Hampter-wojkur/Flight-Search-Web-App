from flask import Flask, Response, jsonify, render_template, request, redirect, url_for
from flask_cors import CORS
from convert_data import convert_data_format
from flight_data import FlightData

app = Flask(__name__)
CORS(app)


# @app.route("/", methods=["POST"])
# def render_home_page():
#     if request.method == "POST":
#         form_data = request.form.to_dict()
#         print(f"Form data: {form_data}")



# Only route currently in use
@app.route("/submit_form", methods=["POST", "OPTIONS"])
def submit_form():
    if request.method == "POST":
        form_data = request.json 
        # print(f"Form data: {form_data}")
        converted_data = convert_data_format(form_data)
        # print(converted_data)
        flights = FlightData(converted_data)
        print(flights)
        

        return Response('{"Message":"PUT Request accept"}', status=200, mimetype='application/json')
    
    return Response('{"option":"ok"}', status=200,  mimetype='application/json')



# @app.route("/deal", methods=["POST"])
# def single_deal():

#     json_data = request.json
#     print(type(json_data))
#     flights = FlightData(json_data).find_best_fly()
#     print(flights)

#     return render_template("index.html")


# @app.route("/newsletter")
# def subscription():
#     return render_template("newsletter.html")


# @app.route("/newsletter/deals", methods=["POST"])
# def subscription_deals():

#     json_data = request.json
#     # print(type(json_data))
#     flights = FlightData(json_data).find_best_fly()
#     print(flights)

#     return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
