# try:
#     with open("app.py") as file:
#         print("File opened")
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except ValueError:
#     print("You didn't enter a valid age.")
# else:
#     print("No exceptions were throws")
# print("Excution continues.")


# How to raise exceptions
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
