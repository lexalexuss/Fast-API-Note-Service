from fastapi import FastAPI
from app.notes import router as notes_router

app = FastAPI()

# Подключаем маршруты для работы с заметками
app.include_router(notes_router)
