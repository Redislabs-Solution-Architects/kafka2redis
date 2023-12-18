from flask import render_template, redirect

from app.utility import redis_conn, session


def view_cart(request, error_msg):
    email = session.get_session(request)
    if not email:
        return redirect("/login")

    items = redis_conn.hgetall(f"cart:{email}")

    for key, value in items.items():
        print(key, '->', value)

    return render_template("cart.html", action_url="/updatecart", name=email,
                           items=items, error_msg=error_msg)


def update_cart(request):
    # Get email from session cookie
    email = session.get_session(request)
    if not email:
        return redirect("/login")

    item = request.form.get("items")
    error_msg = None
    try:
        count = int(request.form.get("count"))
        if count == 0:
            redis_conn.hdel(f"cart:{email}", item)
        else:
            redis_conn.hset(f"cart:{email}", mapping={item: count})
    except Exception:
        count = request.form.get("count")
        error_msg = f"Invalid count: {count}"

    print(f"update_cart name: {email} item: {item}, count: {count}")

    return view_cart(request, error_msg=error_msg)
