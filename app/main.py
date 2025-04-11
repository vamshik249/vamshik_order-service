from fastapi import FastAPI
from app.routers import orders as order
from app.database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(order.router, prefix="/orders", tags=["Orders"])

@app.get("/")
def read_root():
    return {"message": "Order Service is running!"}