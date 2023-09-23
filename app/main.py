from fastapi import FastAPI
import dotenv, pathlib, urllib.parse
from . import sample_endpoints, api
#from .db.connect import connectToDatabase, syncconnectToDatabase
from tortoise.contrib.fastapi import register_tortoise
app_path = pathlib.Path(__file__).parent.parent
dotvalues = dotenv.dotenv_values(app_path/".env")
app = FastAPI()

# Register Tortoise-ORM with FastAPI and PostgreSQL
connection_string = f"postgres://{dotvalues['POSTGRESQL_USER']}:{urllib.parse.quote(dotvalues['POSTGRESQL_PASSWORD'])}@{dotvalues['POSTGRESQL_HOST']}:{dotvalues['POSTGRESQL_PORT']}/{dotvalues['POSTGRESQL_DATABASE']}"
#print("connection_string", connection_string)
register_tortoise(
    app,
    db_url=connection_string,  # Replace with your PostgreSQL connection info
    modules={'models': ['be.app.db.models']},
    generate_schemas=True,
    add_exception_handlers=True,
)
app.include_router(sample_endpoints.router, prefix="/sample")
app.include_router(api.router, prefix="/api")