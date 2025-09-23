# Quem teve mais transacoes de Streak

# %%
import pandas as pd

# %%

transacoes = pd.read_csv("../../data/transacoes.csv", sep=";")
transacoes.head()

# %%
clientes = pd.read_csv("../../data/clientes.csv", sep=";")
clientes.head()
# %%
transacao_produto = pd.read_csv("../../data/transacao_produto.csv", sep=";")
transacao_produto = transacao_produto.dropna(subset=["IdProduto"])
transacao_produto["IdProduto"] = transacao_produto["IdProduto"].astype(int)
transacao_produto["IdProduto"]
# %%
produtos = pd.read_csv("../../data/produtos.csv", sep=";")
produtos = produtos.dropna(subset=["IdProduto"])
produtos["IdProduto"] = produtos["IdProduto"]
produtos.head()
# %%
produtos[produtos["DescProduto"] == 'Presença Streak']
# %%

# %%
transacao_cliente_merge = (transacoes.merge(right=clientes,
                 how='left',
                 on=['IdCliente'],
                 suffixes=["Transacoes", "Clientes"]))
   
# %%
transacao_cliente_prod = (transacao_cliente_merge.merge(right=transacao_produto,
                              how='left',
                              on=['IdTransacao']))[["IdTransacao", "IdCliente", "IdProduto"]]


# %%
transacao_cliente_prod = transacao_cliente_prod.dropna(subset=["IdProduto"])
transacao_cliente_prod["IdProduto"] = transacao_cliente_prod["IdProduto"].astype(int)
transacao_cliente_prod

# %%
df_full = transacao_cliente_prod.merge(
                                right=produtos,
                                how='left',
                                on=['IdProduto']
                                       )
df_full

# %%
df_full = df_full[df_full["DescProduto"] == "Presença Streak"]
df_full
# %%
(df_full.groupby(by=["IdCliente"])["IdTransacao"]
                .count()
                .sort_values(ascending=False)
                .head(1)
        )
produtos
# %%
prod = produtos[produtos["DescProduto"] == "Presença Streak"]
prod

# %%
(transacoes.merge(transacao_produto, 
                  how='left', 
                  on="IdTransacao"
            )     
            .merge(prod,
                   how='right',
                   on="IdProduto"
            )
            .groupby(by=["IdCliente"])["IdTransacao"]
            .count()
            .sort_values(ascending=False)
            .head(1)
)
# %%
