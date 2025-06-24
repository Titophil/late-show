# 🎤 Late Show API

A Flask REST API to manage episodes, guests, and appearances on a fictional late-night talk show. Includes user authentication with JWT and PostgreSQL persistence.

---

## 🛠️ Setup Instructions

### Requirements
- Python 3.8+
- PostgreSQL
- `pipenv` or `virtualenv` (recommended)

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/late-show-api.git
cd late-show-api
2. Create Virtual Environment & Install Dependencies
bash
Copy
Edit
pipenv install
pipenv shell
# OR
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
3. PostgreSQL Setup
Start PostgreSQL (on port 5433 if used):

bash
Copy
Edit
sudo service postgresql start
Create the database:

bash
Copy
Edit
psql -U postgres -p 5433
CREATE DATABASE late_show_db;
\q
Give proper permissions if needed:

bash
Copy
Edit
GRANT ALL PRIVILEGES ON DATABASE late_show_db TO postgres;
🔐 Environment Variables
Create a .env file:

ini
Copy
Edit
FLASK_APP=server.app
FLASK_ENV=development
DATABASE_URI=postgresql://postgres@localhost:5433/late_show_db
JWT_SECRET_KEY=your-secret-key
Ensure Config in server/config.py reads these variables using os.getenv.

🚀 How to Run
1. Run Migrations
bash
Copy
Edit
flask db init       # Only once
flask db migrate -m "Initial"
flask db upgrade
2. Seed the Database
bash
Copy
Edit
python -m server.seed
3. Start the Server
bash
Copy
Edit
flask run
🔐 Auth Flow
Register
POST /register

json
Copy
Edit
{
  "username": "admin",
  "password": "admin123"
}
Login
POST /login

json
Copy
Edit
{
  "username": "admin",
  "password": "admin123"
}
➡ Returns:

json
Copy
Edit
{
  "access_token": "your.jwt.token"
}
Using Token (Example)
In Postman or headers:

makefile
Copy
Edit
Authorization: Bearer <access_token>
📡 Routes
Method	Endpoint	Description
POST	/register	Register a new user
POST	/login	Login and receive JWT token
GET	/episodes	List all episodes
GET	/episodes/<id>	Get a single episode
DELETE	/episodes/<id>	Delete an episode
GET	/guests	List all guests
POST	/appearances/	Create an appearance
POST	/users	Create user (manual/seed)

🧪 Sample Request/Response
GET /episodes
http
Copy
Edit
GET /episodes HTTP/1.1
Authorization: Bearer <token>
Response:

json
Copy
Edit
[
  {
    "id": 1,
    "title": "First Show",
    "air_date": "2025-01-01"
  }
]
🧰 Postman Usage Guide
Open Postman.

Create a new collection Late Show API.

Add POST /register and POST /login.

For authenticated requests, go to Authorization tab:

Type: Bearer Token

Token: Paste the value from /login response.

🔗 late-show
📎 https://github.com/Titophil/late-show.git