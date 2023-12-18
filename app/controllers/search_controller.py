import sys

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
    if description is not '':
        query_string = f'@description:("{description}")'

    if user_id is not '':
        query_string += " @user_id:{" + user_id + "}"

    if query_string is not '':
        query = Query(query_string)
    elif min_amount is not '' or max_amount is not '' or from_date is not '' or to_date is not '':
        query = Query("*")
    else:
        query = Query("")
 
    if min_amount is not '' and max_amount is not '':
        query = query.add_filter(NumericFilter("amount", min_amount, max_amount))
    elif min_amount is not '':
        query = query.add_filter(NumericFilter("amount", min_amount, sys.maxsize))
    elif max_amount is not '':
        query = query.add_filter(NumericFilter("amount", 0, max_amount))

    result = redis_conn.ft('transaction_idx').search(query)

    print(result)

    return render_template("search.html", action_url="/search", result=result, error_msg=error_msg)


