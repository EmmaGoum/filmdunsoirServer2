from flask import Flask, request, jsonify
import os

app = Flask(__name__)
port = int(os.environ["PORT"])

@app.route('/', methods=['GET'])
def index():

  p1 = request.args.get("p1")
  p2 = request.args.get("p2")
  a = p1 + p2

  return jsonify(
    status=200,
    parameters=a
  )

app.run(port=port, host="0.0.0.0")
