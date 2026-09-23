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
favgame="Apex Legends"
leastfavgame="Rocket League"
upcominggame="GTA 6"
# Then print your variables.
print(f"{leastfavgame} {upcominggame} {favgame}")
# Now try to reassign a value. This is essentially "overwriting" your variables data with new data. Python works from top to bottom.
favgame="R6"
# After you've done this, try to print your variables in string using f-strings.
print(f"My favorite game is {favgame} and my least favorite game is {leastfavgame}")

# Next, try to create some expressions that involve addition, subtraction, multiplication, and division
# Store the results of your expressions in a variable and then print the outcome
apartment=5+4
room=2
print(apartment+room)
# See if you can find other ways to "do maths" (hint: operators are useful and efficient.)
# https://www.w3schools.com/python/python_operators.asp


# Now, I'd like you to make two variables that contain your first and last name
# After you've made the variables, find a way to join the two strings to print your full name. This is string concatenation.
# Think of it as "adding" your variables together.
x="Thomas"
y="Pangelinan"
print(f"My name is {x} {y}")
# While we did some math earlier, I'd like you to try doing math with variables this time. (If you already did this, you can skip this. Good job.)


# Lastly, do something of your own choice. Anything that involves variables and expressions is allowed here.
# If you're stumped on ideas, just try and make an expression that converts Celsius to Fahrenheit or vice versa.
n="notebook"
x=30
y=4
print(f"The answer in the {n} was {x*y}")
# Upload this to Canvas under the Variable and Expressions Lab assignment.
