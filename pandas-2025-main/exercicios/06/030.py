# %%
import pandas as pd
# %%
transacoes = pd.read_csv("../../data/transacoes.csv", sep=";")
transacoes

# %%
transacao_produto = pd.read_csv("../../data/transacao_produto.csv", sep=";")
transacao_produto

# %%
clientes = pd.read_csv("../../data/clientes.csv", sep=";")
clientes

# %%
# 06.03 - Qual usuário teve maior quantidade de 
# pontos debitados?
filtro = transacoes["QtdePontos"] < 0
filtro
# %%
(transacoes[filtro].groupby(by=["IdCliente"])["QtdePontos"]
 .sum()
 .sort_values(ascending=True)
 .head(1)
)

# %%
