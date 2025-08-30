# 🧩 QueryQuest  
> **Play Data Science! — Gamified challenges for aspiring data scientists.**

QueryQuest is a **battle royale–themed data science challenge platform** that blends learning with competition. Participants solve **timed coding problems**, capture **unique flags**, and advance through levels — making data science both engaging and practical.

<br>

![Query Quest Banner](https://github.com/yassermessahli/Query-quest/blob/main/static/images/Question.PNG)

### 💠 Key Features
- Timed coding challenges  
- Progress tracking with unique flags  
- Secure authentication system  
- Multiple difficulty levels (Beginner → Advanced)  
- Battle royale–themed interface  

### 🛠 Tech Stack
- **Backend:** Django REST Framework  
- **Database:** MySQL  
- **Validation:** OpenAI integration for answer checking  
- **Auth:** Token-based authentication  

### 📦 Architecture
```

project/
├── server/              # Django backend
│   ├── src/
│   ├── config/
│   └── ...
└── data/                # Challenge questions
├── questions/
└── advanced/

````

## ⚡ Getting Started

### Prerequisites
- Python 3.11+  
- Node.js 18+  
- MySQL  

### Setup (development environment)
```sh
cd <directory>
pip install poetry
poetry install
python manage.py migrate
python manage.py runserver
````

### Environment Variables

Create a `.env` file in the project root based on `.env.example`.

## ⚙️ Security Features

* Single-session authentication
* Unique team tokens
* Secure flag generation algorithm
* Rate limiting on submissions
* SSL/TLS encryption

### 💠 API Documentation

### Key Endpoints

* `POST /api/login/` → Team authentication
* `GET /api/question/<id>/` → Retrieve question details
* `POST /api/question/<id>/check/` → Submit & validate answers
* `GET /api/status/` → Check team progress

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes and push
4. Open a Pull Request
