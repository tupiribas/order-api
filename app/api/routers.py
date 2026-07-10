from fastapi import APIRouter
from models.schemas import OrderCreate

router = APIRouter()


@router.post('/orders')
def create_order(order: OrderCreate):
    '''
    Base de conhecimento: https://fastapi.tiangolo.com/reference/apirouter/#f
    astapi.APIRouter.post
    '''
    return {"message": "order created",
            "order": dict(order)}
