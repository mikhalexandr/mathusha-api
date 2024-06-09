# Mathusha API

![License](https://img.shields.io/github/license/dmhd6219/sdamgia-solver)
![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![Version](https://img.shields.io/badge/version-1.0-green)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)

API which is written for the Mathusha service. It interacts with user data and also has the ability to perform admin requests

## 🛠️ Tech Stack
ㅤ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/sqlalchemy-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)
![Keycloak](https://img.shields.io/badge/keycloak-5277C3.svg?style=for-the-badge)
![Yandex GPT](https://img.shields.io/badge/yandex_gpt-FF0000?style=for-the-badge)
![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

## 🎯 Quick Start
* Clone the project to your computer from Github using the command:
```
git clone https://github.com/mikhalexandr/mathusha-api.git
```

* Install all required dependencies from `requirements.txt`:
```
pip install requirements.txt
```

* create `.env` in the project folder and paste these lines there:
```env
SECRET_KEY=your_secret_key

YANDEX_GPT_DIRECTORY_ID=your_yandex_gpt_directory_id
YANDEX_GPT_API_KEY=your_yandex_gpt_api_key

KEYCLOAK_SERVER_URL=your_keycloak_server_url
KEYCLOAK_ADMIN_USERNAME=ypur_keycloak_admin_username
KEYCLOAK_ADMIN_PASSWORD=your_keycloak_admin_password
KEYCLOAK_REALM_NAME=your_keycloak_realm_name
KEYCLOAK_USER_REALM_NAME=your_keycloak_user_realm_name
KEYCLOAK_CLIENT_ID=your_keycloak_client_id
KEYCLOAK_CLIENT_SECRET_KEY=your_keycloak_client_secret_key
```

* Run `app.py`

> [!TIP]
> To create a docker container use [Dockerfile](https://github.com/mikhalexandr/mathusha-api/blob/main/Dockerfile) and [docker-compose.yml](https://github.com/mikhalexandr/mathusha-api/blob/main/docker-compose.yml)

> [!TIP]
> To host the API on [Glitch](https://glitch.com/) use [start.sh](https://github.com/mikhalexandr/mathusha-api/blob/main/start.sh)
 
## 📝 Documentation
#### 🧩 SQLAlchemy Database Structure
* Users Table
  - name - user's name -> str
  - hashed_password - user's hashed password -> str
  - level_amount - number of levels completed by the user -> int (default=0)
  - time - amount of time spent by the user on completion (in seconds) -> int (default=0)
 
#### 📬 Requests
* **Register Requests**
  - POST "/api/register" (body: name -> str, password -> str)
    + adds a new user (requires name uniqueness check)
* **Login Requests**
  - GET "/api/login" (body: name -> str, password -> str)
    + authorizes the user by checking the username and password
    + returns number of levels completed and time spent completing (body: level_amount -> int, time -> int)
* **Update Resources**
  - PATCH "/api/update/name" (body: name -> str, new_name -> str, password -> str)
    + updates user's name (requires password confirmation and name uniqueness check)
  - PATCH "/api/update/password" (body: name -> str, password -> str, new_password -> str)
    + updates user's password (requires password confirmation and password difference from the old one)
  - PATCH "/api/update/record" (body: name -> str, level_amount -> int, time -> int)
    + updates number of levels completed and time spent completing
* **Delete Requests**
  - DELETE "/api/delete" (body: name -> str, password -> str)
    + deletes user data (requires password confirmation) 
* **Rating Requests**
  - GET "/api/rating" (body: name -> str)
    + gets all users in the sorted list (body of each user in list: name -> str, level_amount -> int, time -> int)
    + gets the user's place in the rating table (body: user_index in list + 1 -> int) 
