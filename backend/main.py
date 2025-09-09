from fastapi import FastAPI
from app.api.routes_user import router as user_router
from app.api.routes_artist import router as artist_router
from app import models
from app.database import engine


app = FastAPI(
    title="SocialJAM",
    description="API para socializar baseado no seu gosto musical",
)

models.base.metadata.create_all(engine)
app.include_router(user_router)
app.include_router(artist_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=8000, reload=True)
