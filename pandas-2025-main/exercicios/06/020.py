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
# 06.02 - Quais são os usuários que mais fizeram transações? 
# Considere os 10 primeiros.

(transacoes.groupby(
    by=["IdCliente"],
    )["IdTransacao"]
    .count()
    .sort_values(ascending=False)
    .head(10))

# %%
