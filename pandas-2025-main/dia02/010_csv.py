# %%

import pandas as pd

# %%
df = pd.read_csv("../data/clientes.csv", sep=";")
df

# %%
df.to_csv("clientes.csv", index=False)

# %%
# %%
