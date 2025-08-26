# %%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %%
# 05.01 - Crie uma coluna nova “twitch_points” que á
# resultado da multiplicação do saldo de pontos e a 
# marcação da twitch

clientes = pd.read_csv("../../data/clientes.csv", sep=";")
clientes
# %%
clientes["twitch_points"] = clientes["QtdePontos"]*clientes["FlTwitch"]
clientes.head()


# %%
# 05.02 - Aplique o log na coluna de saldo de pontos, 
# criando uma coluna nova

plt.figure(dpi=400)
plt.plot(clientes["IdCliente"], clientes["QtdePontos"])
# %%
clientes["LogPontos"] = np.log(clientes["QtdePontos"])

plt.plot(clientes["IdCliente"], clientes["QtdePontos"])
# %%
clientes.head()


# %%
# 05.03 - Crie uma coluna que sinalize se a
# pessoa tem vínculo com alguma (qualquer uma)
# plataforma de rede social.

clientes["AnySocial"] = clientes["FlEmail"]+	clientes["FlTwitch"]+	clientes["FlYouTube"]+clientes["FlBlueSky"]+	clientes["FlInstagram"]
clientes.head()
# %%


# 05.04 - Qual é o id de cliente que tem maior saldo de pontos?
# E o menor?

# %%
# Maior saldo de pontos
max = clientes["QtdePontos"].max()
max
filtro = clientes["QtdePontos"] == max
idClienteMaiorPontos = clientes["IdCliente"][filtro]
print(f"IdCliente com maior pontuação {idClienteMaiorPontos}, com {max} pontos")
# %%
# Menor saldo de pontos
min = clientes["QtdePontos"].min()
min
filtroMin = clientes["QtdePontos"] == min
idClienteMenorPontos = clientes["IdCliente"][filtroMin]
print(f"IdCliente com menor pontuação {idClienteMenorPontos}, com {min} pontos")

# %%
clientes.sort_values(by="QtdePontos", ascending=False).head(1)
# %%
clientes.sort_values(by="QtdePontos", ascending=True).head(1)

# %%
# 05.05 - Selecione a primeira transação diária de cada cliente.
# TODO
import pandas as pd

transacoes = pd.read_csv("../../data/transacoes.csv", sep=";")
transacoes.head()

# %%
#  ordenar pela data de criação
transacoes = transacoes.sort_values(by="DtCriacao")
    
transacoes
# %%
# criar a data da transacao to_datetime
transacoes["Data"] = pd.to_datetime(transacoes["DtCriacao"].str.replace(r"\s\+\d{4}\sUTC", "", regex=True), errors="coerce").dt.date
transacoes
# %%
# primeira transacao no dia
transacoes.drop_duplicates(keep="first", subset=["IdCliente", "Data"])
# %%
# última transacao no dia