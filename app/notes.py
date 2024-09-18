from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.auth import authenticate
from app.models import Note
from app.storage import read_notes, write_notes
from app.speller import check_spelling

# Создаем маршрутизатор для работы с заметками
router = APIRouter()


# Маршрут для добавления заметки
@router.post("/notes/")
async def add_note(note: Note, username: str = Depends(authenticate)):
    notes = read_notes()
    corrected_content = await check_spelling(note.content)
    if username not in notes:
        notes[username] = []
    notes[username].append({"content": corrected_content})
    write_notes(notes)
    return {"message": "Note added successfully", "content": corrected_content}


# Маршрут для получения списка заметок
@router.get("/notes/", response_model=List[dict])
async def get_notes(username: str = Depends(authenticate)):
    notes = read_notes()
    if username not in notes:
        raise HTTPException(status_code=404, detail="No notes found")
    return notes[username]
