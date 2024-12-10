from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def create_app() -> FastAPI:
    """Create the `FastAPI` application"""

    app = FastAPI()

    app.add_middleware(CORSMiddleware, allow_credentials=True, allow_methods=["*"])

    from .routes.root import router as root_router

    app.include_router(root_router)

    return app


app = create_app()
