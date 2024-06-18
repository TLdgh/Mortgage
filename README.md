# Mortgage
This is a project to analyze amortization of loans or mortgages.

The class Amortization can be genereated given a number of inputs:

The Balance shoud be the total loan amount to begin with in the analysis.

The Rate variable should be a list consisting of sublists of interest value and effective month. For example [[1, 0.05], [5, 0.03]] represents that in the beginning of month 1, the interest rate is 0.05. It changes to 0.03 in the 5th month.

The CalcPayment function estimates the equal monthly payement needed to pay out the loan based on given rates and terms (N is the number of years required to payout).

The Payment variable is needed for the CalcTime method, for which you have to specify your own payment schedule. You may initially give a rough guess of how many payments you need, and CalcTime should calculate the final number of months of payments for the entire loan. Note if you don't start with enought payments, you can get a message indicating that your balance is not paid out, and thus you need to add more terms. Therefore adding more terms of payment is recommanded.  

The BalancePctPay is an optional variable indicating that your loan can be paid with extra payments per year based on a percentage of your outstanding balance. This rate should be converted to monthly basis. For example if your bank allows extra payment equal to 10% of your outstanding balance per year, you should enter 0.1/12.

the plotResult function simply plots two amortization schedules and compares them.