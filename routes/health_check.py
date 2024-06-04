from typing import List
from fastapi import APIRouter

transactify_health_routes = APIRouter(prefix='/transactify/status', tags=["Health"])

@transactify_health_routes.get("")
def health_check():
    return 'healthy'