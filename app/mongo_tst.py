import os
import dotenv

from GetBitcoin import get_bitcoin
from SalvaDB import insert_mongodb

# Carrega variáveis de ambiente
dotenv.load_dotenv()

##Conexao MongoDB
MONGODB_URL = os.getenv("MONGODB_URL")
MONGODB_DB = os.getenv("MONGODB_DB")
MONGODB_COLLECTION = os.getenv("MONGODB_COLLECTION")


bitcoin = get_bitcoin()


try:
    insert_mongodb(bitcoin)
    print("Dados inseridos com sucesso!")
except Exception as e:
    print(f"Erro ao inserir dados no MongoDB: {e}")


# use('db_mercado');
# db.getCollection('bitcoin').find().sort({ _id: -1 }).limit(1);