FROM python:3.9

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV DATABASE_URL="postgresql://postgres:Sita9867@host.docker.internal:5432/Trading?public=StockData"

RUN prisma generate
ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]