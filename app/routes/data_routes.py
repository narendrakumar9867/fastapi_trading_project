from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.database import db
from datetime import datetime
from decimal import Decimal
from typing import List
from prisma.types import StockDataCreateInput

router = APIRouter()

class StockDataRequest(BaseModel):
    datetime: datetime
    open: Decimal
    high: Decimal
    low: Decimal
    close: Decimal
    volume: int

@router.get("/data", response_model=List[StockDataRequest])
async def get_data():
    return await db.stockdata.find_many()

@router.post("/data")
async def add_data(stock: StockDataRequest):
    try:
        stock_data = StockDataCreateInput(
            datetime=stock.datetime,
            open=stock.open,
            high=stock.high,
            low=stock.low,
            close=stock.close,
            volume=stock.volume
        )
        await db.stockdata.create(data=stock_data)
        return {"message": "Stock data added successfully."}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    