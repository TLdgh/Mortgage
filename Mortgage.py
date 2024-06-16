import numpy as np
import pandas as pd
import plotly.express as px

class Amortization:
    def __init__(self, Balance:list, Rate:float, N=25, Payment=[0],):
        self.Balance=Balance
        self.Rate=Rate
        self.N=N
        self.Interests=[0]
        self.Principal=[0]
        self.Payment=Payment
    
    def CalcPayment(self, N):
        t=0
        Time = list(range(0, N+1, 1))
        L=self.Balance[0]*self.Rate*(1+self.Rate)**N/((1+self.Rate)**N - 1)

        while self.Balance[-1] >=0:
            self.Interests.append(self.Balance[t]*self.Rate)
            self.Principal.append(L-self.Interests[t+1])
            self.Balance.append(self.Balance[t]-self.Principal[t+1])
            t+=1
        self.Payment=self.Payment+[L]*t
        self.printAmrt(t, Time)
        
    def CalcTime(self):
        t=0
        Time = [0]
        
        if(self.Payment==[0]):
            error_message="Payment amount cannot be 0."
            raise ValueError(error_message)
        elif(self.Payment[0]!=0):
            self.Payment=[0]+self.Payment
        
        while self.Balance[-1] >0 and t<(len(self.Payment)-1):
            self.Interests.append(self.Balance[t]*self.Rate)
            if(self.Payment[t+1]<self.Interests[t+1]):
                error_message="Payment amount cannot be less than the interest"
                raise ValueError(error_message)
            
            if(self.Balance[t]>=self.Principal[t]):
                pass
            else:
                self.Payment[t+1]=self.Balance[t]+self.Interests[t+1]
                
            self.Principal.append(self.Payment[t+1]-self.Interests[t+1])
            self.Balance.append(self.Balance[t]-self.Principal[t+1])
                
            t+=1
            Time.append(t)
        self.printAmrt(t, Time)
    
    def printAmrt(self,t,Time):
        data={"Time": Time[:t+1], 
              "Payment": self.Payment[:t+1], 
              "Interests": self.Interests[:t+1], 
              "Principal": self.Principal[:t+1], 
              "Balance": self.Balance[:t+1]}
        df=pd.DataFrame(data).round(3)
        print(df)

        #fig=px.line(df, x="Time", y="Balance")
        #fig.show()



Payment=[0, 12]
len(Payment)-1