"""
Created on Mar 26, 2012

@author: steve
"""

from database import password_hash
import uuid
from bottle import response, request
from http.cookies import SimpleCookie

# this variable MUST be used as the name for the cookie used by this application
COOKIE_NAME = 'sessionid'


def check_login(db, usernick, password):
    cur = db.cursor()
    list = cur.execute("select * from users")

    for entry in list.fetchall():
        if usernick == entry[0]:
            if password_hash(password) == entry[1]:
                return True
            else:
                return False
    """returns True if password matches stored"""


def generate_session(db, usernick):
    """create a new session and add a cookie to the response object (bottle.response)
    user must be a valid user in the database, if not, return None
    There should only be one session per user at any time, if there
    is already a session active, use the existing sessionid in the cookie
    """
    cur = db.cursor()
    key = str(uuid.uuid4())

    listSessions = "select sessionid from sessions where usernick=?"
    insertSessions = "insert into sessions values(?,?)"
    cur.execute("select nick from users where nick=?", (usernick,))

    if cur.fetchone:  # can also do if not row
        cur.execute(listSessions, (usernick,))
        idExist = cur.fetchone()
        if idExist:
            response.set_cookie(COOKIE_NAME, idExist[0])
        else:
            cur.execute(insertSessions, (key, usernick))
            db.commit()
            response.set_cookie(COOKIE_NAME, key)

    else:
        return None


def delete_session(db, usernick):
    """remove all session table entries for this user"""
    cur = db.cursor()
    list = cur.execute("select * from sessions")

    for entry in list.fetchall():
        if entry [1] == usernick:
            query = "delete from sessions where usernick=?"
            values = (usernick,)
            cur.execute(query, values)
            db.commit()


def session_user(db):
    """try to
    retrieve the user from the sessions table
    return usernick or None if no valid session is present"""
    cur = db.cursor()
    key = request.get_cookie(COOKIE_NAME)

    list = cur.execute("select * from sessions where sessionid=?", (key,))
    row = cur.fetchone()

    if row:
        return row[1]
    else:
        return None
