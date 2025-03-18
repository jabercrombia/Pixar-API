from fastapi import APIRouter, HTTPException
from db import get_db_connection

router = APIRouter()

@router.get("/films/{film_name}")
def get_film(film_name: str):
    conn = get_db_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Database connection failed")

    cursor = conn.cursor()
    cursor.execute("""
          SELECT 
            bo.film, 
            bo.budget, 
            pr.rotten_tomatoes_score, 
            pr.imdb_score, 
            pr.metacritic_score,
            COALESCE(json_agg(
                json_build_object('role_type', pp.role_type, 'name', pp.name) 
                ORDER BY pp.name ASC
            ) FILTER (WHERE pp.name IS NOT NULL), '[]') AS people,
            COALESCE(
                json_agg(DISTINCT jsonb_build_object(
                    'award_type', ac.award_type, 
                    'statuses', (
                        SELECT json_agg(ac2.status ORDER BY ac2.status ASC) 
                        FROM academy ac2 
                        WHERE ac2.award_type = ac.award_type AND ac2.film = bo.film
                    )
                )) FILTER (WHERE ac.award_type IS NOT NULL), '[]'
            ) AS awards
        FROM public_response pr
        JOIN box_office bo ON bo.film = pr.film
        LEFT JOIN pixar_people pp ON pp.film = bo.film
        LEFT JOIN academy ac ON ac.film = bo.film
        WHERE bo.film = %s
        GROUP BY bo.film, bo.budget, pr.rotten_tomatoes_score, pr.imdb_score, pr.metacritic_score;
    """, (film_name,))
    
    row = cursor.fetchone()
    cursor.close()
    conn.close()

    if not row:
        raise HTTPException(status_code=404, detail="Film not found")

    return {
        "film": row[0],
        "budget": row[1],
        "rotten_tomatoes_score": row[2],
        "imdb_score": row[3],
        "metacritic_score": row[4],
        "people": row[5],
        "awards": row[6]
    }
