import sqlite3 as sq
from flask import Flask, render_template, url_for, g, session, request
from FDataBase import FDataBase
from forms import addNoteForm

DATABASE = 'to_do.db'
SECRET_KEY = '423hjk534ghjk52190&()'

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
    form = addNoteForm()
    if form.validate_on_submit():
        dbase.addNote(form.textarea.data)
        return index()
    else:
        print('Неврный формат записи')
    return render_template('addNote.html', form=form)

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