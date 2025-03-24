from fastapi import FastAPI, UploadFile, File, HTTPException
import pandas as pd
import io
import logging
from db import get_db_connection
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from routes import movie
from routes import films

app = FastAPI(
    title="Pixar Movie API",
    description="This is the documentation for my API endpoints.",
    version="1.0.0"
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(movie.router, prefix="/api", tags=["movie"])
app.include_router(films.router, prefix="/api", tags=["films"])

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Landing Page Route
@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("static/index.html", "r") as file:
        return file.read()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)