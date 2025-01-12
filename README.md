# Chat App with WebSocket Support

## Overview
This is a real-time chat application built using FastAPI and WebSocket. It supports user registration, authentication, and real-time messaging between users. The backend uses PostgreSQL for data storage and SQLAlchemy for ORM.

---

## Features
- User registration and authentication using JWT tokens.
- Real-time messaging via WebSocket.
- Persistent storage of chat messages and user information in PostgreSQL.
- Scalability with async processing using FastAPI.

---

## Requirements
- Python 3.10+
- PostgreSQL
- Redis (optional for caching)
- WebSocket-compatible client (e.g., Postman or browser-based client)

---

## Installation

### 1. Clone the Repository
```bash
git clone <repository_url>
cd ChatApp
```

### 2. Set Up Environment
Create a virtual environment and activate it:  
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up PostgreSQL
Ensure PostgreSQL is running and create a database:  
CREATE DATABASE chat_app;  

Update the `DATABASE_URL` in `.env` file:  
```bash
DATABASE_URL=postgresql+asyncpg://<username>:<password>@localhost/chat_app
SECRET_KEY=your_secret_key
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5. Initialize the Database
Run the following to set up the database schema:  
```bash
python -m backend.database
```

---

## Running the Application

### 1. Start the Development Server
```bash
uvicorn backend.main:app --reload
``` 

### 2. Access the API
Visit the interactive API documentation:  
- Swagger UI: http://localhost:8000/docs  
- ReDoc: http://localhost:8000/redoc  

---

## Testing WebSocket
Use a WebSocket client (e.g., Postman or browser-based tool) to test real-time messaging:  
1. Connect to the WebSocket endpoint:
 ```bash
   ws://localhost:8000/ws
```
2. Send and receive real-time messages.  

---

## Project Structure
ChatApp/  
│  
├── backend/  
│   ├── auth.py                # JWT and authentication logic  
│   ├── config.py              # Configuration data  
│   ├── database.py            # Database setup and connection  
│   ├── models.py              # SQLAlchemy models  
│   ├── routes/                # FastAPI routes  
│   │   ├── users.py           # User-related routes  
│   │   ├── chats.py           # Chat-related routes  
│   │   ├── messages.py        # Message-related routes  
│   │   └── websocket.py       # WebSocket routes  
│   ├── schemas.py             # Pydantic schemas  
│  
├── frontend/  
│   ├── index.htmp                
│   ├── ws.js           
│  
├── .env                       # Environment variables  
├── requirements.txt           # Python dependencies  
└── README.md                  # Project documentation  

---

## License
This project is licensed under the MIT License.
