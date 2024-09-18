import json
import os

NOTES_FILE = "notes.json"


# Чтение заметок из файла
def read_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as f:
            return json.load(f)
    return {}


# Запись заметок в файл
def write_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=4)
