from flask import Flask, request, jsonify
import os

#https://filmdunsoir2.herokuapp.com/?p1="0, 2"&p2="5, 8, 10, 13"&p3="2"&p4="3, 8, 14"&p5="3"&p6="2"&p7="4"&p8="2"&p9="1"&p10="2"&p11="4"&p12="4"&p13="1"&p14="3"&p15="2"&p16="3"&p17="1"&p18="0"&p19="1"&p20="5"&p21="0"&p22="1"
#https://filmdunsoir2.herokuapp.com/?p1=0, 2&p2=5, 8, 10, 13&p3=2&p4=3, 8, 14&p5=3&p6=2&p7=4&p8=2&p9=1&p10=2&p11=4&p12=4&p13=1&p14=3&p15=2&p16=3&p17=1&p18=0&p19=1&p20=5&p21=0&p22=1
#rep = ["0, 2", "5, 8, 10, 13", "2", "3, 8, 14", "3", "2", "4", "2", "1", "2", "4", "4", "1", "3", "2", "3", "1", "0", "1", "5", "0", "1"]


app = Flask(__name__)
port = int(os.environ["PORT"])

@app.route('/', methods=['GET'])
def index():

  p1 = request.args.get("p1")
  p2 = request.args.get("p2")
  p3 = request.args.get("p3")
  p4 = request.args.get("p4")
  p5 = request.args.get("p5")
  p6 = request.args.get("p6")
  p7 = request.args.get("p7")
  p8 = request.args.get("p8")
  p9 = request.args.get("p9")
  p10 = request.args.get("p10")
  p11 = request.args.get("p11")
  p12 = request.args.get("p12")
  p13 = request.args.get("p13")
  p14 = request.args.get("p14")
  p15 = request.args.get("p15")
  p16 = request.args.get("p16")
  p17 = request.args.get("p17")
  p18 = request.args.get("p18")
  p19 = request.args.get("p19")
  p20 = request.args.get("p20")
  p21 = request.args.get("p21")
  p22 = request.args.get("p22")

  rep = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22]

  return jsonify(
    status=200,
    #parameters=request.args
    parameters=rep
  )

app.run(port=port, host="0.0.0.0")
