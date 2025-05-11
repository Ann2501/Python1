#Assignement: Paint Job Functions/Output Files
#Class: Python D80
#Date: 4/27/25
#Name: Angie Campos

#import file:
from math import ceil

#Create a function for float:
def getFloatInput(sPrompt):
    while True:
        try:
            iNumber = float(input(sPrompt))
            if iNumber <= 0:
                print("Please enter a number >0!")
                continue
            else:
                break
        except ValueError:
            print("Please enter a valid positive number!")

    return iNumber

#create functions for calc:
def getGallonsofPaint(fSqrFtWall,iFtGallonPaint):
    return ceil(fSqrFtWall / iFtGallonPaint)

def getLaborHours(fLaborHrsPerGallon,fSqrFtWall,iFtGallonPaint):
    return fLaborHrsPerGallon * ceil(fSqrFtWall / iFtGallonPaint)

def getLaborCost(fLaborHrsPerGallon,fSqrFtWall,iFtGallonPaint,fPaintLaborChrgHr):
    return  fLaborHrsPerGallon * ceil(fSqrFtWall / iFtGallonPaint) * fPaintLaborChrgHr

def getPaintCost(fSqrFtWall, iFtGallonPaint,fPaintPrice):
    return ceil(fSqrFtWall / iFtGallonPaint) * fPaintPrice

#function for state tax:
def getSalesTax(sState):
    if sState == 'CT' or sState == 'ct' or sState == 'VT' or sState == 'vt':
        return 0.06
    elif sState == 'MA' or sState == 'ma':
        return 0.0625
    elif sState == 'ME'or sState == 'me':
        return 0.085
    elif sState == 'RI' or sState == 'ri':
        return 0.07
    elif sState == 'NH' or sState == 'nh':
        return 0.0
    else:
        return 0.0
       
def showCostEstimate(sLastName, iTotalGallons, fLaborHours, fPaintCost, fLaborCost, fTaxRate):

    fTotalLaborCost = fLaborHours + fLaborCost
    fTotalTax = fTaxRate * (fLaborCost + fPaintCost)
    fTotalCost = fLaborCost + fPaintCost + fTotalTax
    sFileName = f"{sLastName}_PaintJobOutput.txt"

    print(f"Customer: {sLastName}")
    print(f"Gallons of Paint: {iTotalGallons:}")
    print(f"Hours of labor: {fLaborHours:.1f}")
    print(f"Paint charges: ${fPaintCost:,.2f}")
    print(f"Labor charges: ${fLaborCost:,.2f}")
    print(f"Tax: ${fTotalTax:,.2f}")
    print(f"Total cost: ${fTotalCost:,.2f}")

    with open(sFileName, "w") as file:
        file.write(f"Customer: {sLastName}")
        file.write(f"Gallons of Paint: {iTotalGallons}")
        file.write(f"Hours of labor: {fLaborHours}")
        file.write(f"Paint charges: {fPaintCost}")
        file.write(f"Labor charges: {fLaborCost}")
        file.write(f"Tax: {fTotalTax}")
        file.write(f"Total cost: {fTotalCost}")

    print(f"File {sFileName} was created.")
    
#Prompt for info:
def main():
    fSqrFtWall = getFloatInput("Enter wall space in square feet: ")    
    fPaintPrice = getFloatInput("Enter paint price per gallon: ")   
    iFtGallonPaint = getFloatInput("Enter feet per gallon: ")
    fLaborHrsPerGallon = getFloatInput("How many labor hours per gallon: ")
    fPaintLaborChrgHr = getFloatInput("Enter Painting Labor charge per hour: ")

    #string Prompts
    sState = input("Enter initials of state: ")
    sLastName = input("Enter client's last name: ")

    iTotalGallons = getGallonsofPaint(fSqrFtWall, iFtGallonPaint)
    fLaborHours = getLaborHours(fLaborHrsPerGallon, fSqrFtWall, iFtGallonPaint)
    fLaborCost = getLaborCost(fLaborHrsPerGallon, fSqrFtWall, iFtGallonPaint, fPaintLaborChrgHr)
    fPaintCost = getPaintCost(fSqrFtWall, iFtGallonPaint, fPaintPrice)
    fTaxRate = getSalesTax(sState)

    showCostEstimate(
        sLastName,
        iTotalGallons,
        fLaborHours,
        fPaintCost,
        fLaborCost,
        fTaxRate
        )
main()
