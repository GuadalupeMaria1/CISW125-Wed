a=10
b=3
c=a+b
d=a/b


#Whats the differenvce between int and flaot?
#Int is whole numbers, no decimals point (10,2,5,6,7,)
#Float contains decimals (10.25, 12.058, 12.52)

x=15 #int value

y=2.5 #Float

print(x, type (x))
print(y, type (y))

print(x//y) #// floor division, willgive whole number value
print(x/y) #/ regular division, this will give Float (decimal) value

user_text=input("Type something: ")
print(f"Hello, {user_text}")

age="22"
print(f"My age is {age} ")

age=input("What is your age?: ")
print(age, type(age))

#User input automatically converts input to string,
# regardless of what we have typed
age_text=input( "What is your age?: ") #asks for age, makes input string
age_int=int(age_text) #converting variable on line 32 into an INT
#string is 



word="Python"
print(word[0]) #This will selects the first character of the word

#Slicing is when we want to print a range from string text
print(word[0:3])
#Start:end means start at and stop before end [start:end]

#Built in python functions,
#.upper(), this converts string to all UPPER CASE
# .lower(), this converts string to al LOWER CASE
phrase="Hello, World"
print(phrase.upper())
print(phrase.lower())


fruits=["apple", "banana", "oranges"]
numbers=[10,2,3.5]
mixed=[100,"score",3.5]

print(fruits)
print(numbers)
print(fruits[0]) #This prints my first item in my list
print(fruits[0:2]) #This prints my first 2 items
#to add to a list, we append the list name
fruits.append("Kiwi")
print(fruits)