try: nummer1 = float(input("What is the first number?\n"))
except(ValueError):
    print("This field is meant for numbers only\n")
    exit(0)

try: nummer2 = float(input("What is the second number?\n"))
except(ValueError):
    print("This field is meant for numbers only\n")
    exit(0)

print("Choose from: *, -, + /")
action = input("What action do you want?\n")

print("The answer is: ")
if action is "*":
    print(nummer1 * nummer2)
elif action is "-":
    print(nummer1 - nummer2)
elif action is "+":
    print(nummer1 + nummer2)
elif action is "/":
    print(nummer1 / nummer2)
else:
    print("This is not a valid option.")
