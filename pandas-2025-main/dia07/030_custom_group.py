# %%
import pandas as pd
import numpy as np

# %%
transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes.head()

# %%
""" # sqrt((amplitude - mean)**2)
def diff_amp(x:pd.Series):
    amplitude = x.max() - x.min()
    media = x.mean()
    return np.sqrt((amplitude - media)**2)

# %%
(transacoes.groupby(by=["IdCliente"])
    .aggregate({
        "IdTransacao": ["count"],
        "QtdePontos": ["sum", "mean", diff_amp]
    })
) """

# %%
transacoes["DtCriacao"] = transacoes["DtCriacao"].str.replace(r"\s\+\d{4}\sUTC", "", regex=True)
transacoes["DtCriacao"]
# %%
def life_time(x:pd.Series):
    dt = pd.to_datetime(x)
    return (dt.max() - dt.min()).days
# %%

(transacoes.groupby(by=["IdCliente"])
            .agg({
                "DtCriacao":[life_time],
            }).sort_values(by=("DtCriacao", "life_time"), ascending=False)
)
# %%
