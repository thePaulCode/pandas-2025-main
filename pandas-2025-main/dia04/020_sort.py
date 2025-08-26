# %%
import pandas as pd

# %%
df_clientes = pd.read_csv("../data/clientes.csv", sep=";")
df_clientes

# %%
# Ordenação de Series
df_clientes["QtdePontos"].sort_values()

# %%
# Ordenação de DF
(df_clientes.sort_values(by="QtdePontos", ascending=False)
            .head(3)["IdCliente"])
# %%
# numero
max_pontos = df_clientes["QtdePontos"].max()
max_pontos
# %%
# Series
filtro = df_clientes["QtdePontos"] == max_pontos
filtro
# %%
# DataFrame
type(df_clientes[filtro])

# %%
# Ordenar pelo salário e idade | idade desempata
briquedo = pd.DataFrame({
"nome": ["Paul", "Ana", "Stll"],
"idade": [34, 33, 35],
"salario": [10789, 9874, 10789]
})

# %%
# Salario em ordem decrescente False
# Idade em ordem crescente True
(briquedo
 .sort_values(by=["salario", "idade"], ascending=[False, True])
 )
# %%
