#Student Robert Doult
#Date 09022019
#Class CSCI 1511 - Lab 2-3
#3. Write a Tipper program where the user enters a restaurant bill total.
#The program should then display two amounts: a 15 percent tip and a 20 percent tip.

totalBill = input ("Please enter the total bill.")
print ()
totalBill = float (totalBill)

tip15 = totalBill * 0.15
#temp = tip15*100
#temp = int(temp)/100.0
#print(temp)


print ("A 15% percent tip $""{0:.2f}".format(tip15))
total15 = totalBill + tip15



print ()

tip20 = totalBill * 0.20
print ("A 20% percent tip $""{0:.2f}".format(tip20))
total20 = totalBill + tip20

print("\nGrand Total with 15%:$=""{0:.2f}".format(total15))
print("\nGrand Total with 20%:$=""{0:.2f}".format(total20))

input("\n\nPress the enter key to exit.")
