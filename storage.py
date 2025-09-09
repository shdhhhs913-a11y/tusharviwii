from pathlib import Path
import json
from typing import List, Dict

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "ids.json"

def load_ids() -> List[Dict]:
    if not DATA_PATH.exists():
        return []
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_ids(records: List[Dict]) -> None:
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)

def ensure_id(rec_id: str) -> Dict:
    records = load_ids()
    for r in records:
        if r["id"] == rec_id:
            return r
    # create new if not exists
    new_r = {"id": rec_id, "views": 0}
    records.append(new_r)
    save_ids(records)
    return new_r