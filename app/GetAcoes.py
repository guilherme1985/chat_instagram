import yfinance as yf
import pandas as pd

from datetime import datetime

def get_acoes() -> pd.DataFrame:
    # Top 10 ações no Ibovespa (por peso no índice)
    top_10 = [
        "PETR4.SA",  # Petrobras
        "VALE3.SA",  # Vale
        "ITUB4.SA",  # Itaú Unibanco
        "BBDC4.SA",  # Bradesco
        "B3SA3.SA",  # B3 
        "WEGE3.SA",  # Weg (Equipamentos elétricos)
        "ABEV3.SA",  # Ambev
        "MGLU3.SA",  # Magazine Luiza
        "RENT3.SA",  # Localiza
        "BBAS3.SA"   # Banco do Brasil
    ]
    dfs = []

    for a in top_10:
        ticket = yf.Ticker(a)
        info = ticket.info
        acao = info['symbol']
        preco = info['regularMarketPrice']
        nome = info['shortName']
        setor = info.get('sector', 'N/A')
        dt_rq = datetime.now().strftime("%Y-%m-%d %H:%M")

        df = pd.DataFrame({
            'acao': [acao],
            'nome': [nome],
            'setor': [setor],
            'preco': [preco],
            'dt_req': [dt_rq]
        })
        dfs.append(df)
    
    resultado = pd.concat(dfs, ignore_index=True)
    return resultado

# acoes = get_acoes()
# print(acoes)