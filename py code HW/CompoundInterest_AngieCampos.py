#Assignment:Compound Interest
#Class:Python CIT-115 D80 
#Date:4/4/25
#Name: Angie Campos


#Input (prompt the user for info)

fPrinciple = float(input("Enter the starting principal:"))

fInterest = float(input("Enter the annual interest rate:"))

fRate = float(input("How many times per year is the interest be compounded?"))

iYears = int(input("For how many years will the account earn interest?"))


#PROCESS(calculate using info - result)
fFutureValue = fPrinciple *(1 + (fInterest/100) / fRate)**(iYears * fRate)

#OUTPUT (display the results to user - formatted)
print(f"At the end of {iYears} years you will have ${fFutureValue:,.2f}")

#print(result)

