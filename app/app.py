import time

from GetAcoes import get_acoes
from GetBitcoin import get_bitcoin
from SalvaDB import insert_mongodb, insert_postgres

MAX_ERROS = 5
INTERVALO = 60  # segundos

def alimenta_banco():
    erro_count = 0
    while erro_count < MAX_ERROS:
        try:
            bitcoin = get_bitcoin()
            acoes = get_acoes()
            try:
                insert_mongodb(bitcoin)
            except Exception as e:
                print(f"[MongoDB] Erro ao inserir dados: {e}")
                erro_count += 1
                continue
            try:
                insert_postgres(acoes)
            except Exception as e:
                print(f"[PostgreSQL] Erro ao inserir dados: {e}")
                erro_count += 1
                continue
            print("Dados inseridos com sucesso!")
            erro_count = 0
            break # Sai do loop após sucesso
        except KeyboardInterrupt:
            print("Execução interrompida pelo usuário.")
            break
        except Exception as e:
            print(f"Erro inesperado: {e}")
            erro_count += 1
#TESTE LOCAL
#        time.sleep(INTERVALO)

    if erro_count >= MAX_ERROS:
        print(f"Falha: atingido o limite de {MAX_ERROS} erros consecutivos. Encerrando execução.")

if __name__ == "__main__":
    alimenta_banco()