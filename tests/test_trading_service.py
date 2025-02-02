import pytest
import logging
from app.services.trading_service import calculate_moving_averages

@pytest.mark.asyncio
async def test_calculate_moving_averages_success():
    data = [
        {"short_term": 86.5, "long_term": 50.2, "signal": "buy"},
        {"short_term": 86.8, "long_term": 91.3, "signal": "sell"}
    ]
    result = await calculate_moving_averages(data)
    assert result["average_short_term"] == (86.5 + 86.8) / 2
    assert result["average_long_term"] == (50.2 + 91.3) / 2
    assert result["signals"] == ["buy", "sell"]

@pytest.mark.asyncio
async def test_calculate_moving_averages_missing_fields():
    data = [
        {"short_term": 86.5, "long_term": 50.2},
        {"short_term": 86.8, "long_term": 91.3, "signal": "sell"}
    ]
    with pytest.raises(ValueError, match="Missing required fields in record"):
        await calculate_moving_averages(data)

@pytest.mark.asyncio
async def test_calculate_moving_averages_exception_handling(caplog):
    data = [
        {"short_term": 86.5, "long_term": 50.2, "signal": "buy"},
        {"short_term": 86.8, "long_term": 91.3, "signal": "sell"}
    ]
    with caplog.at_level(logging.ERROR):
        try:
            await calculate_moving_averages(data)
        except Exception as e:
            assert "Error in calculate_moving_averages" in caplog.text
            raise e