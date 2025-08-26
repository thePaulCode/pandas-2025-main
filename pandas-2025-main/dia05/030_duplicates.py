# %%
import pandas as pd


# %%
briquedo = pd.DataFrame({
"nome": ["Olavo", "Ana", "Stll", "Olavo"],
"idade": [33, 33, 35, 18],
"salario": [1078, 21078, 2350, 11078]
})
briquedo

# %%
# manter o último dado repedito, remover os anteriores
briquedo = briquedo.drop_duplicates(keep='last')



# %%
# criar regra para alguns dados repitidos
# como nome em cadastros etc
brinquedo = (briquedo.sort_values(by="salario", ascending=False)
.drop_duplicates(keep='last', subset=["nome"]))
brinquedo
# uma única chamada ordena e remove duplicates

# %%
import tabula
# %%
path = r"C:\Users\engen\OneDrive\Área de Trabalho\CasaLondrina\02 pollo ORÇAMENTO. 246265942.pdf"
path = path.replace("\\", "/")
path
# %%
apollo = tabula.read_pdf(path, pages="all", multiple_tables=True)
apollo
# %%
