#///////////////////////////////////////////////////////
age = int(input("enter age: "))
gender = input("enter gender: ")
dose = 0.0
ispregnant = False

if age <20:
    dose = age*0.1

else:
    dose = 2

if gender == "female":
    ispregnant = input("are you pregnant: ")
    if ispregnant =="yes" and dose > 1.5:
        dose = 1.5

else:
    dose = dose*0.5

print(dose)