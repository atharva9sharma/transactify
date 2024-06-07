from fastapi import APIRouter
from models.txn_api_requests import AddTransaction


transactify_routes = APIRouter(prefix='/transactify/v1/txn', tags=["Transaction"])

@transactify_routes.post("/register")
def create_transactions(addtransaction:AddTransaction):
    return addtransaction