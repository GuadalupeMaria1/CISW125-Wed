signal_color=input("Enter the color of the light")
is_blinking=input("Is the light blinking? ")
if signal_color=='red':
    if is_blinking=="yes":
        print("This is a 4 way stop basically")
    else:
        print("Stop")


#Login Program
username=input("What is your username")
password=input("What is your password?")
if username=='admin':
    if password=="cat":
        print("Login successful")
    else:
        print("Password")