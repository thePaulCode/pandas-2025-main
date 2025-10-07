# %%
import pandas as pd
# %%
import sqlalchemy
# %%
engine = sqlalchemy.create_engine(r"sqlite:///G:/Meu Drive/TI/trilhaML/pandas-2025-main/pandas-2025-main/data/olist.db")
with engine.connect() as conn:
    result = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print([row[0] for row in result])
# %%

# %%
clientes = pd.read_sql_table(table_name="tb_customers",
                             con=engine)
clientes.head()
# %%
query = "SELECT * FROM tb_customers LIMIT 100"
# %%
df_100 = pd.read_sql_query(query, con=engine)
df_100
# %%
