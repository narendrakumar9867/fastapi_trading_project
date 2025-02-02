from fastapi import APIRouter
from pydantic import BaseModel
import logging
    
from app.services.trading_service import calculate_moving_averages

router = APIRouter()


class MovingAverageRequest(BaseModel):
    short_term: float
    long_term: float
    signal: str


@router.get("/strategy/performance")
async def moving_averages():
    try:
        data = [
            {"short_term": 86.5, "long_term": 50.2, "signal": "buy"},
            {"short_term": 86.8, "long_term": 91.3, "signal": "sell"}
        ]
        result = await calculate_moving_averages(data)
        return result
    except Exception as e:
        logging.error(f"Error in moving_averages: {e}")
