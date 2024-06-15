import numpy as np
import pandas as pd
import plotly.express as px

Balance=[30000]
Payment=664.03
Rate=0.03/12
Interests=[0]
Principle=[0]
Time=[0]
t=0

while Balance[-1] >=0:
    Interests.append(Balance[t]*Rate)
    Principle.append(Payment-Interests[t+1])
    Balance.append(Balance[t]-Principle[t+1])
    t+=1
    Time.append(t)


data={"Time": Time, "Payment": [0]+[Payment]*t, "Interests": Interests, "Principle": Principle, "Balance": Balance}
df=pd.DataFrame(data)
print(df)

fig=px.line(df, x="Time", y="Balance")
fig.show()