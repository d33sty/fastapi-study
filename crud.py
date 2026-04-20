from fastapi import FastAPI, Body, status, HTTPException

app = FastAPI()
comments_db = {0: "First comment in FastAPI"}


# Напишите здесь ваше решение.
@app.get("/comments", status_code=status.HTTP_200_OK)
async def get_comments() -> dict:
    pass


@app.get("/comments/{comment_id}", status_code=status.HTTP_200_OK)
async def get_comment(comment_id: int) -> dict:
    pass


@app.post("/comments", status_code=status.HTTP_201_CREATED)
async def get_comment(comment: str = Body(...)) -> dict:
    pass


@app.put("/comments/{comment_id}", status_code=status.HTTP_200_OK)
async def get_comment(comment_id: int, comment: str = Body(...)) -> dict:
    pass


@app.delete("/comments/{comment_id}", status_code=status.HTTP_200_OK)
async def get_comment(comment_id: int) -> dict:
    pass
