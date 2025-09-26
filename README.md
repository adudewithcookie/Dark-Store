# Dark Store Management API  

This project implements a secure REST API using Django and Django REST Framework (DRF) for managing dark stores (locations) and their internal shelving systems.  

---

## 🚀 Features  

- User authentication with **Token-based login**  
- Manage **Locations (Dark Stores)**  
  - Create, read, update, delete (CRUD) operations  
  - List all shelves belonging to a specific location  
- Manage **Shelves**  
  - CRUD operations with weight capacity tracking  
- SQLite database (lightweight and portable)  
- Postman collection provided for testing  

---

## 🛠️ Tech Stack  

- **Django** (Backend Framework)  
- **Django REST Framework** (API layer)  
- **SQLite** (Database)   
- **python-dotenv** (for `.env` configuration)  

---

## ⚙️ Installation & Setup  

### 1. Clone the repository  
```bash
git clone https://github.com/adudewithcookie/Dark-Store
cd dark-store
```

### 2. Set up a virtual environment  
```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

### 3. Install dependencies  
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables  
Create a `.env` file in the root directory:  
```
SECRET_KEY=your_secret_key
DEBUG=True
```

### 5. Run migrations  
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a superuser (for authentication)  
```bash
python manage.py createsuperuser
```

### 7. Run the server  
```bash
python manage.py runserver
```

Your API will be available at:  
👉 `http://127.0.0.1:8000/api/`  

---

## 🔑 Authentication  

Before accessing protected endpoints, obtain a token:  

### Login  
```http
POST /api/auth/login/
Content-Type: application/json

{
  "username": "your_username",
  "password": "your_password"
}
```

Response:  
```json
{
  "token": "your_auth_token"
}
```

Use this token in the `Authorization` header:  
```
Authorization: Token your_auth_token
```

---

## 📖 API Endpoints  

### Locations  

- **List all locations**  
  `GET /api/locations/`

- **Create new location** (Authenticated)  
  `POST /api/locations/`  
  ```json
  {
    "name": "Central Warehouse",
    "address": "123 Main St",
    "is_active": true
  }
  ```

- **Get location by ID**  
  `GET /api/locations/<id>/`

- **Update location** (Authenticated)  
  `PUT /api/locations/<id>/`

- **Delete location** (Authenticated)  
  `DELETE /api/locations/<id>/`

- **List shelves for a location**  
  `GET /api/locations/<id>/shelves/`

---

### Shelves  

- **List all shelves**  
  `GET /api/shelves/`

- **Create new shelf** (Authenticated)  
  `POST /api/shelves/`  
  ```json
  {
    "location": 1,
    "identifier": "Shelf-A1",
    "weight_capacity": 500
  }
  ```

- **Get shelf by ID**  
  `GET /api/shelves/<id>/`

- **Update shelf** (Authenticated)  
  `PUT /api/shelves/<id>/`

- **Delete shelf** (Authenticated)  
  `DELETE /api/shelves/<id>/`

---

## 🧪 Testing  

A **Postman collection** is included in the repo for testing all endpoints.  
Import it into Postman and adjust the authentication token where required.  

---

## 📌 Notes  

- Default database is SQLite (for simplicity).  
- Easily extendable to PostgreSQL/MySQL by updating `DATABASES` in `settings.py`.  
- Built for demonstration purposes under a time-constrained interview task.  

---

## 👨‍💻 Author  

Developed by **Soroush**  
