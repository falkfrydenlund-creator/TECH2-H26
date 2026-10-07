import numpy as np
taxes=0
income = 0
def tax(income):
    taxes=0
    """
    Return the taxes owed for a given income
    
    Pratmeters
    ----------
    income
        Gross income
        
    returns
    -------
    tax owed
    """
    if income <= 300_000:
        taxes = 0
    elif 300000 <= income <= 700000:
        taxes = (income - 300_000) * 0.2
    else:
        taxes = (income - 700_000) * 0.35 + 0.2 * (700_000 - 300_000)

    return taxes

incomes = np.linspace(0, 1_200_000, 13)
print(incomes)

taxes_loop = []

for income in incomes:
    #compute taces for current income level
    taxes = tax(income)
    taxes_loop.append(income)
    net_income = income - taxes

    print(f'Gross income: {income:10.0f}'
          f'Taxes: {taxes:10.0f}'
          f'Net income: {net_income:10.0f}')
