#!/usr/bin/env python
from flask import Flask,render_template,Response,request,jsonify
# emulated camera
from camera import MyCamera
from time import time
# Raspberry Pi camera module (requires picamera package)
# from camera_pi import Camera

# import smbus

# This is the address we setup in the Arduino Program
address = 0x04

app = Flask(__name__)


@app.route('/')
def index():
	"""Video streaming home page."""
	return render_template('index.html')


def gen(camera):
	"""Video streaming generator function."""
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
	"""Video streaming route. Put this in the src attribute of an img tag."""
	return Response(gen(MyCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')


bus = None


@app.route('/control_robot')
def control_robot():
	global bus
	cmd = request.args.get('cmd', 0, type=int)
	print "got command", cmd
	# if cmd == 0:
	#     bus = smbus.SMBus(1)
	#     print "Connecting to Arduino"
	# elif bus != None:
	#     bus.write_byte(address, cmd)
	#     print "Writing cmd ", cmd
	return jsonify(result=cmd)

if __name__ == '__main__':
	app.run(host='127.0.0.1', debug=True, threaded=True)
