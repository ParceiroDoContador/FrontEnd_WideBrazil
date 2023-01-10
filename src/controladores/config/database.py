import os
from dotenv import load_dotenv

load_dotenv()

database_infos = {
    "app_key": os.getenv("APP_KEY"),
    "app_secret": os.getenv("APP_SECRET"),
    "id_conta_corrente": os.getenv("ID_CONTA_CORRENTE")
}