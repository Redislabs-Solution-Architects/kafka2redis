import os, json

from flask import Flask, request

from app.controllers import login_controller, cart_controller, home_controller, search_controller
from app.utility.data_handler import DataHandler
from app.utility import redis_conn
from dotenv import load_dotenv

load_dotenv()

INDEX_NAME = "transaction_idx"
app = Flask(__name__)

maker = DataHandler()
maker.create_index(INDEX_NAME, redis_conn)


def to_pretty_json(value):
    return json.dumps(value, sort_keys=True, indent=4, separators=(',', ': '))


app.jinja_env.filters['tojson_pretty'] = to_pretty_json


@app.route("/home")
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


@app.route("/", methods=["GET"])
@app.route("/search", methods=["GET", "POST"])
def search():
    return search_controller.view_search(request, None)


@app.route("/create_index", methods=["GET"])
def create_index():
    maker.create_index(INDEX_NAME, redis_conn)
    return home_controller.show_home(request)


@app.route("/ingest", methods=["GET"])
def ingest():
    maker.ingest_data(redis_conn)
    return home_controller.show_home(request)

@app.route("/sample_data", methods=["GET"])
def sample_data():
    f = open('app/resources/test_data.json')
    data = json.load(f)
    return data
