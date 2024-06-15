import numpy as np
import pandas as pd
import plotly.express as px

#Calculate Payment amount if n is known:
Balance=[30000]
Rate=0.03/12
Interests=[0]
Principle=[0]
n=25
t=0
Time = list(range(0, n+1, 1))

Payment=Balance[0]*Rate*(1+Rate)**n/((1+Rate)**n - 1)

while Balance[-1] >=0:
    Interests.append(Balance[t]*Rate)
    Principle.append(Payment-Interests[t+1])
    Balance.append(Balance[t]-Principle[t+1])
    t+=1
Payment=[0]+[Payment]*t

#Customized payment schedule and estimate time needed:
Balance=[30000]
Rate=0.03/12
Payment=[0]+[664.03]*48
Interests=[0]
Principle=[0]
t=0
Time = [0]

while Balance[-1] >=0 and t<=len(Payment):
    Interests.append(Balance[t]*Rate)
    Principle.append(Payment[t+1]-Interests[t+1])
    Balance.append(Balance[t]-Principle[t+1])
    t+=1
    Time.append(t)

data={"Time": Time[:t+1], "Payment": Payment[:t+1], "Interests": Interests[:t+1], "Principle": Principle[:t+1], "Balance": Balance[:t+1]}
df=pd.DataFrame(data).round(3)
print(df)

fig=px.line(df, x="Time", y="Balance")
fig.show()

