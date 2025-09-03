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
# converter idade
def str_to_float_idade(x:str):
    return float(x.split(" ")[0]
                 .replace(",",".")
                )

uf["Expectativa de vida (2016)"] = uf["Expectativa de vida (2016)"].apply(str_to_float_idade)
uf

# %%
exp_vida = uf["Expectativa de vida (2016)"][0]
lista_exp_vida = exp_vida.split(" ")
idade = lista_exp_vida[0].replace(",",".")
float(idade)
# %%
# converter Alfabetização (2016) 0 - 1
uf.head()
def alfabetizacao_0_1(x:str):
    return float(x.replace("%", "")
                 .replace(",", "."))/100

uf["Alfabetização (2016)"] = uf["Alfabetização (2016)"].apply(alfabetizacao_0_1)
uf
# %%
alfabeto = uf["Alfabetização (2016)"][0]
alfabeto_0_1 = float(alfabeto.replace("%", "").replace(",", "."))/100
alfabeto_0_1
# %%
# converter IDH (2010) 0 - 1

def idh_to_0_1(x:str):
    return float(x)/1000

uf["IDH (2010)"]=uf["IDH (2010)"].apply(idh_to_0_1)
uf.head()
# %%
# converter 0 - 1000 Mortalidade infantil (2016)uf
def mortalidade_inf_to_0_1(x:str):
    return float(x.replace("‰","")
                  .replace(",","."))*10
uf["Mortalidade infantil (2016)"] = uf["Mortalidade infantil (2016)"].apply(mortalidade_inf_to_0_1)
uf.head()
# %%
# Uf to Regiao
def uf_to_regiao(uf:str):
    if uf in ["Distrito Federal", "Goiás", "Mato Grosso", "Mato Grosso do Sul"]:
        return "Centro-Oeste"
    elif uf in ["Alagoas","Bahia", "Ceará", "Maranhão", "Paraíba", "Pernambuco", "Piauí", "Rio Grande do Norte", "Sergipe"]:
        return "Nordeste"
    elif uf in ["Acre", "Amapá", "Amazonas", "Pará", "Rondônia", "Roraima", "Tocantins"]:
       return "Norte"
    elif uf in ["Espírito Santo","Minas Gerais", "Rio de Janeiro", "São Paulo"]:
        return "Sudeste"
    elif uf in ["Paraná", "Rio Grande do Sul", "Santa Catarina"]:
        return "Sul"
    
uf["Região"] = uf["Unidade federativa"].apply(uf_to_regiao)
uf.head()

# %%
# Maior IDH
filtro = uf["IDH (2010)"] == uf["IDH (2010)"].sort_values(ascending=False).iloc[0]

uf[filtro]
# %%

# Pior Expectativa de vida (2016)
filtro = uf["Expectativa de vida (2016)"] == uf["Expectativa de vida (2016)"].sort_values().iloc[0]

uf[filtro]
# %%
# Se pib / capitar > 30.000 && 
# mortalidade < 150 && 
# idh > 0.7 -> "parece bom" : "IDH de Mongólia"

def classificar_cidade(linha):
    if(linha["PIB per capita (R$) (2015)"] > 30000.0 and 
    linha["IDH (2010)"] > 0.7 and
   linha["Mortalidade infantil (2016)"] < 150.0):
        return "Parece bom"
    else:
        return "Não Parece bom"

# %%
uf["Classificação da Cidade"] = uf.apply(classificar_cidade, axis=1)
uf
# %%
