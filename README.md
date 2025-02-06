# Simple CRUD API with FastAPI and Robot Framework

This project is a simple CRUD API built using FastAPI, designed to be tested using Robot Framework. The API provides basic operations for managing users.

## 🚀 Setup Instructions

### 1️⃣ Clone the Repository
```bash
mkdir my_crud_api
cd my_crud_api
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
```

Activate the environment:
- **Windows (Command Prompt)**:  
  ```bash
  venv\Scripts\activate
  ```
- **Mac/Linux**:  
  ```bash
  source venv/bin/activate
  ```

### 3️⃣ Install Dependencies
```bash
pip install fastapi uvicorn robotframework-requests
```

### 4️⃣ Save Dependencies (Optional, for sharing)
```bash
pip freeze > requirements.txt
```

To install dependencies later, run:
```bash
pip install -r requirements.txt
```

---

## ▶️ Running the API

### 🔹 Running Locally
Start the FastAPI server:
```bash
uvicorn main:app --reload
```
The API will be available at **http://127.0.0.1:8000**

You can also access interactive API docs at:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Redoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### 🔹 Running with Docker

1. **Build the Docker Image**
```bash
docker build -t my_crud_api .
```

2. **Run the API Container**
```bash
docker run -p 8000:8000 my_crud_api
```

---

## 🧪 Running Robot Framework Tests

### 🔹 Running Locally
1. Navigate to the `tests/` directory:
```bash
cd tests
```
2. Run the API tests:
```bash
robot api_tests.robot
```

### 🔹 Running Tests with Docker

1. **Run Tests Inside a Docker Container** (Make sure the API is running first)
```bash
docker run --network=host -v $(pwd)/tests:/app/tests my_crud_api robot /app/tests/api_tests.robot
```

2. **Run Tests in a Separate Container (API + Tests)**
```bash
# Run API in detached mode
docker run -d --name my_api -p 8000:8000 my_crud_api

# Run tests
docker run --network=host -v $(pwd)/tests:/app/tests my_crud_api robot /app/tests/api_tests.robot

# Stop and remove the API container after tests
docker stop my_api && docker rm my_api
```

---

## 📂 Project Structure
```
my_crud_api/
│-- main.py               # FastAPI Application
│-- Dockerfile            # Docker setup
│-- requirements.txt      # Dependencies
│-- venv/                 # Virtual Environment (optional)
└── tests/
    └── api_tests.robot   # Robot Framework API Tests
```

---

## 🎯 Next Steps
- Extend API functionality
- Improve test cases
- Add database support (SQLite, PostgreSQL, etc.)
