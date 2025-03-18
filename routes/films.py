from fastapi import APIRouter, HTTPException
from db import get_db_connection

router = APIRouter()

# return all films
@router.get("/films/")
def get_films():
    conn = get_db_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Database connection failed")

    cursor = conn.cursor()
    cursor.execute("SELECT bo.film, bo.budget, pr.rotten_tomatoes_score, pr.imdb_score, pr.metacritic_score, COALESCE(json_agg(json_build_object('role_type', pp.role_type, 'name', pp.name)) FILTER (WHERE pp.name IS NOT NULL), '[]') AS people FROM box_office bo JOIN public_response pr ON bo.film = pr.film LEFT JOIN pixar_people pp ON bo.film = pp.film GROUP BY bo.film, bo.budget, pr.rotten_tomatoes_score, pr.imdb_score, pr.metacritic_score;")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    # Convert to list of dicts
    films = [{"film": row[0], "budget": row[1], "rotten_tomatoes": row[2], "imdb": row[3], "metacritic": row[4], "people": row[5]} for row in rows]

    return {"films": films}
