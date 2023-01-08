name = input("What is your name? ")
print("Hi " + name + ", Welcome to Your first Python project!")
birth_year = input("What is your birth year? ")
age = 2023 - int(birth_year)
print("You will be " + str(age) + " this year!,")
print("Let's go do some addition!")
first_num = float(input("What is the first number? "))
second_num = float(input("What is the second number? "))
sum = first_num + second_num
print("The Total is: " + str(sum))
print(" ")
print("Calculations RULE!")
print(" ")
outside_temp = int(input("What is the outside temperature? "))
if outside_temp > 65:
    print("It's a hot day!")
    print("Drink!")
elif outside_temp > 40:
    print("It's a okay day!")
    print("PARTY!")
elif outside_temp < 39:
    print("Stay inside!")
    print("It is COLD!")
