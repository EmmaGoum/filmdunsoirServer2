from flask import Flask, request, jsonify
import os

#https://filmdunsoir2.herokuapp.com/?p1=0&p2=5&p3=12&p4=1&p5=1&p6=1&p7=1&p8=1&p9=1&p10=1&p11=1&p12=1&p13=1&p14=1&p15=1&p16=1&p17=1&p18=1&p19=1&p20=1&p21=1&p22=1

app = Flask(__name__)
port = int(os.environ["PORT"])

@app.route('/', methods=['GET'])
def index():

  p1 = request.args.get("p1")
  p2 = request.args.get("p2")

  return jsonify(
    status=200,
    parameters=request.args
  )

app.run(port=port, host="0.0.0.0")
