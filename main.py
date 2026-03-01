
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from core.config import Settings
from routers.health import router as health_router
from routers.todos import router as todos_router
from pathlib import Path

settings = Settings()

app = FastAPI(title=settings.APP_NAME)

app.include_router(health_router)
app.include_router(todos_router, prefix="/api/v1")

# serve static frontend (use file-relative path so it works regardless of CWD)
BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


@app.get("/")
def read_root():
    return FileResponse(str(STATIC_DIR / "index.html"))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=settings.DEBUG)
