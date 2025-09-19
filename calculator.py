def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("That's not a valid number. Please try again.")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Error: division by zero.")
        return None
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    if b == 0:
        print("Error: modulus by zero.")
        return None
    return a % b

def main():
    while True:
        print("\n=== Simple Calculator ===")
        print("1) Add")
        print("2) Subtract")
        print("3) Multiply")
        print("4) Divide")
        print("5) Power")
        print("6) Modulus")
        print("7) Exit")

        choice = input("Choose (1-7): ").strip()

        if choice == "7":
            print("Goodbye!")
            break

        if choice in ("1", "2", "3", "4", "5", "6"):
            n1 = get_number("First number: ")
            n2 = get_number("Second number: ")

            if choice == "1":
                res = add(n1, n2)
            elif choice == "2":
                res = subtract(n1, n2)
            elif choice == "3":
                res = multiply(n1, n2)
            elif choice == "4":
                res = divide(n1, n2)
            elif choice == "5":
                res = power(n1, n2)
            elif choice == "6":
                res = modulus(n1, n2)

            if res is not None:
                print("Result:", round(res, 8))
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()
