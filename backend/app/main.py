from fastapi import FastAPI
from app.api.routes.products import router as products_routes
from app.api.routes.sales import router as sales_routes

app = FastAPI(
    title="pos system api",
    version="0.1.0"
)

app.include_router(products_routes)
app.include_router(sales_routes)
