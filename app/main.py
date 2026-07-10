from fastapi import FastAPI

app = FastAPI(title="Order API")


@app.get('/')
def health_check():
    '''
    Base utilizada para o código: https://fastapi.tiangolo.com/pt/#installation
    '''
    return {"title": app.title, "status": "online"}
