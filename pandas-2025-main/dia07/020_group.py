# %%
import pandas as pd
# %%
transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes

transacoes
transacoes.groupby(by=["IdCliente"]).count()

# %%
# quantidade de transacoes
# index clientes["IdCliente"] , value QtdeTransacoes
transacoes.groupby(by=["IdCliente"], as_index=False)[["IdTransacao"]].count()
# %%
# quantidade de transacoes 
# e soma de pontos por Id
summary =(transacoes.groupby(by=["IdCliente"], as_index=False)
    .aggregate({
                "IdTransacao": ['count'], 
                "QtdePontos": ['sum', 'mean']
                }
            )
)
# %%
summary.columns
# %%
summary.columns = ['IdCliente', 'QtdeTransacao', 'TotalPontos', 'AvgPontos']
summary
# %%
