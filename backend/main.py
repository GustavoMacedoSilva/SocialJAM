import uvicorn
from app.api.routes_album import router as album_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes_user import router as user_router
from app.api.routes_artist import router as artist_router
from app import models
from app.database import engine
from app.core.mongo import connect_mongo, disconnet_mongo


app = FastAPI(
    title="SocialJAM",
    description="API para socializar baseado no seu gosto musical",
)

# connect to mongo db right after starting the server and disconnect before closing the server
async def lifespan(app: FastAPI):
    await connect_mongo()
    yield
    await disconnet_mongo()

origins = [
    "http://localhost:5173"
]

# adds the cors middleware responsible to menage the conection betwen front-end and back-end
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.base.metadata.create_all(engine)
app.include_router(user_router)
app.include_router(artist_router)
app.include_router(album_router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
