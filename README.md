# Pixar Films API

A FastAPI-based REST API to manage Pixar films and their associated people (directors, actors, etc.).

## 📌 Project Structure
```
Pixar-API/
│── main.py                 # Main entry point
│── db.py                   # Database connection
│── api/                    # API directory
│   │── films.py            # Films route
│   │── movies.py           # Movies route
│── pixar-tables/           # Directory containing data files
│   │── academy.sql         # Academy awards
│   │── box-office.sql      # Box office data
│   │── genres.sql          # Genre Data
│   │── pixar-films.sql     # Pixar films
│   │── pixar-people.sql    # People who were involved in the film
│   │── public-response.sql # Movie scores
│── requirements.txt        # Dependencies
│── .env                    # Environment variables
│── README.md               # Project documentation
```

## 🚀 Getting Started

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/jabercrombia/Pixar-API.git
cd Pixar-API
```

### 2️⃣ **Create a Virtual Environment (MacOS/Linux)**
```bash
python -m venv venv
source venv/bin/activate
```

#### **On Windows, use:**
```bash
venv\Scripts\activate
```

### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Set Up Environment Variables**
Create a `.env` file and add your **PostgreSQL database credentials**:
```env
PG_HOST=your-db-host
PG_PORT=5432
PG_USER=your-db-user
PG_PASSWORD=your-db-password
PG_DATABASE=your-db-name
```

### 5️⃣ **Set Up Database Tables and Data**
Navigate to the `pixar-tables` directory and use the provided SQL queries to set up the database tables:
```bash
psql -h $PG_HOST -U $PG_USER -d $PG_DATABASE -f pixar-tables/box_office.sql
```
For text-based data, manually insert records using SQL commands inside `films.txt` and `people.txt`.

### 6️⃣ **Run the API**
```bash
uvicorn main:app --reload
```

## 🌝 API Endpoints
| Method | Endpoint               | Description |
|--------|------------------------|-------------|
| GET    | `/api/films/`          | Get all films |
| GET    | `/api/films/{film_name}`   | Get all people from a specific film |

#### **Available Films for API Search**
Example api
```bash
https://pixar-api.vercel.app/api/films/Coco
```
Use `/api/films/` with one of the following movie names:
- Toy Story
- A Bug's Life
- Toy Story 2
- Monsters, Inc.
- Finding Nemo
- The Incredibles
- Cars
- Ratatouille
- WALL-E
- Up
- Toy Story 3
- Cars 2
- Brave
- Monsters University
- Inside Out
- The Good Dinosaur
- Finding Dory
- Cars 3
- Coco
- Incredibles 2
- Toy Story 4
- Onward
- Soul
- Luca
- Turning Red
- Lightyear
- Elemental
- Inside Out 2



## 🛠 Tech Stack
- **FastAPI** - Web framework
- **PostgreSQL** - Database
- **Uvicorn** - ASGI server
- **Pandas** - Data processing

## 📝 Additional Notes
- Ensure that the PostgreSQL database is running and accessible.
- The `pixar-tables` directory contains structured data that should be uploaded before using the API.
- Use `psql` or a database management tool like **pgAdmin** to verify data insertion.

