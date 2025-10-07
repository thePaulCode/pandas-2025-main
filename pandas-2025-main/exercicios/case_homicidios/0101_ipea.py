# %%
import pandas as pd
import os

# %%

def read_file(file_name: str):
    return (
        pd.read_csv(f"../../data0/ipea/{file_name}.csv", sep=";")
        .rename(columns={"valor":file_name})
        .set_index(["nome", "período"])
        .drop(["cod"], axis=1)
    )
# %%
read_file("homicidios")
# %%
dfs = []
file_name = os.listdir("../../data0/ipea/")

dfs
# %%
for i in file_name:    
    file_name = i.split(".")[0]
    dfs.append(read_file(file_name))
# %%
dfs
# %%
df_full = (pd.concat(dfs, axis=1)
           .reset_index()
           .sort_values(by=["período", "nome"]))
# %%
df_full
# %%
df_full.to_csv(r"g:\Meu Drive\TI\trilhaML\pandas-2025-main\pandas-2025-main\exercicios\case_homicidios\homicidios_consolidado.csv", sep=";", index=False)

# %%
