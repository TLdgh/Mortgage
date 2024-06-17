import numpy as np
import pandas as pd
import plotly.express as px
from functools import reduce

class Amortization:
    def __init__(self, Balance:list, Rate:list, N=25, Payment=[0], BalancePctPay=None):
        self.Balance=Balance
        self.BalancePctPay=BalancePctPay
        self.Rate=Rate
        self.N=N
        self.Interests=[0]
        self.IntRate=[0]
        self.Principal=[0]
        self.Payment=Payment
    
    def CalcPayment(self, N):
        for rate in self.Rate:
            trunc_point=rate[0]
            n=N-trunc_point+1
            r=rate[1]
            self.Balance=self.Balance[0:trunc_point]
            self.Interests=self.Interests[0:trunc_point]
            self.Principal=self.Principal[0:trunc_point]
            self.Payment=self.Payment[0:trunc_point]
            self.IntRate=self.IntRate[0:trunc_point]
        
            L=self.Balance[-1]*r*(1+r)**n/((1+r)**n - 1)
        
            t=trunc_point-1
            while self.Balance[-1]>0:
                self.Interests.append(self.Balance[t]*r)
                self.Principal.append(L-self.Interests[t+1])
                self.Balance.append(self.Balance[t]-self.Principal[t+1])
                t+=1
            
            self.Payment=self.Payment+[L]*n
            self.IntRate=self.IntRate+[r]*n

        self.printAmrt(t=N+1, Time= list(range(0, N+1, 1)))
        
    def CalcTime(self):
        t=0
        Time = [0]

        if(self.Payment==[0]):
            error_message="Payment amount cannot be 0."
            raise ValueError(error_message)
        elif(self.Payment[0]!=0):
            self.Payment=[0]+self.Payment
        
        while self.Balance[-1] >0 and t<(len(self.Payment)-1):
            r=self.determine_r(self.Rate, t+1)
            self.IntRate.append(r)
            self.Interests.append(self.Balance[t]*r)
            if(self.Payment[t+1]<self.Interests[t+1]):
                error_message="Payment amount cannot be less than the interest"
                raise ValueError(error_message)
            
            if self.BalancePctPay is not None:
                if isinstance(self.BalancePctPay, float):
                    self.Payment[t+1]=self.Payment[t+1]+self.Balance[t]*self.BalancePctPay
                else:
                    raise ValueError("BalancePctPay must be a float")
            
            if(self.Balance[t]>=self.Principal[t]):
                pass
            else:
                self.Payment[t+1]=self.Balance[t]+self.Interests[t+1]
            
                
            self.Principal.append(self.Payment[t+1]-self.Interests[t+1])
            self.Balance.append(self.Balance[t]-self.Principal[t+1])
                
            t+=1
            Time.append(t)
        
        self.printAmrt(t+1, Time)        
        if(self.Balance[-1]!=0):print("WARNING: Your balance is not paid out, please add more payment terms.")

    
    def printAmrt(self,t,Time):
        data={"Time": Time, 
              "IntRate": self.IntRate[:t],
              "Payment": self.Payment[:t], 
              "Interests": self.Interests[:t], 
              "Principal": self.Principal[:t], 
              "Balance": self.Balance[:t]}
        df=pd.DataFrame(data).round(3)
        self.data=df
        print(df)
    
    def determine_r(self, Rate, t):
        for i in range(len(Rate) - 1):
            start, rate = Rate[i]
            end, temp_r = Rate[i + 1]
            if start <= t < end:
                return rate
        # If t is greater than the last start value, return the last rate
        return Rate[-1][1]

def plotResult(dfs:dict):
    df_join=reduce(lambda left, right: 
        pd.merge(left[["Time", "Balance", "Interests"]], 
                 right[["Time", "Balance", "Interests"]], 
                 on="Time", how="outer"), dfs.values())

    df_join_Bal=df_join[[col for col in df_join.columns if "Balance" in col or "Time" in col]]
    df_join_Bal=df_join_Bal.melt(id_vars="Time", var_name="Variable", value_name="Value")
    fig=px.line(df_join_Bal, x="Time", y="Value", color="Variable", labels={'value': "Balance", 'x':"Month"})
    fig.show()
    
    df_join_Int=df_join[[col for col in df_join.columns if "Interests" in col or "Time" in col]]
    df_join_Int.iloc[:,1:]=df_join_Int.iloc[:,1:].cumsum()
    df_join_Int=df_join_Int.melt(id_vars="Time", var_name="Variable", value_name="Value")
    fig=px.line(df_join_Int, x="Time", y="Value", color="Variable", labels={'Value': "Cumulative Interests", 'x':"Month"})
    fig.show()
    
