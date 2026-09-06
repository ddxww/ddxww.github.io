import pandas as pd

dfjo=pd.DataFrame(
    dict(A=range(1,4),B=range(4,7),C=range(7,10)),
    columns=list('ABC'),
    index=(list("xyz")),
)
print(dfjo)
print(dfjo.to_json('dict'))
print(dfjo.to_json('list'))
print(dfjo.to_json('series'))
print(dfjo.to_dict('split'))
print(dfjo.to_dict('tight'))
print(dfjo.to_dict('records'))
print(dfjo.to_dict('index'))
df=pd.DataFrame(
    [{"input":[1,2,3,4,5,6],"output":[7]},
     {"input":[2,3,4,5,6,7],"output":[8]},
     {"input":[2,3,4,5,6,7],"output":[9]},
     ]
)
print(df.to_dict('records'))
