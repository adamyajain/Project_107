import csv 
import pandas as pd
import plotly.express as px
df=pd.read_csv ('data.csv')
fig=px.scatter(df.groupby(['student_id','level'],as_index=False)['attempt'].mean(),x='student_id',y='level',size = 'attempt',color='attempt')
fig.show()
