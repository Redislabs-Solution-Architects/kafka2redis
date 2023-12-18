import os
import requests
from flask import render_template

from app.utility import redis_conn, session


def show_home(request):
    email = session.get_session(request)

    return render_template("index.html", name=email)
