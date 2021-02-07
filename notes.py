NOTES_FILE = 'notes.csv'
SEPARATOR = ";"
ID_INDEX = 0
TEXT_INDEX = 1

def get_notes():
    with open(NOTES_FILE, "r") as file:
        notes = []
        for line in file.readlines():
            note = {
                'id': line.split(SEPARATOR)[ID_INDEX],
                'text': line.split(SEPARATOR)[TEXT_INDEX].replace("\n", "")}
            notes.append(note)
        print(notes)
        return notes


def add_note_to_list(note):
    with open(NOTES_FILE, "a") as file:
        file.write(note + "\n")
