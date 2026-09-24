#Maria Gomez-Arroyo

age_text=input("How old are you? ")
age_number=int(age_text)
# Using the int it will make them intergers and help formulate the math instead of a string.
print(age_number,type(age_number))
# Using type will help the system know which variable we are going to be using
print(f"You will be {age_number+10}")