import numpy_financial as npf
import pandas as pd


def getIRR(df, cols):
    res_df=df.copy()
    for col in cols:    
        y=[0]*len(df)
        for i in range(len(df)):
            res=df["Annual Premium"].iloc[0:i+1].tolist()
            res.append(df[col].iloc[i].tolist())
            y[i]=f"{round(npf.irr(res)*100,2)}%"
        res_df[f"IRR_{col}"]=y
        
    return res_df