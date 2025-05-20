from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="AI Trading Sandbox")

app.include_router(router)
