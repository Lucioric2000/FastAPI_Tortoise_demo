from tortoise import Tortoise, run_async
import dotenv, pathlib
app_path = pathlib.Path(__file__).parent.parent
dotvalues = dotenv.dotenv_values(app_path/".env")

async def init():
    # Here we create a SQLite DB using file "db.sqlite3"
    #  also specify the app name of "models"
    #  which contain models from "app.models"
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['db.models']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()

# run_async is a helper function to run simple async Tortoise scripts.
run_async(init())