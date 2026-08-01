# argocd_deploy_repo2/hello/apps/fortune/src/main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/fortune")
def get_fortune():
    return {
        "service": "fortune", 
        "message": "너무 기분좋아요!"
    }