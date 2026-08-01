# argocd_deploy_repo2/hello/apps/greet/src/main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/greet")
def get_fortune():
    return {
        "service": "greet", 
        "message": "오늘의 인사는 겁나게 반갑습니다"
    }