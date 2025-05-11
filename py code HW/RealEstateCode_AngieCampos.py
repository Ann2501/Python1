#Assignment:Real Estate Analyzer
#Class: Python D80
#Date: 4/30/25
#Name: Angie Campos

#function for Float input:

def getFloatInput(sPrompt):
    while True:
        try:
            fValue = float(input(sPrompt))
            if fValue <= 0:
                raise ValueError
            return fValue
        except ValueError:
            print("Enter a valid positive numeric value.")

            
#Function for median, getMedian():
def getMedian(LstSales):
    iMid = len(LstSales) // 2
    # number of entries in the list
    if len(LstSales) % 2 == 0:
        return (LstSales[iMid] + LstSales [iMid - 1]) / 2
        #if even devide the count by 2.take entry an entry beofre it
        #average 2 elements and use that as median.
    else:
        return LstSales[iMid]
        #devide the count by 2 and use that entry as median

#Main Function, Prompt for info and choose to add more info:
def main():
    LstSales = []
    while True:
        fSale = getFloatInput("Enter Property sales value: ")
        LstSales.append(fSale)

        while True:
            sAddMore = input("Enter another value Y or N: ").upper()
            if sAddMore in ['Y', 'N']:
                break
            print("Please enter Y or N only.")

        if sAddMore == 'N':
            break
#calc:
    LstSales.sort()
    iLength = len(LstSales)
    #minimum
    fMin = LstSales[0]
    #maximum
    fMax = LstSales[-1]
    #sum
    fTotal = sum(LstSales)
    #avg
    fAvrg = fTotal / iLength
    #median
    fMedian = getMedian(LstSales)
    #commision
    fCommish = fTotal * 0.03

#display and format output:
    
    for index in range(iLength):
        print(f"Property {index + 1} ${LstSales[index]: 15,.2f}")
    print(f"{'Minimum:':12s} ${fMin: 15,.2f} ")
    print(f"{'Maximum:':12s} ${fMax: 15,.2f}")
    print(f"{'Total:':12s} ${fTotal: 15,.2f}")
    print(f"{'Average:':12s} ${fAvrg: 15,.2f}")
    print(f"{'Median:':12s} ${fMedian: 15,.2f}")
    print(f"{'Commission:':12s} ${fCommish: 15,.2f}")
        

main()

