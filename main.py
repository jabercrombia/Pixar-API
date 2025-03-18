from fastapi import FastAPI
import pandas as pd
import io
import logging
from db import get_db_connection
from routes import movie
from routes import films
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(movie.router, prefix="/api", tags=["movie"])
app.include_router(films.router, prefix="/api", tags=["films"])

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return RedirectResponse(url="/static/favicon.ico")
# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/")
def read_root():
    return {"message": "Welcome to Pixar Films API!"}