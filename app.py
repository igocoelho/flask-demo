from flask import Flask, render_template, request
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--debug", help="Debug mode")
parser.add_argument("--host", help="Host on running")
parser.add_argument("--port", help="Port number")

args = parser.parse_args()

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        return "LOGON"

@app.route("/logoff")
def logoff():
    return render_template('login.html')

if __name__ == "__main__":
    debug_mode = args.debug or False
    host_address = args.host or '0.0.0.0'
    port_number = args.port or 5000
    app.run(debug=debug_mode, host=host_address, port=port_number)