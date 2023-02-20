from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Item(BaseModel):
    item_id: int
    name: str
    price: float
    description: str
    category: str

# @app.post("/items/")
# async def create_item(item: Item):
#     return item

# using query 
@app.get("/products")
async def get_products(name: str | None = Query(default=..., max_length=10)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if name:
        results.update({"Product": name})
    return results

@app.get("/mahasiswa")
async def get_mahasiswa(name: list[str] | None = Query(default=...)):
    results = {"mahasiswa": [{"name": "sultan"}, {"name": "Babiono"}]}
    for value in name:
        results["mahasiswa"].append({"name": value})
    return results


# @app.get("/items/{item_id}")
# async def get_item(
#         item_id: int = Path(title="The ID of the item to get"),
#         q: str | None = Query(default=None, alias="item-query")
#     ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(title="The ID of the item to get", ge=0, le=1000),
    q: str | None = None,
    item: Item | None = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item = Body(embed=True)):
#     results = {"item_id": item_id, "item": item}
#     return results

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)