# %%
import pandas as pd

# %%
df_clientes = pd.read_csv("../data/clientes.csv", sep=";")
df_clientes.head()
# %%

df_clientes["QtdePontos"].astype(int)
# %%
df_clientes["DtCriacao"] = pd.to_datetime(df_clientes["DtCriacao"].str.replace(r"\s\+\d{4}\sUTC", "", regex=True), errors="coerce")
df_clientes["DtCriacao"]
# Datas
# replace
# %%
df_clientes["DtCriacao"].dt.days_in_month