import json, sys

from datetime import datetime
from flask import render_template, redirect
from redis.commands.search.query import Query, NumericFilter

from app.utility import redis_conn, session


def view_search(request, error_msg):
    user_id = request.form.get("user_id") or ''
    from_date = request.form.get("from_date") or ''
    to_date = request.form.get("to_date") or ''
    min_amount = request.form.get("min_amount") or ''
    max_amount = request.form.get("max_amount") or ''
    type = request.form.get("type") or ''
    description = request.form.get("description") or ''

    query_string = ""
    if description != '':
        query_string = f'@description:("{description}")'

    if user_id != '':
        query_string += " @user_id:{" + user_id + "}"

    if type != '':
        query_string += " @type:{" + type + "}"

    if query_string != '':
        query = Query(query_string)
    elif min_amount != '' or max_amount != '' or from_date != '' or to_date != '':
        query = Query("*")
    else:
        query = Query("")
 
    if min_amount != '' and max_amount != '':
        query = query.add_filter(NumericFilter("amount", min_amount, max_amount))
    elif min_amount != '':
        query = query.add_filter(NumericFilter("amount", min_amount, sys.maxsize))
    elif max_amount != '':
        query = query.add_filter(NumericFilter("amount", 0, max_amount))

    if from_date != '':
        from_epoch = datetime.strptime(from_date, '%m/%d/%y').timestamp()
    if to_date != '':
        to_epoch = datetime.strptime(to_date, '%m/%d/%y').timestamp()

    if from_date != '' and to_date != '':
        query = query.add_filter(NumericFilter("date", from_epoch, to_epoch))
    elif from_date != '':
        query = query.add_filter(NumericFilter("date", from_epoch, sys.maxsize))
    elif to_date != '':
        query = query.add_filter(NumericFilter("date", 0, to_epoch))

    result = redis_conn.ft('transaction_idx').search(query)
    count = result.total

    json_docs = []
    for i, doc in enumerate(result.docs): # makes no sense why I have to specify i here
        json_docs.append(json.loads(doc["json"]))
    

    return render_template("search.html", action_url="/search", count=count, result=json_docs, error_msg=error_msg)


