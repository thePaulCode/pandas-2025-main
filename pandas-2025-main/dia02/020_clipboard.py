# %%
import pandas as pd

# %%
url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

dfs = pd.read_html(url)
dfs
# %%
len(dfs)

# %%
type(dfs)

# %%
df_uf = dfs[1]
df_uf

df_uf.to_csv("ufs.csv", sep=";", index=False)

# %%
df_uf
# %%
