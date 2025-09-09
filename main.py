from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from .storage import load_ids, save_ids, ensure_id

app = FastAPI(title="Educational View Simulation API", version="1.0.0")

class IDItem(BaseModel):
    id: str

class BulkIDs(BaseModel):
    ids: List[str]

class ViewEvent(BaseModel):
    id: str
    increment: int = 1

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/ids")
def get_ids():
    return load_ids()

@app.post("/ids/add")
def add_ids(payload: BulkIDs):
    records = load_ids()
    existing = {r["id"] for r in records}
    added = 0
    for _id in payload.ids:
        if _id not in existing:
            records.append({"id": _id, "views": 0})
            existing.add(_id)
            added += 1
    save_ids(records)
    return {"added": added, "total": len(records)}

@app.post("/view")
def add_view(evt: ViewEvent):
    if evt.increment < 1:
        raise HTTPException(status_code=400, detail="increment must be >= 1")
    records = load_ids()
    # find or create
    found = None
    for r in records:
        if r["id"] == evt.id:
            found = r
            break
    if found is None:
        found = {"id": evt.id, "views": 0}
        records.append(found)
    found["views"] += evt.increment
    save_ids(records)
    return {"id": found["id"], "views": found["views"]}

@app.post("/view/random")
def add_view_random():
    records = load_ids()
    if not records:
        raise HTTPException(status_code=400, detail="No IDs available. Add IDs first.")
    # choose a random id
    import random
    rec = random.choice(records)
    rec["views"] += 1
    save_ids(records)
    return {"id": rec["id"], "views": rec["views"]}

@app.get("/stats")
def stats(limit: Optional[int] = 50):
    records = sorted(load_ids(), key=lambda r: r["views"], reverse=True)
    return records[:limit]