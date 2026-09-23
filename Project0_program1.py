#Thomas Pangelinan
age_text=input('How old are you now? ') 
age_number=int(age_text)
#Using int defines it and makes it a INT variable because they are always string at first
print(age_number,type(age_number))
#This just defines what type of variable it is.
print(f'Next year you will be {age_number+30}')
