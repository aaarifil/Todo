# FastAPI ToDo (assignment)

Quick demo implementing levels 0–3 (in-memory CRUD, validation, filtering, pagination).

Run:

```powershell
pip install -r requirements.txt
uvicorn main:app --reload
```

Database (optional):

Set `DATABASE_URL` in `.env` (defaults to a local `sqlite:///./dev.db`). To create database tables run:

```powershell
python create_db.py
```

For Postgres use e.g.:

```powershell
set DATABASE_URL=postgresql://postgres:password@localhost:5432/todo
python create_db.py
```

Endpoints:
- GET /health -> { "status": "ok" }
- GET / -> greeting message
- POST /api/v1/todos
- GET /api/v1/todos (supports `is_done`, `q`, `sort`, `limit`, `offset`)
- GET /api/v1/todos/{id}
- PUT /api/v1/todos/{id}
- PATCH /api/v1/todos/{id}
- DELETE /api/v1/todos/{id}
