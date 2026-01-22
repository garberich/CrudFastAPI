# CrudFastAPI

Small reference project demonstrating how to build a **scalable backend API** using:

- **FastAPI**
- **Domain-Driven Design (DDD)**
- **Test-Driven Development (TDD)**
- **Clean Architecture principles**

The project is designed for **educational purposes** and as a **starting point for real-world applications** involving multiple domains (e.g. customers, users, orders).

## 🎯 Project goals

- Show how to structure a FastAPI project using **DDD principles**
- Keep the **domain layer independent** from frameworks
- Apply **SOLID principles** and **dependency inversion**
- Build a **fully testable application**
- Ensure tests are **100% repeatable and isolated**

## 🧱 Architecture overview

The project follows a layered architecture inspired by **DDD** and **Hexagonal Architecture (Ports & Adapters)**:

```
API (FastAPI)
└── Application (Use Cases)
└── Domain (Entities & Interfaces)
└── Infrastructure (DB, ORM, external services)
```

### Layers

- **Domain**
  - Entities
  - Business rules
  - Repository interfaces
  - No dependency on FastAPI or SQLAlchemy

- **Application**
  - Use cases (commands & queries)
  - Orchestrates domain logic

- **Infrastructure**
  - SQLAlchemy models
  - Repository implementations
  - Database configuration

- **API**
  - FastAPI routers
  - Request / response schemas
  - Dependency injection

---

The domain layer is completely independent from FastAPI and SQLAlchemy.

## 📁 Project structure

```
src/
├── customers/
│ ├── api/
│ ├── application/
│ ├── domain/
│ └── infrastructure/
├── users/
│ ├── api/
│ ├── application/
│ ├── domain/
│ └── infrastructure/
├── infrastructure/
│ └── db/
├── main.py
tests/
├── api/
├── application/
├── domain/
├── fakes/
```

## ⚙️ Requirements

- Python >= 3.14
- Poetry

## 📦 Installation

Install Poetry if you don't have it:

```
pip install poetry
```

Install project dependencies:

```
poetry install
```

## ▶️ Running the application

Run the API in development mode:

```
poetry run uvicorn src.main:app --reload
```

The API will be available at:

http://127.0.0.1:8000

Swagger UI: http://127.0.0.1:8000/docs

## 🧪 Testing strategy

The project follows TDD and includes:

- Unit tests
    - Domain logic
    - Application use cases
- Integration tests
    - FastAPI endpoints
- In-memory SQLite database for tests
    - Tests do NOT use the application database
    - Database is created and destroyed per test
    - Tests are fully repeatable

Run all tests:

```
poetry run pytest
```

Tests are isolated and can be executed multiple times without affecting the application database.

## 🚧 Project status
This project is under active development and is intended for learning and experimentation with:

- DDD
- Clean Architecture
- FastAPI best practices
- Automated testing