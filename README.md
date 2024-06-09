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
### 🧩 SQLAlchemy Database Structure
* Users Table
  - name - user's name -> str
  - hashed_password - user's hashed password -> str
  - level_amount - number of levels completed by the user -> int (default=0)
  - time - amount of time spent by the user on completion (in seconds) -> int (default=0)
 
### 📬 Requests
#### Admin
* **Achievements Requests**
  - GET "/api/admin/achievements" 
    + returns list of achievements (body: list[id -> int, name -> str, decription -> str] + list of files)
  - PATCH "/api/admin/achievement" (body: id -> int, name -> str, decription -> str + file)
    + updates achievement data
  - DELETE "/api/admin/achievemnt" (body: id -> int)
    + deletes achievemnt
* **Statistics Requests**
  - GET "/api/admin/statistics"
    + returns lists of topics, users and achievements for data analysis (topics -> list, users -> list, achievements -> list)
* **Topics Requests**
  - GET "/api/admin/topics"
    + returns topics list (body: list[id -> int, name -> str, decription -> str] + list of files)
  - POST "/api/admin/topic" (body: name -> str, decription -> str + file + excel_file)
    + adds new topic
  - PATCH "/api/admin/topic" (body: id -> int, name -> str, decription -> str + file)
    + updates topic
  - DELETE "/api/admin/topic" (body: id -> int)
    + delete topic
