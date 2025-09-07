import os
import dotenv
import psycopg2

from pymongo import MongoClient

#Carrega variáveis de ambiente
dotenv.load_dotenv()

##Conexao MongoDB
MONGODB_URL = os.getenv("MONGODB_URL")
MONGODB_DB = os.getenv("MONGODB_DB")
MONGODB_COLLECTION = os.getenv("MONGODB_COLLECTION")

##Conexao Postgres
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")

# Conexao no Postgre
def insert_postgres(df):
    if df.empty:
        print("DataFrame vazio, nada a inserir.")
        return
    
    try:
        conn = psycopg2.connect(
            dbname=POSTGRES_DB,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
            host=POSTGRES_HOST,
            port=POSTGRES_PORT
        )
        cursor = conn.cursor()
        for _, row in df.iterrows():
            cursor.execute(
                """
                INSERT INTO tbl_acoes (acao, nome, setor, preco, dt_req)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (row.get('acao'), row.get('nome'), row.get('setor'), row.get('preco'), row.get('dt_req'))
            )
        conn.commit()
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        cursor.close()
        conn.close()

# Conexao MongoDB com autenticaçao
def insert_mongodb(js):
    if js.empty:
        print("Json vazio, nada a inserir.")
        return
    try:
        client = MongoClient(MONGODB_URL)
        db = client[MONGODB_DB]
        collection = db[MONGODB_COLLECTION]
        
        # Converte o DataFrame para dict e insere
        data = js.to_dict(orient='records')
        result = collection.insert_many(data)
#        print(f"Inserted IDs: {result.inserted_ids}")
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        client.close()

