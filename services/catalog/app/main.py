from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="AegisOps Catalog API",
    description="An original microservice for the AegisOps DevSecOps platform",
    version="1.0.0",
)

PRODUCTS = [
    {"id": 1, "name": "Secure Cloud Storage", "category": "cloud"},
    {"id": 2, "name": "Identity Protection", "category": "security"},
    {"id": 3, "name": "Monitoring Service", "category": "observability"},
]


@app.get("/health", tags=["operations"])
def health():
    return {"status": "healthy", "service": "catalog-api"}


@app.get("/api/v1/products", tags=["catalog"])
def list_products():
    return {"items": PRODUCTS, "count": len(PRODUCTS)}


@app.get("/api/v1/products/{product_id}", tags=["catalog"])
def get_product(product_id: int):
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product

    raise HTTPException(status_code=404, detail="Product not found")
