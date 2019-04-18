from flask import Flask, request, jsonify
import os

app = Flask(__name__)
port = int(os.environ["PORT"])

@app.route('/', methods=['GET'])
def index():
  return jsonify(
    status=200,
    parameters=request.args
  )

app.run(port=port, host="0.0.0.0")
