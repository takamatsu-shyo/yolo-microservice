from flask import Flask
from flask import request
from flask import Response
from resources import resourcePing

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    output = resourcePing.main()
    json = output.toJSON()
    return Response(json, mimetype='appliction/json')
