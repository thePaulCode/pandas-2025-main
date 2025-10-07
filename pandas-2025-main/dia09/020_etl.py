# %%
import pandas as pd
import sqlalchemy
from sklearn import cluster

# %%
with  open("020_etl.sql") as open_file:
    query = open_file.read()

print(query)
# %%
engine = sqlalchemy.create_engine("sqlite:///../data/olist.db")
df = pd.read_sql_query(query, con=engine)
df

# %%
kmean = cluster.KMeans(n_clusters=4)
kmean.fit(df[["total_revenue","total_sales"]])
# %%
df["cluster"]=kmean.labels_
df
# %%
df.to_sql("sellers_cluster", 
          con=engine, 
          index=False,
          if_exists="replace")