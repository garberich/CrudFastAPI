# CrudFastAPI

Small example project using **FastAPI**, **DDD (Domain-Driven Design)** and **TDD (Test-Driven Development)**.

The goal of this project is to serve as a clean architecture reference for building scalable APIs with Python.

## Architecture

This project follows a layered architecture inspired by DDD:

- **Domain**: Entities, value objects and repository interfaces
- **Application / Use cases**: Business logic
- **Infrastructure**: Database, repositories, external services
- **API**: FastAPI routers and schemas

The domain layer is completely independent from FastAPI and SQLAlchemy.

## Requirements

- Python >= 3.14
- Poetry

## Installation

Install Poetry if you don't have it:

```
pip install poetry
```

Install project dependencies:

```
poetry install
```

## Running the application

Run the API in development mode:

```
poetry run uvicorn src.main:app --reload
```

The API will be available at:

http://127.0.0.1:8000

Swagger UI: http://127.0.0.1:8000/docs

## Running tests

Run all tests:

```
poetry run pytest
```

Tests are isolated and can be executed multiple times without affecting the application database.

## Project status
This project is under active development and is intended for educational purposes