# %%
import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep=";")
df.head()
# %%
# pegar só uma parcela do idCliente

def get_last_id(x):
    return x.split("-")[-1]
id_cliente = "000ff655-fa9f-4baa-a108-47f581ec52a1000ff655-fa9f-4baa-a108-47f581ec52a1"

# %%
get_last_id(id_cliente)
# %%
# não otimizado
novo_id = []
for i in df["IdCliente"]:
    novo = get_last_id(i)
    novo_id.append(novo)

novo_id

# %%
# >> usando pandas << aplica uma função elemento a elemento
df["IdCliente"].apply(get_last_id)
# %%


