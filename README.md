# To-Do Manager App

A simple **To-Do Manager** application built as part of Task 2. The project demonstrates a full-stack CRUD workflow with a **frontend** (HTML, CSS, JS) hosted on **Vercel** and a **backend** (Python FastAPI/Flask) hosted on **Render**.

---

## 🚀 Features

* Add tasks with title and description
* View list of tasks
* Delete tasks
* Backend API built with Python (FastAPI/Flask)
* Frontend built with HTML, CSS, JavaScript
* Hosted frontend on **Vercel**
* Hosted backend on **Render**
* Cross-origin support (CORS enabled)

---

## 🏗️ Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python (FastAPI)
* **Hosting:**

  * Frontend → Vercel
  * Backend → Render

---

## 📂 Project Structure

```
📦 To-Do Manager
 ┣ 📜 index.html        # Frontend UI
 ┣ 📜 main.py           # FastAPI backend
 ┣ 📜 requirements.txt  # Dependencies
 ┗ 📜 README.md         # Documentation
```

---

## ⚙️ Setup Instructions

### 1. Clone repository

```bash
git clone https://github.com/your-username/todo-manager.git
cd todo-manager
```

### 2. Backend Setup (FastAPI on Render)

1. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run locally:

   ```bash
   uvicorn main:app --reload
   ```

   Visit: [http://127.0.0.1:8000/tasks](http://127.0.0.1:8000/tasks)

4. Deploy to **Render**

   * Add `requirements.txt`
   * Add a start command:

     ```bash
     gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
     ```
   * Deploy and note the Render URL (e.g., `https://todo-manager-backend.onrender.com`).

### 3. Frontend Setup (on Vercel)

1. Update `index.html` → set API URL:

   ```js
   const API_URL = "https://todo-manager-backend.onrender.com";
   ```
2. Push frontend files (`index.html`, CSS, JS) to GitHub.
3. Deploy repo on **Vercel**.
4. Visit your live app at `https://todo-manager.vercel.app`.

---

## 📌 API Endpoints

* `GET /tasks` → Get all tasks
* `POST /tasks` → Create a new task
* `PUT /tasks/{id}` → Update a task
* `DELETE /tasks/{id}` → Delete a task

---

## 🎯 Usage

1. Open the deployed frontend.
2. Add a task (title + description).
3. Tasks will appear in the list.
4. Click **Delete** to remove a task.

---

## 🔮 Bonus Enhancements (Optional)

* AI-powered task suggestions
* Task prioritization & deadlines
* Persistent database (SQLite/Postgres)
* Authentication (user-based task lists)

---

## 📽️ Demo

A short 2–3 min screen recording is available here:
https://drive.google.com/file/d/1ozqo96GsizYc2wXww-nCaCqOkXqTfl1Y/view?usp=drive_link

Frontend(UI) accessible here: https://to-do-manager-task-2-m03tz2qmk-rahul-vamshis-projects.vercel.app/
Backend accessible here to check the tasks created: https://to-do-manager-task-2.onrender.com/tasks


---

## 👨‍💻 Author

Built with ❤️ for Task 2 challenge.
