# 🏋️ AI Fitness Helper with AI Nutritionist 🤖🥗

This project provides a simple web application that offers personalized fitness and nutrition advice based on a user's height, weight, and activity level. It uses OpenAI's GPT model to generate human-like recommendations.

---

## 🚀 Features

- AI-powered fitness & nutrition recommendations
- Calculates daily caloric needs using basic health formulas
- Personalized meal suggestions and fitness tips
- Built using FastAPI (backend) and vanilla HTML/CSS/JS (frontend)

---


## 🖥️ How to Run Locally

### 🔧 Requirements

- Python 3.9+
- Node.js (only if you expand frontend logic later)
- OpenAI API Key

### 1. Clone the Repository

```bash
git clone https://github.com/basantapokharel/fuse_ai.git
cd ai-fitness-helper
```

### 2. Set Up the Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r ../requirements.txt
```

Add your OpenAI API key in `openai.api_key` line inside `app.py` or load it from `.env`.

### 3. Run FastAPI Server

```bash
uvicorn app:app --reload
```

### 4. 



## ⚙️ Configuration Notes

- The frontend and backend are decoupled, communicating via HTTP `POST` request to `/api/fitness`.
- CORS is enabled in FastAPI to allow frontend access.
- Customize your prompt for better AI formatting (see `app.py`).

---

## 📽️ Demo Video

Watch the short demo here: [Demo Video](https://drive.google.com/your-demo-link)

---

## ✅ Status

- [x] FastAPI backend functional
- [x] OpenAI integration working
- [x] Frontend UI completed
- [x] JSON POST communication implemented
- [x] AI-generated HTML displays nicely in the frontend

---


## 🙌 Credits

Built using:

- [FastAPI](https://fastapi.tiangolo.com/)
- [OpenAI GPT-3.5](https://platform.openai.com/)
- HTML, CSS, JavaScript

---
