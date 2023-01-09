from flask import request, make_response, redirect, flash
from functools import wraps

def user_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        htoken = request.args.get("token")
        qtoken = request.cookies.get("token")

        if not htoken and not qtoken:
            flash("Unauthorized Access. Please do the login!")
            return make_response(redirect("/login", 302))
        else:
            return f(*args, **kwargs)
    
    return decorated