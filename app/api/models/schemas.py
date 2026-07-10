# Base de conhecimento: https://pydantic.dev/docs/validation/latest/get-
# started/
from pydantic import BaseModel


class OrderCreate(BaseModel):
    customer_name: str
    item_description: str
    price: float
