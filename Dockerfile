FROM python:3.9

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
COPY / .env 

RUN prisma generate
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]