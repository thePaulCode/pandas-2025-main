# %%
import pandas as pd

idades = [
    32, 38, 30, 31,
    35, 25, 31, 37,
    27, 19, 36, 33
]

nomes = [
    "Paul", "Stll", "Jsf", "Adlbt",
    "Moi", "Mn", "Bico", "Tg",
    "Aprcd", "Mrt", "Mr", "Anna"
]

# %%

series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)
series_idades
series_nomes

# %%
df = pd.DataFrame()
df["idades"] = series_idades
df["nomes"] = series_nomes
df
type(df)

# %%
# Acessar Series no DataFrame
df["nomes"]
df["idades"]
df.iloc[0]
type(df.iloc[0])

# %%
# Primeira pessoa do DF
df.iloc[0]["nomes"]

# %%
# Idade da última pessoa
df.iloc[-1]["idades"]
