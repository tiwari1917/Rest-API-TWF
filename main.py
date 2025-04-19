from fastapi import FastAPI
from pydantic import RootModel

app = FastAPI()

PRODUCT_WAREHOUSE_MAPPING = {
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

WAREHOUSE_COST = {
    "C1": 50,
    "C2": 36, 
    "C3": 82  
}


class ProductRequest(RootModel[dict[str, int]]):
    pass


@app.post("/min-cost")
def min_cost(product_request: ProductRequest):
    product_quantities = product_request.root

    
    used_warehouses = set()

    for product, quantity in product_quantities.items():
        if quantity > 0:
            warehouses = PRODUCT_WAREHOUSE_MAPPING.get(product, [])
            used_warehouses.update(warehouses)

    total_price = sum(WAREHOUSE_COST[wh] for wh in used_warehouses)
    return {"price": total_price}
