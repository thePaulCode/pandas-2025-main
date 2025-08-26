# %%
import pandas as pd
import numpy as np

# %%
import matplotlib.pyplot as plt
# %%
df_clientes  = pd.read_csv("../data/clientes.csv", sep=";")
df_clientes.head()

# %%
df_clientes["Pontos Mil"] = df_clientes["QtdePontos"] + 1000

# %%

# %%
df_clientes.describe()
# %%
# Operação em 2 Series
df_clientes["emailTwich"]=df_clientes["FlEmail"] + df_clientes["FlTwitch"]
df_clientes.head()

# %%
# Intersecção dos 2 dados
df_clientes["FlTwich e FlEmail"] = df_clientes["FlTwitch"] * df_clientes["FlEmail"]
df_clientes.head()

# %%
# Qtde de Redes Sociais
df_clientes["QtdeSocial"] = df_clientes["FlEmail"]	+ df_clientes["FlTwitch"]+ 	df_clientes["FlYouTube"]	+ df_clientes["FlBlueSky"]	+ df_clientes["FlInstagram"]

df_clientes["QtdeSocial"].describe()

# %%
# Ao menos 1 rede social
df_clientes["Qtde_1_Social"] = df_clientes["QtdeSocial"] == 1
nova_col = pd.DataFrame(df_clientes["Qtde_1_Social"])
nova_col

# %%
df_clientes["log_pontos"] = np.log(df_clientes["QtdePontos"]+1)
df_clientes["log_pontos"].describe()
# %%
plt.hist(df_clientes["log_pontos"])

plt.show()
# %%
