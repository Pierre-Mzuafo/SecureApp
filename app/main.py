from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from datetime import datetime, timezone
from typing import Optional

app = FastAPI(
    title="SecureApp API",
    description="API de démonstration pour un pipeline DevSecOps",
    version="1.0.0"
)

# Modèle Pydantic
class Item(BaseModel):
    id: Optional[int] = None
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    created_at: Optional[datetime] = None

# Base de données en mémoire
items_db = {}
next_id = 1

# Healthcheck
@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

# GET /items
@app.get("/items")
def get_items():
    return list(items_db.values())

# GET /items/{item_id}
@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return items_db[item_id]

# POST /items
@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    global next_id
    item.id = next_id
    item.created_at = datetime.now(timezone.utc)
    items_db[next_id] = item
    next_id += 1
    return item

# DELETE /items/{item_id}
@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    del items_db[item_id]
    return None
