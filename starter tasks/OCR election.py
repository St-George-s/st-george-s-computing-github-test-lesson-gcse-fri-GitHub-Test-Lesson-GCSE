vote = input("do you vote for A B or C? or enter 'END' to finish. ").upper()
totala=0
totalb=0
totalc=0

while vote != "END":
    if vote == "A":
        totala=totala+1
    elif vote =="B":
        totalb=totalb+1
    elif vote =="C":
        totalc=totalc+1
    else:
        print("Invalid vote.")
    vote = input("do you vote for A B or C? or enter 'END' to finish. ").upper()

    
print("Candidate A got " + str(totala) + " votes")
print("Candidate B got " + str(totalb) + " votes")
print("Candidate C got " + str(totalc) + " votes")