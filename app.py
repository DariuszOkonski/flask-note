from flask import Flask, render_template, redirect, request, url_for
from user_data import get_name
from notes import get_notes, add_note_to_list

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
def display_add_note():
    return render_template('add_note.html')


@app.route('/add_note', methods=['POST'])
def add_note():
    note_dict = dict(request.form)

    add_note_to_list(note_dict['note'])

    return redirect(url_for('list_notes'))


@app.route('/edit_note/<note_id>', methods=['GET'])
def display_edit_note(note_id):
    note_text = ""
    for note in get_notes():
        if int(note['id']) == int(note_id):
            note_text = note['text']

    return render_template('edit_note.html',
                           note_text=note_text)


@app.route('/edit_note/', methods=['POST'])
def edit_note():
    note_dict = dict(request.form)
    add_note_to_list(note_dict['note'])
    return redirect(url_for('list_notes'))


if __name__ == '__main__':
    app.run()
