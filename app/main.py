from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "David Hello World from Flask"
#@app.route("/david")
#def david():
#    return "Hello, david"

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
