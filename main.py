from fastapi import FastAPI, Depends, HTTPException, status

app = FastAPI()


# Напишите здесь ваше решение.
async def check_auth(token: str):
    if token == "secret":
        return True

    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")


@app.get("/profile", status_code=status.HTTP_200_OK)
async def get_profile(auth: bool = Depends(check_auth)) -> str:
    if auth:
        return "User is authorized"
