# %%
import pandas as pd 
import os
# %%
homicidios = pd.read_csv("../../data0/ipea/homicidios.csv", sep=";")
homicidios

# %%
df_homicidios_negros = pd.read_csv("../../data0/ipea/homicidios-negros.csv", sep=";")

# %%
homicidios = homicidios.rename(columns={"valor": "homicídios"})
df_homicidios = homicidios
df_homicidios = df_homicidios.drop(["cod"], axis=1)
df_homicidios
# %%

df_homicidios_negros = df_homicidios_negros.rename(columns={"valor":"homicídios-negros"})
df_homicidios_negros
df_homicidios_negros = df_homicidios_negros.drop(["cod"], axis=1)
df_homicidios
# %%
df_homicidios = df_homicidios.set_index(["nome", "período"])
df_homicidios = df_homicidios.drop(["cod"], axis=1)



df_homicidios_negros = df_homicidios_negros.set_index(["nome", "período"])
df_homicidios_negros = df_homicidios_negros.drop(["cod"], axis=1)

df_homicidios_negros
df_homicidios
# %%
df_homicidios
# %%
df_homicidios.columns
pd.concat([df_homicidios, df_homicidios_negros], axis=1)

# %%
def etl_dataframe(x:pd.DataFrame, y:pd.DataFrame):
    x = x.rename(columns={"valor": "homicídios"})
    x = x.drop(["cod"], axis=1)
    y = y.rename(columns={"valor": "homicídios"})
    y = y.drop(["cod"], axis=1)
    return pd.concat([x, y], axis=1)


# %%
etl_dataframe(homicidios, df_homicidios_negros)
# %%
def read_file(file_name:str):
    return (pd.read_csv(f"../../data0/ipea/{file_name}.csv", sep=";")
            .rename(columns={"valor":file_name})
            .set_index(["nome", "período"])
            .drop(["cod"], axis=1)
    )

# %%
df_homicidios = read_file("homicidios")
# %%
df_homicidios_negros = read_file("homicidios-negros")
# %%

file_name = os.listdir("../../data0/ipea/")
dfs = []
for i in file_name:
    file_name = i.split(".")[0]
    dfs.append(read_file(file_name))
# %%
dfs[1]
# %%
df_full = (pd.concat(dfs, axis=1)
           .reset_index()
           .sort_values(["período", "nome"]))
# %%

df_full.to_csv(r"g:\Meu Drive\TI\trilhaML\pandas-2025-main\pandas-2025-main\exercicios\case_homicidios\homicidios_consolidado.csv", sep=";", index=False)
# %%
