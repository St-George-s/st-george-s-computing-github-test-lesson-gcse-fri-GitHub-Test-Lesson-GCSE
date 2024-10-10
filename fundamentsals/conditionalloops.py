# Question 1

entercode = input("enter code : ")
while entercode != "rzy":
    print("incorrect, try again")
    entercode = input("enter code : ")  

# This will print after the loop as it is not indented
print("code accepted")

# Question 2

entercode = input("enter code : ")
while entercode != "4003":
    print("incorrect, try again")
    entercode = input("enter code : ")

# This will print after the loop as it is not indented
print("code accepted")

# Question 3

enterage = input("enter age : ")
while int(enterage) <=14:
    print("age not accepted")
    enterage = input("enter age : ")

# This will print after the loop as it is not indented
print("age accepted")

#Question 4

enterpassword = input("enter password: ")

while len(enterpassword) <= 5:
    print("incorrect password, please try again")
    enterpassword = input("enter password: ")

print("password accepted")

#Question 5

askwatch = input("would you like to watch another episode? : ")

while askwatch == "yes":
    print("playing another episode")
    askwatch = input("would you like to watch another episode? : ")

print("😡😡")

#Question 6

totalmoney=0
getmoneybig=int(input("give me money 🔫 : "))
totalmoney = totalmoney +getmoneybig

while totalmoney <=100:
    print("Current money in the bank is 🏦🏦😡😡😡: " + str(totalmoney))
    # Ask user for money
    getmoneybig=int(input("give me money 🔫 : "))
    #Add money to total
    totalmoney = totalmoney +getmoneybig

print("Thanks sucker 🏦🏦😊: " + str(totalmoney))


