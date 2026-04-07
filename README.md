# 🚀 DevOps CI/CD Monitoring Dashboard

🚀 A production-style DevOps dashboard with CI/CD, monitoring, and deployment pipeline

![CI](https://github.com/sakshamkamra33/devops-project/actions/workflows/ci.yml/badge.svg)

---


## 🌍 Live Demo
👉 https://devops-project-1nhi.onrender.com


---

## 📌 Overview  

This project demonstrates a **production-style DevOps pipeline** with a **real-time monitoring dashboard**.

It simulates how modern applications are built, tested, containerized, and deployed automatically using CI/CD practices.

---

## ⚡ Key Features  

- 🔄 Automated CI/CD Pipeline using GitHub Actions  
- 🐳 Dockerized Application for consistent deployment  
- ☁️ Cloud Deployment on Render  
- 📊 Interactive DevOps Dashboard UI  
- 🔐 Authentication System (JWT-based login)  
- 📈 API Monitoring & Metrics Visualization  
- 📜 Deployment Timeline Tracking  
- 🧪 Automated Testing with Pytest  

---

## 🛠️ Tech Stack  

- 🐍 Python (Flask)  
- ⚙️ GitHub Actions  
- 🐳 Docker  
- 🧪 Pytest  
- ☁️ Render  
- 📊 Chart.js  
- 🔐 JWT Authentication  

---

## 🔁 CI/CD Pipeline Flow  

1. Code pushed to GitHub  
2. GitHub Actions triggered  
3. Automated tests executed (Pytest)  
4. Docker image built  
5. Application deployed to Render  
6. Live dashboard updated  

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
| `/` | Dashboard UI |
| `/status` | App status & version |
| `/about` | Project details |
| `/login` | Authentication (JWT) |

---

## ▶️ Run Locally

```bash
git clone https://github.com/sakshamkamra33/devops-project.git
cd devops-project
pip install -r requirements.txt
python app.py
```

---

🐳 Run with Docker
```
docker build -t devops-dashboard .
docker run -p 5000:5000 devops-dashboard
```
---

📊 Dashboard Highlights
- Real-time service status
- Version tracking
- API metrics visualization
- Deployment timeline
- Logs simulation
  
---
💡 What Makes This Project Special
- End-to-end DevOps lifecycle implementation
- Combines Development + Operations + Monitoring
- Demonstrates real-world CI/CD practices
- Clean UI with meaningful system insights

  ---

## 📸 Preview  

### Dashboard Overview
![Dashboard](assets/dashboard-1.png)

### Metrics & Monitoring
![Metrics](assets/dashboard-2.png)

### Deployment & Logs
![Logs](assets/dashboard-3.png)

---

👨‍💻 Author

- Saksham Kamra

  ---

⭐ If you like this project

- Give it a ⭐ on GitHub!
