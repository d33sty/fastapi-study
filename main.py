from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/users")
async def retrieve_user_profile(
    username: Annotated[
        str, Query(min_length=2, max_length=50, description="Имя пользователя")
    ],
) -> dict:
    return profiles_dict.get(
        username, {"message": f"Пользователь {username} не найден."}
    )


@app.get("/category/{category_id}/products")
async def category(
    category_id: Annotated[int, Path(gt=0, description="Category ID")],
    page: int,
) -> dict:
    return {"category_id": category_id, "page": page}


@app.get("/users/{name}")
async def get_user(
    name: Annotated[
        str, Path(min_length=4, max_length=20, description="Enter your name")
    ],
) -> dict:
    return {"user_name": f"{name}"}


@app.get("/user")
async def search(people: Annotated[list[str], Query()]) -> dict:
    return {"user": people}


@app.get("/product")
async def detail_view(item_id: int) -> dict:
    return {"product": f"Stock number {item_id}"}


@app.get("/users/admin")
async def admin() -> dict:
    return {"message": f"Hello admin"}
