import sqlite3 as sq
from flask import Flask, render_template, url_for, g, session, request
from FDataBase import FDataBase

DATABASE = 'to_do.db'

app = Flask(__name__)
app.config.from_object(__name__)


def connect_db():
    con = sq.connect('to_do.db')
    con.row_factory = sq.Row
    return con

def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = DATABASE
    

@app.route('/')
def index():
    db = connect_db()
    return render_template('index.html', notes=enumerate(FDataBase(db).getNotes()))

@app.route('/addNote', methods=['POST', 'GET'])
def addNote():
    db = connect_db()
    dbase = FDataBase(db)
    if request.method == 'POST':
        print(1)
        if len(request.form['text']) > 5 and request.form['text'] not in [x[1] for x in dbase.getNotes()]:
            dbase.addNote(request.form['text'])
        else:
            print('Неврный формат записи')
    return render_template('addNote.html')

@app.route('/deleteNote<int:id>')
def deleteNote(id):
    db = connect_db()
    dbase = FDataBase(db)
    dbase.deleteNote(id)
    
    return index()


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == '__main__':
    app.run(debug=True)