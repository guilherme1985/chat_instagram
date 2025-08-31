import os
import dotenv 

from time import time
from GetAcoes import get_acoes
from GetBitcoin import get_bitcoin
from SalvaDB import insert_mongodb, insert_postgres

# Carrega variáveis de ambiente
dotenv.load_dotenv()

erro_count = 0
max_erros = 3

while erro_count < max_erros:
    try:
        bitcoin = get_bitcoin()
        acoes = get_acoes()
        try:
            insert_mongodb(bitcoin)
        except Exception as e:
            print(f"Erro ao inserir dados no MongoDB: {e}")
            erro_count += 1
            continue
        try:
            insert_postgres(acoes)
        except Exception as e:
            print(f"Erro ao inserir dados no PostgreSQL: {e}")
            erro_count += 1
            continue
        print("Dados inseridos com sucesso!")
        erro_count = 0
    except Exception as e:
        print(f"Erro ao obter ou inserir dados: {e}")
        erro_count += 1
    time.sleep(int(os.getenv("SLEEP", 60)))

if erro_count >= max_erros:
    print(f"Falha: atingido o limite de {max_erros} erros consecutivos. Encerrando execução.")