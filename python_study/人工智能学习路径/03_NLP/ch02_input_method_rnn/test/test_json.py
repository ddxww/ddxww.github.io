import pandas as pd

dfjo=pd.DataFrame(
    dict(A=range(1,4),B=range(4,7),C=range(7,10)),
    columns=list('ABC'),
    index=(list("xyz")),
)
print(dfjo)

dfjo.to_json("df_columns.json",orient="columns")
dfjo.to_json("df_index.json",orient="index")
dfjo.to_json("df_split.json",orient="split")
dfjo.to_json("df_records.json",orient="records")
dfjo.to_json("df_records_lines.json",orient="records",lines=True)
dfjo.to_json("df_values.json",orient="values")