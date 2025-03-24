# Query Quest

A battle royale-themed data science challenge platform where participants solve timed coding questions to earn flags and progress through levels.

![Query Quest Banner](https://github.com/yassermessahli/Query-quest/blob/main/static/images/Question.PNG)

## Overview

Query Quest is a web-based platform that combines data science education with competitive gaming elements. Participants face timed challenges, solve data science problems, and collect unique flags to track their progress.

### Key Features
- Timed coding challenges
- Progress tracking with unique flags
- Secure authentication system
- Multiple difficulty levels (Beginner, Medium, Advanced)
- Battle royale themed interface

## Tech Stac
- Django REST Framework
- MySQL Database
- OpenAI Integration for answer validation
- Token Authentication

## Architecture

```
project/
├── server/              # Django backend
│   ├── src/
│   ├── config/
│   └── ...
└── data/               # Challenge questions
    ├── questions/
    └── advanced/
```

## Getting Started

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
```

### Environment Variables
Create a `.env` file in the main directory similar to .env.example

## Features

### Security Features

- Single session authentication
- Unique team tokens
- Secure flag generation algorithm
- Rate limiting on submissions
- SSL/TLS encryption

### API Documentation

#### Key Endpoints
- `/api/login/` - Team authentication
- `/api/question/<id>/` - Get question details
- `/api/question/<id>/check/` - Submit & validate answers
- `/api/status/` - Get team progress

### Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Open a Pull Request
