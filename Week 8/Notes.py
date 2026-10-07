#LOOP THROUGH 1-10
#FOR NUMBER IN RANGE (1,11):
# PRINT THE CURRENT NUMBER
# PRINT (NUMBER)


#Countdown Timer
#from time import time


seconds=int(input("Enter the time you want to countdown from: "))
while seconds>=0:
    if seconds==3:
       print("Almost there!")
    elif seconds==0:
        print("Time's up!")
    else:
       print(seconds )
    seconds-=1



        #Bank Program
balance=1000
while True:
    print(f"{balance}, Balance")
    choice=input("Deposit, withdraw or exit ").lower()
    if choice=="deposit":
        amount=float(input("Amount:"))
        balance+=amount
    elif choice=="withdraw":
        amount=float(input("How much money do you want to take out "))
        if amount>balance:
            print("Not enough funds")
        else:
            balance-=amount
    elif choice=="exit":
        break
print(f"Your final balance is {balance}")


#Random number generator
print("Guess the number: ")
target=4
while True:
    guess=int(input("Enter your guess "))
    if guess<target:
        print("Too low")
    elif guess>target:
        print("Too high")
    else:
        break #correct guess exit loops
print("Correct! The number was", target )



#Create a grocery list
#make an empty list
grocery_list=[]
while True:
    #Ask the user if they want to add an item to the list
    userInput=input("Do you want to add an item to the grocery list? (yes/no) ")
    if userInput=="yes":
        #Ask the user for the item they want to add
        item=input("Enter the item you want to add: ")
        #Add the item to the list
        grocery_list.append(item)
    elif userInput=="no":
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")