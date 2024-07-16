from fastapi import FastAPI
from app.main import app

def test_main_exports_app() -> None:
    
    assert isinstance(app, FastAPI)