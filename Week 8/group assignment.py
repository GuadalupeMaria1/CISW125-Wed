grocery_list=[]
while True:
    item=input("Enter an item for the grocery list (or type 'done' to finish): ")
    if item.lower() == 'done':
        break
    grocery_list.append(item)

print("Your grocery list:")
for item in grocery_list:
    print("- " + item)




 