from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/webhook',methods=["POST","GET"])
def hook():
    print(request.data)
