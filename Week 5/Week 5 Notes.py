#What is Boolean?
#Aboolean value is either true or false
#Examples 
print(5<10)
print(5>10)
print(3>=7)
print('cat'=='dog')

answer=input("Do you want to contunue? (yes or no) "). lower()
if answer=="yes":
    print("Continuing the program....")
elif answer=="no":
    print("How come you answer no?")
else:
    print("Okay, exiting now. ")


#Comparison Operators
# ==equal to 
# != not equal to
# > greater than
# <less than
# <=less than or equal to
# >=greater than or equal to


score=85
print(score>75)
print(score==75)
print(score!=85)


#How do we compare 3 values?
#We can compare 3 or more values with "and" & 'or'
temp=72
if temp >=68 and temp <=75:
    print("Comfy room temp")
#When using AND, both conditions must be true
#When using OR, at least one condition must be true

day="Saturday"
is_holiday=False
if day=="Saturday" or day=="Sunday" or is_holiday:
    print("You dont have class today")



#I want to print "You dont have class today"



score=75
if score <= score <90:          #score >=60 and score <90
    print("Mediorce grade")


#give me a conditional program that prints out shipping cost depending on total price
total=float(input("Enter yout total order: "))
if total<25:
    print("Shipping is $10")
elif total<50:
    print("Shipping is $5")
else:
    print("Shipping is free! ")



list1=[1,2,3]
list2=[1,2,3]
list3=list1

print(list1==list2)
print(list1 is list2)
print(list1==list3)
print(list1 is list3)
#== compares values and contents
# is, compares identity (are they literally the same object)




password=input("Enter your password")
if len(password)>8: #len is a build in function that counts how many characters my input was 
    print("This works")