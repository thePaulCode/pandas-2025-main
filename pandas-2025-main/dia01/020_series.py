# %%

import pandas as pd

# %%
idades = [
    32, 38, 30, 31,
    35, 25, 31, 37,
    27, 23, 36, 33
]



# %%
series_idades = pd.Series(idades)


# %%
#Média
series_idades.mean()
# %%
# Variância
series_idades.var()
# %%
summary_idades = series_idades.describe()

# %%
summary_idades
# %%
