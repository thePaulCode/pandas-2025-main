# %%
import pandas as pd
import requests

# %%
url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

dfs = pd.read_html(response.text)
uf = dfs[1]
# %%
uf.dtypes

# %%
def str_to_float(x:str):
    return float(x.replace(" ", "")
                 .replace(",", ".")
                 .replace("\xa0", "")
                )

# %%
numero = "281 748,5"

str_to_float(numero)
uf.columns
# %%


# %%
uf
# %%
uf["Área (km²)"] = uf["Área (km²)"].apply(str_to_float)
uf["População (Censo 2022)"] = uf["População (Censo 2022)"].apply(str_to_float)
uf
uf["PIB (2015)"] = uf["PIB (2015)"].apply(str_to_float)
uf["PIB per capita (R$) (2015)"] = uf["PIB per capita (R$) (2015)"].apply(str_to_float)
# %%
exp_vida_maior = uf["Expectativa de vida (2016)"].max()
exp_vida_maior
# %%
maximo = uf["Expectativa de vida (2016)"] == exp_vida_maior
maximo
# %%
uf["Abreviação"][maximo]
# %%
