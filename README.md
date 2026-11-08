# Task Management App

A task management application backend that allows users to manage their tasks. The system uses **Python, FastAPI and PostgreSQL**.

## Features

- User registration and login
- JWT-based authentication
- Protected API endpoints
- Create, view, update, and delete tasks
- User-specific task management

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- Alembic (database migrations)
- Pydantic
- JWT Authentication
- PostgreSQL

## Project Structure

```text
Task-Management/
│
├── backend/
│   ├── src/
│   │   ├── tasks/
│   │   ├── users/
│   │   └── utils/
│   ├── alembic/
│   │   └── versions/
│   ├── alembic.ini
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── Components/
│   │   ├── Pages/
│   │   └── App.jsx
│   └── package.json
│
├── .gitignore
└── README.md
```

This project is developed for learning and educational purposes.
