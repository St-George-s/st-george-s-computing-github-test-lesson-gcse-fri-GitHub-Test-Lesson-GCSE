numberofbearsmade = int(input("enter the number of teddy bears that were made: "))
numberofhoursworked = int(input("enter the amount of hours that were worked: "))
wagehoursworked = 0
wagebearsmade = 0

wagebearsmade = numberofbearsmade * 2
wagehoursworked = numberofhoursworked * 5

if wagebearsmade > wagehoursworked:
    print(wagebearsmade)
else:
    print(wagehoursworked)

