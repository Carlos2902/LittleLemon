# Restaurant API

## 1. Setup Environment
Create a `.env` file in the root directory:

```env
DB_NAME=your_db_name_here
DB_USER=root
DB_PASSWORD=your_password_here
DB_HOST=127.0.0.1
DB_PORT=3306
```
# 2. Initialization

Run these commands in your terminal:

```python manage.py migrate```

```python manage.py createsuperuser```

## 3. API Endpoints
Test these routes in **Insomnia**:

| Feature | Method | URL |
| :--- | :--- | :--- |
| **Admin Panel** | GET | `http://127.0.0.1:8000/admin/` |
| **Auth Token** | POST | `http://127.0.0.1:8000/restaurant/api-token-auth/` |
| **Bookings** | GET/POST | `http://127.0.0.1:8000/restaurant/booking/` |
| **Menu** | GET | `http://127.0.0.1:8000/restaurant/menu/` |
| **Menu Item** | GET | `http://127.0.0.1:8000/restaurant/menu/1` |
| **User Mgmt** | GET/POST | `http://127.0.0.1:8000/auth/users/` |

> **Header Auth:** `Authorization: Token <your_token>`
