#Part 1:

number=1 
while number<=5: 
    print(number)
    number+=1

#Part 2:

birth_year=int(input("Enter your birth year: "))
while  birth_year >= 1946 and birth_year <=1964:
    print("Baby boomer")
    birth_year=int(input("Enter your birth year: "))
print("Not a baby boomer")

#Part 3:

grocery=["Sugar", "Bread", "Milk"]
for groceryItem in grocery:
    print(groceryItem)

#Part 4:

for number in range(2,8):
    print(number)

#Part 5:

name="Maria"
for letter in name:
    print(letter)

#Part 6:

for number in range(1,11):
    print(number)
    if number==5: 
        break

#Part 7:

for number in range(1,4):
    for number2 in range(1,4):
        print(number, number2)