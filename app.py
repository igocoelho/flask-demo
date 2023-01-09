from flask import Flask, render_template, request, make_response, redirect, flash
import helper
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--debug", help="Debug mode")
parser.add_argument("--host", help="Host on running")
parser.add_argument("--port", help="Port number")

args = parser.parse_args()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

@app.route("/")
@helper.user_required
def home():
    return render_template('home.html')

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        email = request.form.get("email")
        password = request.form.get("password")
        if email == "igo@coelho.com" and password == "1234":
            response = make_response(redirect("/", 302))
            response.set_cookie("token", "fsjdlfsdlkfsldfkjslkdfjsldkjfsldf")
            return response
        else:
            flash("Invalid Email or Password. Please try again!")
            return make_response(redirect("/login", 302))

@app.route("/logoff")
def logoff():
    response = make_response(redirect("/login", 302))
    response.delete_cookie("token")
    return response

if __name__ == "__main__":
    debug_mode = args.debug or False
    host_address = args.host or '0.0.0.0'
    port_number = args.port or 5000
    app.run(debug=debug_mode, host=host_address, port=port_number)