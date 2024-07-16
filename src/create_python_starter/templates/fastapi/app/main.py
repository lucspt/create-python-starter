from fastapi import FastAPI


def create_app() -> FastAPI:
    """Create the fastify application"""

    app = FastAPI()

    from .routes.root import router as root_router

    app.include_router(root_router)

    return app


app = create_app()
