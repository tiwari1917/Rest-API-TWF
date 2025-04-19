from fastapi import FastAPI
from pydantic import RootModel

app = FastAPI()


COSTS = {
    "C1": 50,
    "C2": 36, 
    "C3": 82  
}
MAPPING = {
    "A": ["C1"],
    "B": ["C1"],
    "C": ["C2"],
    "D": ["C3"],
    "E": ["C3"],
    "F": ["C3"],
    "G": ["C2"],
    "H": ["C2"],
    "I": ["C2"]
}



class Request_Item(RootModel[dict[str, int]]):
    pass


@app.post("/min-cost")
def min_cost(item: Request_Item):
    quantities = item.root

    
    warehouses = set()

    for product, quantity in quantities.items():
        if quantity > 0:
            ans = MAPPING.get(product, [])
            warehouses.update(ans)

    total_price = sum(COSTS[wh] for wh in warehouses)
    return {"price": total_price}
