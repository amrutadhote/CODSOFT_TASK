def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


print("Select operation.")
print("1.Addition")
print("\U0001f600")
print("2.Subtraction")
print("\U0001f601")
print("3.Multiplication")
print("\U0001f602")
print("4.Division")
print("\U0001f607")

while True:
    
    choice = input("Enter choice(*1*2*3*4): ")

    
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter 1st number: "))
            num2 = float(input("Enter 2nd number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")