from fastapi import FastAPI
import dotenv, pathlib
from . import sample_endpoints, api
#from .db.connect import connectToDatabase, syncconnectToDatabase
from tortoise.contrib.fastapi import register_tortoise
app_path = pathlib.Path(__file__).parent.parent
dotvalues = dotenv.dotenv_values(app_path/".env")
app = FastAPI()

# Register Tortoise-ORM with FastAPI and PostgreSQL
register_tortoise(
    app,
    db_url=f"postgres://{dotvalues['POSTGRESQL_USER']}:{dotvalues['POSTGRESQL_DATABASE']}@localhost:5432/{dotvalues['POSTGRESQL_DATABASE']}",  # Replace with your PostgreSQL connection info
    modules={'models': ['__main__']},
    generate_schemas=True,
    add_exception_handlers=True,
)
app.include_router(sample_endpoints.router, prefix="/sample")
app.include_router(api.router, prefix="/api")