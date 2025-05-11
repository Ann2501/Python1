#Assignment: Grade Analyzer
#Class: Python D80
#Date finished:4/20/25
#Date started:4/11/25
#Name:Angie


#Prompt name:
sName = input("Name of person that we are calculating the grades for: ")

#Prompt for 4 test scores:
iTest1 = int(input("Test 1: "))
iTest2 = int(input("Test 2: "))
iTest3 = int(input("Test 3: "))
iTest4 = int(input("Test 4: "))

#Ask y/n drop lowest grade?:
sDropLowest = input("Do you wish to Drop the Lowest Grade Yes or No? ")

#error message ask for numeric value greater than 0:
if iTest1 < 0 or iTest2 < 0 or iTest3 < 0 or iTest4 < 0:
    print("Test scores must be greater than 0.")
    raise SystemExit

#If statements for 'Y' or 'N' input:
if sDropLowest.upper() == 'Y':
    fDivisor = 3.0
    if iTest1 <= iTest2 and iTest1 <= iTest3 and iTest1 <= iTest4:
        iLowest = iTest1
    elif iTest2 <= iTest3 and iTest2 <= iTest4:
        iLowest = iTest2
    elif iTest3 <= iTest4:
        iLowest = iTest3
    else:
        iLowest = iTest4

elif sDropLowest.upper() == 'N':
    fDivisor = 4.0
    iLowest = 0

#error message ask for 'Y' or 'N' only    
else:
    print("Enter Y or N to Drop the Lowest Grade.")
    raise SystemExit

#Calculate the average Score:
fAverage = ((iTest1 + iTest2 + iTest3 + iTest4) - iLowest) / fDivisor

#Thanks to Prof C's Monday Class...Boom 💥
#get letter grade:
if fAverage >= 90.0:
    sLetterGrade = "A"
elif fAverage >= 80.0:
    sLetterGrade = "B"
elif fAverage >= 70.0:
    sLetterGrade = "C"
elif fAverage >= 60.0:
    sLetterGrade = "D"
else:
    sLetterGrade = "F"

#Check if a + or - is needed on the Letter Grade:
iFirstDigit = int(fAverage % 10)
if iFirstDigit >= 7 or fAverage >= 100:
    sLetterGrade += '+'
elif iFirstDigit <= 3:
    sLetterGrade += '-'


#output:
print(f"{sName} test average is: {fAverage:.1f}")
print(f"Letter Grade for the test is: {sLetterGrade}")

        
