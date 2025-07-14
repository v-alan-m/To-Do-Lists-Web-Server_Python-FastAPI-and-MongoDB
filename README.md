# 🧠 FastAPI To-Do List app with MongoDB


A lightweight and efficient backend web server built using **FastAPI** and **MongoDB**, ideal for modern Python-based RESTful APIs.

---

## 🚀 Features

- ⚡    FastAPI for high-performance async API routes  
- 🍃    MongoDB Atlas integration for cloud-hosted NoSQL storage  
- 🛠️   Clean structure and support for `.env` secrets  
- ♻    Auto-reload server on code changes during development

---

## 📦 Dependencies

Install the required Python packages using:

```bash
pip install fastapi uvicorn pymongo python-dotenv
pip install fastapi uvicorn pymongo
```


## 🍃 Setting Up MongoDB Atlas

1. Go to https://www.mongodb.com/
2. Log in
3. Click homepage logo > Project (Create New) > Connect > Drivers
4. Create a cluster and connect it via Drivers → Python 
   1. python -m pip install "pymongo[srv]"
5. Ensure the IP you are currently using is set as an allowed IP (within your MongoDB account within 'Network Access'.)


## ⚡ Run FastAPI Web App

```bash
uvicorn main:app --reload --no-use-colors
```