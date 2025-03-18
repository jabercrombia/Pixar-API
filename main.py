from fastapi import FastAPI, UploadFile, File, HTTPException
import pandas as pd
import io
import logging
from db import get_db_connection
from routes import movie
from routes import films

app = FastAPI()

app.include_router(movie.router, prefix="/api", tags=["movie"])
app.include_router(films.router, prefix="/api", tags=["films"])

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/")
def read_root():
    return {"message": "Welcome to Pixar Films API!"}