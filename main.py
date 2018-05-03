__author__ = 'Steve Cassidy, Shanis Lovin 44857713'

from bottle import Bottle, template, static_file, request, redirect, response
from interface import position_add, position_get, position_list
from users import session_user, check_login, generate_session, delete_session
from database import sample_data, create_tables
app = Bottle()
created = False


#   HOME PAGE:      Global boolean allows the tables and data to be created only
#                   once. Returns title, session information, and listings.
@app.route('/')
def index(db):
    global created
    if not created:
        create_tables(db)
        sample_data(db)
        created = True

    info = {
        'title': 'myfuture',
        'positions': position_list(db, 10),
        'name': session_user(db)
    }

    return template('index', info)


#   POST LOGIN:     Processes the login form and uses users' check_login
#                   to confirm login details are correct, else returns
#                   failed login template.
@app.route('/login', method="POST")
def log_in(db):
    nick = request.forms.get('nick')
    password = request.forms.get('password')

    if check_login(db, nick, password):
        sessionid = generate_session(db, nick)
        response.status = 303
        return redirect('/',302)
    else:
        return template('failedlogin.tpl')


#   POST LOGOUT:    Gets the current session user name and deletes it,
#                   therefore logging the user out by deleting session
@app.route('/logout', method="POST")
def log_out(db):
    usernick = session_user(db)
    delete_session(db,usernick)
    return redirect('/', 302)


#   POST POST:      Processes the details of a new listing and adds it
#                   to the list
@app.route('/post', method="POST")
def post(db):
    title = request.forms.get('title')
    company = request.forms.get('company')
    location = request.forms.get('location')
    description = request.forms.get('description')
    position_add(db, session_user(db), title, location, company, description)
    return redirect('/', 302)


#   ABOUT PAGE
@app.route('/views/about.html')
def about(db):

    info = {
        'title': 'About Jobs',
        'name': session_user(db)
    }

    return template('about', info)


#   POSITIONS PAGE:     Lists the details of a position that the user
#                       clicked on to read more information
@app.route('/positions/<DD>')
def positions(db,DD=id):
    info = {
        'positions': position_get(db, int(DD)),
        'name': session_user(db)
    }

    return template('positions', info)


@app.route('/static/<filename:path>')
def static(filename):
    return static_file(filename=filename, root='static')


if __name__ == '__main__':

    from bottle.ext import sqlite
    from database import DATABASE_NAME
    # install the database plugin
    app.install(sqlite.Plugin(dbfile=DATABASE_NAME))
    app.run(debug=True, port=8010)
