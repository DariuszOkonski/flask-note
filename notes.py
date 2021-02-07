NOTES_FILE = 'notes.txt'

def get_notes():
    with open(NOTES_FILE, "r") as file:
        return file.readlines()

def add_note_to_list(note):
    with open(NOTES_FILE, "a") as file:
        file.write(note + "\n")