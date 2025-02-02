<h1>For code Run command lines</h1>

# PRISMA

---

### Prisma Commands:

```bash
prisma generate
prisma migrate dev --name list
```

---

### Run or Test the API:

```bash
uvicorn app.main:app --reload
```

---

### Run the Dockerfile:

```bash
docker build -t fastapi-app .
docker run -p 8000:8000 --env-file .env fastapi-app
```

---

### Test

- Run all tests:

```bash
pytest
```

- Run tests with coverage report:

```bash
pytest --cov=app
```

- Run a specific test file:

```bash
pytest tests/test_main.py
```
