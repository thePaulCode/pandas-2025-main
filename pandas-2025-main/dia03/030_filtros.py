# %%
import pandas as pd



# %%
df_clientes = pd.read_csv("../data/clientes.csv", sep=";")
df_clientes.head()

# %%
# Clientes com 0 pontos

df_clientes_pontos = df_clientes["QtdePontos"] == 0
df_clientes_pontos
# %%
clientes_0_view = df_clientes[df_clientes_pontos]
clientes_0_view

# %%
# filtro está apontando para o mesmo df
# porém só exibe onde o filtro é true
# performance memória
clientes_0_view["flag_1"] = 1
# %%
