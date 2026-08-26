# CISW 125
# Intro to programming

# Follow the Documentation Policy as it's good practice and will get you used to what you should do for
# your projects and other labs.

# If you're stuck, ask questions. There are no dumb questions.
# ------------------------------------------------------------------------------------------------------
# We're going to play around with variables and expressions today
# The goal is to just test out things and put them to use and possibly
# save the ideas/work for projects down the line.

# Again, the goal is to "play" around and explore. There's no right or wrong to this.
# Just think about input vs output and what we can do with them.
# ------------------------------------------------------------------------------------------------------


# Create some variables, give them a theme. Example: items on a grocery list, games/books/movies you enjoy, etc.
favmovie="Bee Movie"
favshow="Game of Thrones"
leastfavmovie="Life"
leastfavshow="Regular Show"
newfavmovie="The Day After Tomorrow"
newfavshow="Greys Anatomy"

# Then print your variables.
print(favmovie)
print(favshow)
print(leastfavmovie)
print(leastfavshow)
print(newfavmovie)
print(newfavshow)

# Now try to reassign a value. This is essentially "overwriting" your variables data with new data. Python works from top to bottom.
favshow="House of Dragons"
favmovie="Tangled"
leastfavshow="Punisher"
leastfavmovie="Encanto"

# After you've done this, try to print your variables in string using f-strings.
print(f"My favorite show is {favshow} because it is enjoyable.")
print(f"My favorite movie is {favmovie} because it is enjoyable.")
print(f"My least favorite show is {leastfavshow} because it is not much enjoyable.")
print(f"My least favorite movie is {leastfavmovie} because it is not much enjoyable.")

# Next, try to create some expressions that involve addition, subtraction, multiplication, and division
# Store the results of your expressions in a variable and then print the outcome
addition=10+2 
subtraction=10-2
multiplication=10*2
division=10/2

print(addition)
print(subtraction)
print(multiplication)
print(division)

# See if you can find other ways to "do maths" (hint: operators are useful and efficient.)
# https://www.w3schools.com/python/python_operators.asp
#+ is for addition
#- is for subtraction
#* is for multiplication
#/ is for division

# Now, I'd like you to make two variables that contain your first and last name
# After you've made the variables, find a way to join the two strings to print your full name. This is string concatenation.
# Think of it as "adding" your variables together.
firstname="Maria"
lastname="Gomez-Arroyo"
fullname=firstname+lastname
print(fullname)

# While we did some math earlier, I'd like you to try doing math with variables this time. (If you already did this, you can skip this. Good job.)
w=10
x=5
y=2
z=w+x+y
print(z)

# Lastly, do something of your own choice. Anything that involves variables and expressions is allowed here.
# If you're stumped on ideas, just try and make an expression that converts Celsius to Fahrenheit or vice versa.
age=22
major="Operations Management"
print(f"I am {age} years old and my major is {major}.") 

# Upload this to Canvas under the Variable and Expressions Lab assignment.
