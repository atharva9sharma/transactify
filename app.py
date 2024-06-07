import uvicorn
from fastapi import FastAPI
from routes.health_check import transactify_health_routes
from routes.txn_routes import transactify_routes

app = FastAPI()
app.include_router(transactify_routes)
app.include_router(transactify_health_routes)

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8002, log_level="info", reload=True)