import sys
import os
import unittest
from fastapi.testclient import TestClient
import asyncio

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.main import app
from app.database import connect_db, disconnect_db

client = TestClient(app)

class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(cls.loop)
        cls.loop.run_until_complete(connect_db())

    @classmethod
    def tearDownClass(cls):
        if cls.loop.is_running():
            cls.loop.run_until_complete(disconnect_db())
        if not cls.loop.is_closed():
            cls.loop.close()

    def test_add_data(self):
        response = client.post("/data", json={
            "datetime": "2023-10-01T12:00:00",
            "open": 100.0,
            "high": 110.0,
            "low": 90.0,
            "close": 105.0,
            "volume": 1000
        })
        print("Response Status Code", response.status_code)
        print("Response JSON", response.json())
        if response.status_code != 200:
            print("error adding data:", response.json())

    def test_get_data(self):
        response = client.get("/data")
        print("Response JSON:", response.json())
        self.assertEqual(response.status_code, 200)