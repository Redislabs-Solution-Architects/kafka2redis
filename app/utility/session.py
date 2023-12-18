import uuid

from app.utility import redis_conn


def get_session(request):
    session_id = request.cookies.get("storesessionid")
    if not session_id:
        return None

    # Reset the expiration on the session
    redis_conn.expire(f"sessions:{session_id}", 60)
    return redis_conn.get(f"sessions:{session_id}")


def create_session(email):
    session_id = uuid.uuid4().hex
    redis_conn.set(name=f"sessions:{session_id}", value=email, ex=60)
    return session_id


def delete_session(session_id):
    if session_id is not None:
        redis_conn.delete(f"sessions:{session_id}")
