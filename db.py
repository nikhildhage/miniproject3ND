import sqlite3

DATABASE = 'users.db'


def init_db():
    with sqlite3.connect(DATABASE) as db:
        with open('sqlschema.sql', mode='r') as f:
            db.executescript(f.read())


def get_db(query, args=(), one=False):
    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor().execute(query, args)
        rv = cur.fetchall()
        cur.close()
        return (rv[0] if rv else None) if one else rv


def post_db(query, args=()):
    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor().execute(query, args)
        con.commit()
        cur.close()

