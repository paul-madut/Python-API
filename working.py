from fastapi import FastAPI

app = FastAPI()

stats = {
    1: {
        "name": "Paul",
        "weight": "155",
        "bench": "245lbs"
    },
    2: {
        "name": "Bob",
        "weight": "175",
        "bench": "125lbs"
    },
    3: {
        "name": "Pau",
        "weight": "140",
        "bench": "445lbs"
    }
}


@app.get("/")
def home():
    return {"data": "Test"}


@app.get("/get-item/{itemId}")
def getItem(itemId: int):
    return stats[itemId]
