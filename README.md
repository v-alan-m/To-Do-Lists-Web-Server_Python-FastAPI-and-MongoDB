# 🧠 FastAPI To-Do List app with MongoDB


A lightweight and efficient backend web server built using **FastAPI** and **MongoDB**, ideal for modern Python-based RESTful APIs.

---

## 🚀 Features

- ⚡    FastAPI for high-performance async API routes  
- 🍃    MongoDB Atlas integration for cloud-hosted NoSQL storage  
- 🛠️   Clean structure and support for `.env` secrets  
- ♻    Auto-reload server on code changes during development
- 🐳    Dockerized for easy deployment and environment consistency

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


## 🐳 Docker

This project is fully Dockerized for consistent development and deployment environments.

### 📦 Build the Docker image

```bash
docker build -t fastapi-todo-app .
```

### 🚀 Run the container

```bash
docker run -d -p 8000:8000 --env-file .env fastapi-todo-app
```

### 🔁 Development with live reload

#### Mac 
```bash
docker run -d -p 8000:8000 \
  -v $(pwd):/app \
  --env-file .env \
  fastapi-todo-app uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
#### Windows 
```bash
docker run -d -p 8000:8000 \
  -v %cd%:/app \
  --env-file .env \
  fastapi-todo-app uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Notes
 - **fastapi-todo-app** 
   - name of the Docker image
 - **uvicorn main:app** 
   - Start FastAPI app with Uvicorn
 - **--reload** 
   - Enables live-reload on code changes
 - **--host 0.0.0.0** 
   - Binds the app to all network interfaces inside the container, so it’s accessible from outside
 - **--port 8000** 
   - Exposes the app on port 8000 inside the container

### 🚀 Production Without live reload

```bash
docker run -d -p 8000:8000 \
  --env-file .env \
  fastapi-todo-app uvicorn main:app --host 0.0.0.0 --port 8000
```

#### Build docker container with the name fastapi using the dockerfile from the root dir:
```bash
docker build -t fastapi .
```

#### Images running, verify changes were made using timestamps 
```bash
docker images
```

#### Run docker server
```bash
docker run -p 8080:80 fastapi
```
- To view web server go to web browser and visit the URL: localhost:8080

#### Build container using the docker compose yaml file to view file changes dynamically
```bash
docker compose up --build 
```

#### List all the running containers
```bash
docker ps
```

####
- View the system logs
- Get the container ID, from running docker ps
  - 4a88d5012d41
```bash
docker attach 4a88d5012d41
```
E.g:
INFO:     Shutting down <br>
INFO:     Waiting for application shutdown. <br>
INFO:     Application shutdown complete. <br>
INFO:     Finished server process [16] <br>
INFO:     Stopping reloader process [1]

#### Initiate or run the dcoker container again without building it
```bash
docker compose up
```

#### Access the live container and view it's files through CLI terminal
- -it: Interactive terminal access
- /bin/bash: Open the terminal within the directory with the project
```bash
docker exec -it 4a88d5012d41 /bin/bash
```
- Check the contents of the directory to confirm that this is the correct directory
```bash
ls
```
