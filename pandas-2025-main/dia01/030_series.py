# %%
import pandas as pd

# %%
idades = [
    32, 38, 30, 31,
    35, 25, 31, 37,
    27, 19, 36, 33
]
# %%
series_idades = pd.Series(idades)
series_idades

# %%
series_idades.describe()

# %%
# Primeiro Elemento da Lista
idades[0]
# %%
#Último elemento da lista
idades[-1]

# %%
#Navegar nas séries
series_idades = series_idades.sort_values()
series_idades
# %%

series_idades[0]
# %%
series_idades.iloc[0]
# %%

series_idades.iloc[::-1]
# %%

# %%
index = [
    "Paul", "Stll", "Jsf", "Adlbt",
    "Moi", "Mn", "Bico", "Tg",
    "Aprcd", "Mrt", "Mr", "Anna"
]

# %%
series_idades = pd.Series(idades, index=index)
series_idades
# %%
series_idades.iloc[2]
# %%
