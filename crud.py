from fastapi import FastAPI, Body, status, HTTPException

app = FastAPI()
comments_db = {0: "First comment in FastAPI"}


# Напишите здесь ваше решение.
@app.get("/comments", status_code=status.HTTP_200_OK)
async def get_comments() -> dict:
    return comments_db


@app.get("/comments/{comment_id}", status_code=status.HTTP_200_OK)
async def get_comment(comment_id: int) -> str:
    if comment_id not in comments_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found"
        )
    return comments_db[comment_id]


@app.post("/comments", status_code=status.HTTP_201_CREATED)
async def get_comment(comment: str = Body(...)) -> str:
    id = max(comments_db) + 1 if comments_db else 0
    comments_db[id] = comment
    return "Comment created!"


@app.put("/comments/{comment_id}", status_code=status.HTTP_200_OK)
async def get_comment(comment_id: int, comment: str = Body(...)) -> str:
    if comment_id not in comments_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found"
        )
    comments_db[comment_id] = comment
    return "Comment updated!"


@app.delete("/comments/{comment_id}", status_code=status.HTTP_200_OK)
async def get_comment(comment_id: int) -> str:
    if comment_id not in comments_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found"
        )
    del comments_db[comment_id]
    return "Comment deleted!"
