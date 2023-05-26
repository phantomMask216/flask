from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/webhook',methods=["POST","GET"])
def hook():
    print(request)
    res = request.get_json()
    print(res)
