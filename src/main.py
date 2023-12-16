from config import STATIC_DIR, STATIC_PATH
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from router import router

app = FastAPI()
app.include_router(router)
app.mount(STATIC_PATH, StaticFiles(directory=STATIC_DIR), name="static")

# replace that with Alembic
# from database.core import Base, engine
# Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)
