
# Instala FastAPI: pip install "fastapi[all]"

from fastapi import FastAPI
from routers import products, users, basic_auth_users, jwt_auth_users
from fastapi.staticfiles import StaticFiles


app = FastAPI()


# Routers

app.include_router(products.router)
app.include_router(users.router)

app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)


app.mount("/static", StaticFiles(directory="static"), name="static")



@app.get("/")
async def  root():
    return "¡Hola FastApi!"

# Url local: http://127.0.0.1:8000/url

@app.get("/url")
async def  url():
    return { "url":"https//mouredev.com/python" }

# Inicia el server: uvicorn main:app --reload
# Detener el server: CTRL + C

# Documentacion con Swagger: http://127.0.0.1:8000/docs
# Documentacion con Redocly: http://127.0.0.1:8000/redoc

# CRUD create, read, update and delete.
