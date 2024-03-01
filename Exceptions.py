try:
    with open("app.py") as file:
        print("File opened")
    age = int(input("Age: "))
    xfactor = 10 / age
except ValueError:
    print("You didn't enter a valid age.")
else:
    print("No exceptions were throws")
print("Excution continues.")