from pydantic import BaseModel

class AddTransaction(BaseModel):
    txn_amount: int
    agent_id: int
    customer_no: int