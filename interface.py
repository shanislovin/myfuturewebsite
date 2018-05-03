"""
Database Model interface for the COMP249 Web Application assignment

@author: steve cassidy
"""

import datetime

def position_list(db, limit=10):
    """Return a list of positions ordered by date
    db is a database connection
    return at most limit positions (default 10)

    Returns a list of tuples  (id, timestamp, owner, title, location, company, description)
    """
    cur = db.cursor()
    list = cur.execute("select id, timestamp, owner, title, location, company, description from positions order by timestamp desc")

    return list.fetchall()[:limit];

def position_get(db, id):
    """Return the details of the position with the given id
    or None if there is no position with this id

    Returns a tuple (id, timestamp, owner, title, location, company, description)
    """
    cur = db.cursor();
    list = cur.execute("select * from positions")

    for row in list.fetchall():
        if row[0] == id:
            return row
    else:
        return None

def position_add(db, usernick, title, location, company, description):
    """Add a new post to the database.
    The date of the post will be the current time and date.
    Only add the record if usernick matches an existing user

    Return True if the record was added, False if not."""
    cur = db.cursor();
    users2 = cur.execute("select * from users")
    timestamp = datetime.datetime.now()

    for nick in users2:
        if nick[0] == usernick:
            query = "insert into positions (timestamp, owner, title, location, company, description) values (?,?,?,?,?,?)"
            values = (timestamp, usernick, title, location, company, description)
            cur.execute(query, values)
            db.commit()
            return True
    else:
        return False




