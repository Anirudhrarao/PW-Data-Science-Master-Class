from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello world!</h1>"
@app.route("/second/")
def hello2():
    return "<h1>Another page</h1>"
@app.route("/third/")
def hello3():
    return "<h1>One more page for flask</h1>"

@app.route('/input/')
def request_input():
    data = request.args.get('x')
    return "this is my input url {}".format(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0")