# %%
import pandas as pd

# %%
df = pd.read_csv("../data/clientes.csv", sep=";")
df

# %%
# Tratar Valores NotANumber NaN
df_completo = df.dropna(how="any")
df_completo

# %%
# Regra para o NaN
briquedo = pd.DataFrame({
"nome": ["Paul", None, "Stll"],
"idade": [None, 33, 35],
"salario": [10789, 9874, None]
})
briquedo
# %%
# todas linhas permanecem, pois a linha toda
# precisa ser Na
briquedo.dropna(how="all")

# %%
# somente a linda 2 permace, pois o any excluí
# a linha que contenha ao menos 1 Na
briquedo.dropna(how="any")

# %%
# excluir linha baseado em Regra
# coluna idade com Na, excluir
briquedo.dropna(subset=["idade"])
# %%
# excluir linha baseado em Regra
# how="all" coluna idade && salário com Na, excluir
briquedo.dropna(how="all", subset=["idade", "salario"])
# %%
# excluir linha baseado em Regra
# how="any" coluna idade || salário com Na, excluir
briquedo.dropna(how="any", subset=["idade", "salario"])
# %%
# Fill Na - preeencher os valores em vazio / branco
briquedo["idade"] = briquedo['idade'].fillna("18")
briquedo
# %%
briquedo["nome"] = briquedo["nome"].fillna("Nome Cliente")
briquedo

# %% 
# Estratégia de imputação de valores
briquedo.fillna({"nome": "Fulano", "idade": "21"})
# %%

# %%
# Preencher com médias idade e salário
media = briquedo[["idade", "salario"]].mean()
briquedo.fillna(media)
# %%
