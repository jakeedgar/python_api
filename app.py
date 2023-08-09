#!/usr/bin/python
import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS
import json

# Specify the path to your JSON file
json_file_path = "users.json"

# Open and read the JSON file
with open(json_file_path, "r") as json_file:
    data = json.load(json_file)


app = Flask(__name__)

if __name__ == "__main__":
    # app.debug = True
    # app.run(debug=True)
    app.run()