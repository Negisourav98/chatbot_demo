# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from app.api.chat import router

# app = FastAPI()

# # ✅ ENABLE CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],   # allow all (for development)
#     allow_credentials=True,
#     allow_methods=["*"],   # allow POST, OPTIONS, GET
#     allow_headers=["*"],
# )

# app.include_router(router)

# @app.get("/")
# def home():
#     return {"status": "AI Chatbot Running"}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from app.api.chat import router
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API router
app.include_router(router)

# Resolve base directory (For Azure)
APP_ROOT = os.getenv("APP_ROOT", os.getcwd())

# Serve frontend index.html
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_PATH = os.path.join(APP_ROOT, "..", "index.html")  #changed base_dir to APP_ROOT

@app.get("/")
def serve_frontend():
    return FileResponse(FRONTEND_PATH)
