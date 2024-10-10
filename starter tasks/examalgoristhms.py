# ///////////////////////////////////////////////////////

firstname = input("Enter first name : ")
surname = input("Enter surname : ")

gender = input("M or F : ")

if gender == "M":
    name = surname[-3:]
    username = name + firstname[0:2]

else:
    name = firstname[0:3]
    username = name + surname[0:2]

print(username)

# ///////////////////////////////////////////////////////

#store names in array
names = ["Helen","Adam","Lidia","Kwaku","Priya","Chan"]
#input places moved
placesmoved=int(input("Enter places moved : "))
#loop for places moved
for count in range(placesmoved):
    #store last name in temporary variable
    temporary = names[5]
    names[5] = names[4]
    names[4] = names[3]
    names[3] = names[2]
    names[2] = names[1]
    names[1] = names[0]
    names[0] = temporary
    
print(names)

# ///////////////////////////////////////////////////////