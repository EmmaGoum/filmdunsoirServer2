from flask import Flask, request, jsonify
import os

#https://filmdunsoir2.herokuapp.com/?p1=0&p2=5&p3=12

app = Flask(__name__)
port = int(os.environ["PORT"])

@app.route('/', methods=['GET'])
def index():

  a=""
  p1 = request.args.get("p1")
  p2 = request.args.get("p2")
  a = int(p1) + int(p2)

  if a = "":
    a = 2
  else:
    a = a

  return jsonify(
    status=200,
    parameters=a
  )

app.run(port=port, host="0.0.0.0")
