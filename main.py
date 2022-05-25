
from flask import Flask

from wsgiref import simple_server

from flask import Flask, session, request, Response, jsonify



import atexit
import uuid
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return "App is successfully deployed"

port = int(os.getenv("PORT", 5001))

if __name__ == "__main__":
    host = '0.0.0.0'
    httpd = simple_server.make_server(host=host, port=port, app=app)
    httpd.serve_forever()