from flask import render_template, make_response, redirect

from app.utility import session


def show_login(request):
    action_url = "/loginuser"
    return render_template("login.html", action_url=action_url, error=request.args.get("error"))


def login_user(request):
    email = request.form.get("email")
    print(f"Login user: {email}")

    # Create a session
    session_id = session.create_session(email)

    resp = make_response(redirect("/viewcart"))
    resp.set_cookie(
        key="storesessionid",
        value=session_id,
        httponly=True
    )
    return resp


def logout_user(request):
    session_id = request.cookies.get("storesessionid")
    session.delete_session(session_id)
    resp = make_response(render_template("index.html"))
    resp.delete_cookie("storesessionid")
    return resp
