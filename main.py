from fastapi import FastAPI, Query
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Item(BaseModel):
    item_id: int
    name: str
    price: float
    description: str
    category: str

@app.post("/items/")
async def create_item(item: Item):
    return item

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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)