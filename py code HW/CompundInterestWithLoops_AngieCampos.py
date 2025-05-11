#Assignment: Compount Interes w/Loops
#Class: Python D80
#Date Finished:
#Date Started:4/23/25
#Name: Angie Campos

#add a loop:
while True:
    
#Prompt for info:
    try:
        fDeposit = float(input("What is the Original Deposit: "))
        if fDeposit > 0:
            break
        print("Please provide numeric value > 0")
    except ValueError:
        print("Must be a positive numeric value.")
            
while True:
    try:
        fInterest = float(input("What is the Interes Rate: "))
        if fInterest > 0:
            break
        print("Please provide numeric value > 0")
    except ValueError:
        print("Must be a positive numeric value.")

while True:
    try:
        iNumberMonths = int(input("What is the Number of Months: "))
        if iNumberMonths > 0:
            break
        print("Please provide a numeric value > 0")
    except ValueError:
        print("Must be a whole numeric value")

while True:
    try:
        fGoalAmount = float(input("What is the Goal Amount: "))
        if fGoalAmount >= 0:
            break
        print("Please provide numeric value >=5 0")
    except ValueError:
        print("Must be a positive numeric value.")
       
    

#Prescess Calculation:
#fFutureValue = fDeposit *(1 + (fInterest/12) /100)
    
fInterestRate = (fInterest / 12) / 100
fValue = fDeposit

#1 for loop
#calculation per months requested:
for iMonth in range(1, iNumberMonths):
    fValue += fValue * fInterestRate
    print(f"Month: {iMonth} Account balance: ${fValue:,.2f}")
    iMonth += 1

#1 while (condition) loop
#months to reach goal:
if fGoalAmount > 0 and fGoalAmount > fDeposit:
    iMonth = 0
    while fGoalAmount > fDeposit:
        fDeposit += fDeposit * fInterestRate
        iMonth += 1
    print(f"It will take {iMonth} months to reach your goal of ${fGoalAmount:,.2f}")
