from flask import Flask
from flask import request
from flask import Response
from resources import resourcePing, resourceResolution
from message_protocol.resolution_input import parseResolutionInput
import json

import darknet.darknet
#import darknet.darknet_video
#from yolo_server import *


app = Flask(__name__)

network, class_names, class_colors = darknet.darknet.load_network(
            './darknet/cfg/yolov4.cfg',#args.config_file,
            './darknet/cfg/coco_m.data', #args.data_file,
            './darknet/yolov4.weights', #args.weights,
            batch_size=1
        )

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
