[![CI](https://github.com/sakshamkamra33/devops-project/actions/workflows/ci.yml/badge.svg)](https://github.com/sakshamkamra33/devops-project/actions)
![CI](https://github.com/sakshamkamra33/devops-project/actions/workflows/ci.yml/badge.svg)

# 🚀 DevOps CI/CD Flask Project

![CI/CD](https://github.com/sakshamkamra33/devops-project/actions/workflows/ci.yml/badge.svg)

## 🌍 Live Demo
👉 https://devops-project-1hhi.onrender.com

---

## 📌 Overview

This project demonstrates a complete **DevOps pipeline** using:

- Flask Web Application
- GitHub Actions (CI/CD)
- Docker Containerization
- Automated Testing (Pytest)
- Cloud Deployment (Render)

---

## ⚙️ Tech Stack

- 🐍 Python (Flask)
- ⚙️ GitHub Actions
- 🐳 Docker
- 🧪 Pytest
- ☁️ Render (Deployment)

---

## 🔁 CI/CD Pipeline

1. Code pushed to GitHub
2. GitHub Actions triggered
3. Tests executed using Pytest
4. Docker image built
5. Image pushed to Docker Hub
6. Application deployed on Render

---

## 📂 Project Structure

```
devops-project/
│── app.py
│── requirements.txt
│── Dockerfile
│── templates/
│ └── index.html
│── tests/
│ └── test_app.py
│── .github/workflows/
│ └── ci.yml
```

---

## 🧪 API Endpoints

| Endpoint | Description |
|--------|-------------|
| `/` | UI Page |
| `/status` | App Status |
| `/about` | Project Info |

---

## ▶️ Run Locally

```bash
git clone https://github.com/sakshamkamra33/devops-project.git
cd devops-project
pip install -r requirements.txt
python app.py
```
🐳 Docker Run
```
docker build -t devops-project .
docker run -p 5000:5000 devops-project
```
---
📸 Output
- CI/CD Pipeline: ✅ Passing
- Deployment: ✅ Live
- Status: Running
---
💡 Key Highlights

- End-to-end DevOps pipeline
- Automated testing & deployment
- Real-world project setup
- Production-ready structure
---

👨‍💻 Author

- Saksham Kamra
