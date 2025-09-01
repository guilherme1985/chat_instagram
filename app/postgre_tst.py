import os
import dotenv # type: ignore

from GetAcoes import get_acoes
from SalvaDB import insert_postgres

# Carrega variáveis de ambiente
dotenv.load_dotenv()

acoes = get_acoes()

try:
    insert_postgres(acoes)
    print("Dados inseridos com sucesso!")
except Exception as e:
    print(f"Erro ao inserir dados no PostgreSQL: {e}")

