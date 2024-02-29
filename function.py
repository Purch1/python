# def greet(firs_name, last_name):
#     print(f"Hi {firs_name} {last_name}")
#     print("welcome aboard")


# greet("Prince", "Ikechukwu")

# def mutiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print("Start")
# print(mutiply(1, 2, 3))


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input


print(fizz_buzz(7))
