from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()


# Напишите здесь вашу модель.
class Note(BaseModel):
    id: int
    text: str


notes = [
    Note(id=1, text="Купить хлеб"),
    Note(id=2, text="Написать отчет"),
    Note(id=3, text="Позвонить маме"),
    Note(id=4, text="Сходить в спортзал"),
    Note(id=5, text="Прочитать книгу"),
]


# Напишите здесь ваше решение.
@app.delete("/notes/{note_id}", status_code=status.HTTP_200_OK, response_model=Note)
async def delete_note(note_id: int) -> Note:
    for i, note in enumerate(notes):
        if note.id == note_id:
            return notes.pop(i)

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
