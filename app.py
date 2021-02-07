from flask import Flask, render_template
from user_data import get_name
from notes import get_notes

app = Flask(__name__)


@app.route('/')
def index():
    name = get_name()
    return render_template('index.html',
                           name=name)


@app.route('/notes')
def list_notes():
    notes = get_notes()
    return render_template('notes.html',
                           notes=notes)

@app.route('/add_note')
def add_note():
    return render_template('add_note.html')


if __name__ == '__main__':
    app.run()
