import os, json
from datetime import datetime

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

def main():
    os.makedirs(DATA_DIR, exist_ok=True)
    ts = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    path = os.path.join(DATA_DIR, f"events_{ts}.jsonl")
    with open(path, "w", encoding="utf-8") as f:
        for i in range(10):
            event = {"ts": datetime.utcnow().isoformat(), "order_id": i+1, "amount": round(10 + i * 2.5, 2)}
            f.write(json.dumps(event) + "\n")
    print(f"Wrote {path}")

if __name__ == "__main__":
    main()