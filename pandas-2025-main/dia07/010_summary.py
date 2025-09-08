# %%
import pandas as pd
# %%
idades = [32,44,12,54,67,32,23,34,32,12,45,43,28,73,29]
idades = pd.Series(idades)
# %%
idades.shape
idades.sum()
idades.min()
idades.max()
idades.mean()
idades.describe()

# %%
clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes
# %%
clientes["FlTwitch"].sum()
clientes["FlTwitch"].mean()
# %%
redes_sociais = ["FlEmail",	"FlTwitch",	"FlYouTube", "FlBlueSky", "FlInstagram"]
clientes[redes_sociais].mean()
# %%
# usar somente as colunas númericas
filtro = clientes.dtypes == "object"
filtro
num_columns = clientes.dtypes[~(clientes.dtypes == "object")].index.tolist()

# %%
clientes[num_columns].mean()
clientes[num_columns].describe()

# %%
