# Income: $2000
# Rental income = $2000

# Expenses: $1610
# Tax = $150, Insurance = $100, Mortgage = $860, Vacancy = $300, Repairs = $200 (Misc = $500)

# Cash Flow: $390 
# Income - Expenses 

# ROI: 9.36%
# Down Payment = $40000, Closing Costs = $3000, Rehab = $7000, Total Investments = $50000
# Annual Cash Flow / Total Investments

class ReturnOfInvestment():
    def __init__(self,income):
        self.income = income
        self.expenses = 0
        self.cashFlow = 0
        self.totalInvestments = 0

    def calculateExpenses(self,tax,insurance,mortgage,misc):
        self.expenses = tax + insurance + mortgage + misc


    def calculateCashFlow(self):
        self.cashFlow = self.income - self.expenses

    def calculateROI(self,downPayment,closingCosts,rehab):
        self.calculateExpenses(tax, insurance, mortgage, misc)
        self.calculateCashFlow()
        self.totalInvestments = downPayment + closingCosts + rehab
        annualCashFlow = self.cashFlow * 12
        investmentReturns = annualCashFlow / self.totalInvestments
        return f'{investmentReturns*100} %'

print('Please enter a dollar amount for the following (ONLY NUMERICAL VALUES ACCEPTED):')
income = float(input('Total monthly income: '))
tax = float(input('Monthly taxes: '))
insurance = float(input('Monthly insurance: '))
mortgage = float(input('Monthly mortgage: '))
misc = float(input('Monthly miscellaneous (vacancy, repairs, etc.): '))
downPayment=float(input('Down payment: '))
closingCosts=float(input('Closing costs: '))
rehab=float(input('Rehab cost: '))

ROI=ReturnOfInvestment(income)

returns=ROI.calculateROI(downPayment, closingCosts, rehab)

print(f'Your ROI is {returns}')
