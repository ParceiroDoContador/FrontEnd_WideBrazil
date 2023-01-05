import os
from dotenv import load_dotenv

load_dotenv()

database_infos = {
    "app_key": os.getenv("APP_KEY"),
    "app_secret": os.getenv("APP_SECRET"),
    "id_conta_corrente": os.getenv("ID_CONTA_CORRENTE"),
    "teste_app_key": os.getenv("TESTE_APP_KEY"),
    "teste_app_secret": os.getenv("TESTE_APP_SECRET"),
    "teste_id_conta_corrente": os.getenv("TESTE_ID_CONTA_CORRENTE")
}