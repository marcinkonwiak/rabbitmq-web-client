from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.config import STATIC_DIR, STATIC_PATH
from src.router import router

app = FastAPI()
app.include_router(router)
app.mount(STATIC_PATH, StaticFiles(directory=STATIC_DIR), name="static")

# replace that with Alembic
# from database.core import Base, engine
# Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)
