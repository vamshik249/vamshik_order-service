# 🛒 Order Management Backend - FastAPI Microservice

This is a FastAPI-based backend microservice for managing customer orders. It supports CRUD operations and is containerized using Docker. The database used is SQLite (can be switched to PostgreSQL/MySQL easily).

---

## 📁 Project Setup Guide

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/your-username/order-backend.git
cd order-backend
```

---

### 🧪 2. Create and Activate Virtual Environment

#### 🔹 Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### 🔹 macOS / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 📦 3. Install Dependencies

```bash
pip install -r requirements.txt
```


---

### 🚀 4. Run the FastAPI App

```bash

uvicorn app.main:app --reload

```

Then open your browser:  
🔗 [http://localhost:8000/docs](http://localhost:8000/docs) — Swagger UI  

---

## 🐳 Docker Usage

### 1. Build Docker Image

```bash
docker build -t order-backend-app .
```

### 2. Run Docker Container

```bash
docker run -d -p 8000:8000 order-backend-app
```

Access API at [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📂 File Structure

```
order-backend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── database.py
│   └── routers/
│       └── orders.py
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🧪 Run Tests

If you have unit tests set up with `pytest`, run:

```bash
pytest
```

---

## 📬 Sample API Calls

### 🔹 Create Order

```bash
curl -X POST http://localhost:8000/orders/ -H "Content-Type: application/json" -d '{
  "customer_name": "John Doe",
  "item_name": "Laptop",
  "quantity": 2,
  "price": 899.99
}'
```

### 🔹 Get Order by ID

```bash
curl http://localhost:8000/orders/1
```

---

## 🛠️ Tech Stack

- FastAPI  
- SQLAlchemy ORM  
- SQLite  
- Uvicorn  
- Pydantic  
- Docker  
- Pytest

---

## 🌐 Deployment (AWS / EC2)

You can push your Docker image to:
- AWS EC2 (via Docker)
- AWS ECS / Fargate
- Render / Railway / Fly.io

> Contact me or see deployment instructions in `DEPLOY.md` (if added)

---

## 👨‍💻 Author

Made  by [VAMSHIK C SHETTY]  
