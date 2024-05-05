import json
from flask import Flask, Response, jsonify, render_template, request, redirect, url_for
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# @app.route("/message", methods=["POST", "OPTIONS"])
# def message(): 
# return message in json format for example:
# { "message": "testtest" }


if __name__ == "__main__":
    app.run(debug=True)
