import logging
from typing import List, Dict

async def calculate_moving_averages(data: List[Dict]):
    try:
        logging.info(f"Received data: {data}")

        for record in data:
            if 'short_term' not in record or 'long_term' not in record or 'signal' not in record:
                raise ValueError("Missing required fields in record")
            logging.info(f"Processing record: {record}")

        performance = {
            "average_short_term": sum(
                record['short_term'] for record in data
            ) / len(data),
            "average_long_term": sum(
                record['long_term'] for record in data
            ) / len(data),
            "signals": [
                record['signal'] for record in data
            ]
        }
        logging.info(f"Calculated performance: {performance}")
        return performance
    except Exception as e:
        logging.error(f"Error in calculate_moving_averages: {e}")
        raise