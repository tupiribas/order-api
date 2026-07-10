from fastapi import FastAPI
from .api.routers import router

app = FastAPI(title="Order API")


@app.get('/')
def health_check():
    '''
    Base utilizada para o código: https://fastapi.tiangolo.com/pt/#installation
    '''
    return {"title": app.title, "status": "online"}


# Base de conhecimento: https://fastapi.tiangolo.com/reference/apirouter/?h=
# include_router#fastapi.APIRouter.include_router
app.include_router(router)
