from fastapi import FastAPI, Path

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
def getItem(itemId: int = Path(None, description="Id of item that you want", gt=0, lt=len(stats))):
    return stats[itemId]


# Get Method that accepts a query by having "?{varName}={Query}" in the URI where varName is
# is the key that you're searching in and Query is the value that is being searched in the dictionary
@app.get("/get-by-name")
def getItem(name: str):
    for itemId in stats:
        if stats[itemId]["name"] == name:
            return stats[itemId]
    return {"Data": "Not found"}

# Post Method that adds an item to the "stats "
