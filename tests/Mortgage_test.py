import pytest

from Mortgage import Amortization

#use the default value N=25 in CalcPayment
def test1():
    result=Amortization(Balance=[30000], Rate=0.03/12)
    result.CalcPayment(result.N) #use the default value
    data=result.data
    
    assert data is not None and len(data["Time"]) == 26 and round(data["Payment"][1],3)==1239.389, "Failed to generate data frame."

def test2():
    result=Amortization(Balance=[30000], Rate=0.03/12)
    result.CalcPayment(N=48) #use the customized value
    data=result.data
    
    assert data is not None and len(data["Time"]) == 49 and round(data["Payment"][1],3)==664.03, "Failed to generate data frame."

def test3():
    #Customized payment schedule and estimate time needed:
    result=Amortization(Balance=[30000], Rate=0.03/12)#use the default value
    
    with pytest.raises(ValueError, match= "Payment amount cannot be 0."):
        result.CalcTime()

def test4():
    #Customized payment schedule and estimate time needed:
    result=Amortization(Balance=[30000], Rate=0.03/12, Payment=[0]+[664.03]*12)
    result.CalcTime()
    data=result.data
    
    assert data is not None and len(data["Time"]) == 13, "Failed to generate data frame."

def test5():
    #Customized payment schedule and estimate time needed:
    result=Amortization(Balance=[30000], Rate=0.03/12, Payment=[664.03]*12)
    result.CalcTime()
    data=result.data
    
    assert data is not None and len(data["Time"]) == 13, "Failed to generate data frame."

def test5():
    #Customized payment schedule and estimate time needed:
    result=Amortization(Balance=[30000], Rate=0.03/12, Payment=[664.03]*12+[10000]+[1200]*12)
    result.CalcTime()
    data=result.data
    
    assert data is not None and len(data["Time"]) == 25 and round(data["Payment"][13],3)==10000.000, "Failed to generate data frame."

