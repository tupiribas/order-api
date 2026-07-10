from fastapi import APIRouter, status
from models.schemas import OrderCreate

router = APIRouter()


@router.post('/orders/', status_code=status.HTTP_201_CREATED)
def create_order(order: OrderCreate):
    '''
    Base de conhecimento: https://fastapi.tiangolo.com/reference/apirouter/#f
    astapi.APIRouter.post
    https://fastapi.tiangolo.com/tutorial/response-status-code/#shortcut-to-remember-the-names
    '''
    return {"message": "order created",
            "order": dict(order)}
