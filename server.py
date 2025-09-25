import os
import psycopg2
# from psycopg2.pool import ThreadedConnecitonPool
from psycopg2.extras import DictCursor
from flask import Flask, request, redirect, url_for, render_template


app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


# TODO separate DB file functions...
# Code is sloppy, likely OK for practice

# dbinit type function:
# pool = None
# global pool
# ThreadedConnectionPool(1,100,dsn=DATABASE_URL, sslmode="require")

@app.route('/api/guestbook', methods=["POST","GET"])
def apiGuests():
    if request.method == "GET":
        conn = psycopg2.connect(os.getenv("DATABASE_URL"))
        with conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute("SELECT * FROM Guests")
            resp = cur.fetchall()
            print(resp)
            conn.close()
            return resp

    if request.method == "POST":
        print(request.form["name"])

        conn = psycopg2.connect(os.getenv("DATABASE_URL"))
        with conn.cursor() as cur:
            name = request.form["name"]
            cmnt = request.form["comment"]
            cur.execute(
                "INSERT INTO Guests(fullName, comment) values(%s, %s)", (name, cmnt)
            )
            conn.commit()
            conn.close()
            return redirect(url_for('hello', name=name))
        conn.close()

    
