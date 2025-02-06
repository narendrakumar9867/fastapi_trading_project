from fastapi import FastAPI 
from app.routes import data_routes, strategy_routes
from app.database import connect_db, disconnect_db
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_db()
    yield
    await disconnect_db()
    
app = FastAPI(lifespan=lifespan)
    
app.include_router(data_routes.router)
app.include_router(strategy_routes.router)