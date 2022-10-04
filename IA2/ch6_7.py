# Nhu Tran

def futureInvestmentValue(investmentAmount, monthlyInterestRate, years):
    futureInvestmentValue = investmentAmount * pow((1+monthlyInterestRate), (years*12))
    return futureInvestmentValue


def main():
    investmentAmount = float(input("Enter investment amount: "))
    interestRate = float(input("Enter annual interest rate: "))
    monthlyRate = interestRate / 1200
    
    print('Years' , '\t' , 'Future Value')

    for i in range(1,31):
        print(i, '\t' , round(futureInvestmentValue(investmentAmount, monthlyRate, i),2))

main()