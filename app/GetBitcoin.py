import requests as rq
import pandas as pd
import os
import dotenv

from datetime import datetime

#Carrega variáveis de ambiente
dotenv.load_dotenv()   
URL_BITCOIN = os.getenv("URL_BITCOIN")

res = rq.get(URL_BITCOIN)
bc_price = res.json()

def get_bitcoin() -> pd.DataFrame:

    # Requisição para a API e conversao para json
    res = rq.get(URL_BITCOIN)
    bc_price = res.json()

    # Extração
    preco = float (bc_price['data']['amount'])
    cripto = 'BTC'
    moeda = 'USD'
    dt_rq = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Dataframe
    df = pd.DataFrame({
        'preco': [preco],
        'cripto': [cripto],
        'moeda': [moeda],
        'dt_req': [dt_rq]
    })

    return df

# vlr_bitcoin = get_bitcoin()
# print(vlr_bitcoin)
