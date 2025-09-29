# %%
import pandas as pd
# %%
transacoes = pd.read_csv("../../data/transacoes.csv", sep=";")
transacoes

# %%
transacao_produto = pd.read_csv("../../data/transacao_produto.csv", sep=";")
transacao_produto

# %%
clientes = pd.read_csv("../../data/clientes.csv", sep=";")
clientes

# %%
clientes["qtd_media_social"]  = (clientes["FlEmail"] + 
                                 clientes["FlTwitch"] + 
                                 clientes["FlYouTube"] + 
                                 clientes["FlBlueSky"] + 
                                 clientes["FlInstagram"])

# %%
media = clientes["qtd_media_social"].mean()
media
# %%
variancia = clientes["qtd_media_social"].var()
variancia
# %%
maximo = clientes["qtd_media_social"].max()
maximo

# %%
print("média", media)
print("variância", variancia)
print("máximo", maximo)

# %%
redes = ["FlEmail",
         "FlTwitch",
         "FlYouTube", 
         "FlBlueSky",
         "FlInstagram"
        ]

clientes[redes].sum(axis=1).describe()