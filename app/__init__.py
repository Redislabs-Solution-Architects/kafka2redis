import os

from flask import Flask, request, jsonify, render_template

from app.controllers import login_controller, cart_controller, home_controller
from app.utility import redis_connect
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/")
def home():
    return home_controller.show_home(request)


@app.route("/login")
def show_login():
    return login_controller.show_login(request)


@app.route("/logout")
def logout():
    return login_controller.logout_user(request)


@app.route("/loginuser", methods=["POST"])
def login_user():
    return login_controller.login_user(request)


@app.route("/viewcart", methods=["GET", "POST"])
def view_cart():
    return cart_controller.view_cart(request, None)


@app.route("/updatecart", methods=["POST"])
def update_cart():
    return cart_controller.update_cart(request)

