from flask import Flask
from flask import request
from flask import Response
from resources import resourcePing, resourceResolution
from message_protocol.resolution_input import parseResolutionInput
import json

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    output = resourcePing.main()
    json = output.toJSON()
    return Response(json, mimetype='appliction/json')

@app.route('/resolution', methods=['POST'])
def resolution():
    input = parseResolutionInput(request.json)
    output = resourceResolution.main(input)
    output_json = json.dumps(output)
    return Response(output_json, mimetype='appliccation/json')
