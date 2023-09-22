from tortoise import Tortoise
import dotenv
dotvalues = dotenv.dotenv_values()

async def connectToDatabase():
    await Tortoise.init(
        db_url=f"postgres://{dotvalues['POSTGRESQL_USER']}:{dotvalues['POSTGRESQL_DATABASE']}@localhost:5432/{dotvalues['POSTGRESQL_DATABASE']}",
        modules={'models': ['app.models']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()

def syncconnectToDatabase():
    Tortoise.init(
        db_url=f"postgres://{dotvalues['POSTGRESQL_USER']}:{dotvalues['POSTGRESQL_DATABASE']}@localhost:5432/{dotvalues['POSTGRESQL_DATABASE']}",
        modules={'models': ['app.models']}
    )
    # Generate the schema
    Tortoise.generate_schemas()