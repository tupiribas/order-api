# Base de conhecimento: https://pydantic.dev/docs/validation/latest/get-
# started/
from pydantic import BaseModel


class OrderCreate(BaseModel):
    customer_name: str
    item_description: str
    price: float


class CondominioCreate(BaseModel):
    nome: str
    endereco: str


class ProdutoCreate(BaseModel):
    nome: str
    preco_base: float


class PessoaCreate(BaseModel):
    nome: str
