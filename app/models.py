from pydantic import BaseModel


# Модель для заметки
class Note(BaseModel):
    content: str
