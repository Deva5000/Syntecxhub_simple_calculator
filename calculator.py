
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b


def calculate(a, operator, b):
    if operator == "+":
        return add(a, b)
    elif operator == "-":
        return subtract(a, b)
    elif operator == "*":
        return multiply(a, b)
    elif operator == "/":
        return divide(a, b)
    else:
        return "Invalid operator!"


def main():
    print("===== SIMPLE CALCULATOR =====")
    print("Supported operators: +, -, *, /")
    print("Type 'clear' to reset or 'exit' to quit.")

    while True:
        user_input = input("\nEnter calculation: ").strip()

        if user_input.lower() == "exit":
            print("Calculator closed. Goodbye!")
            break

        if user_input.lower() == "clear":
            print("\nCalculator cleared!")
            continue

        try:
            parts = user_input.split()

            if len(parts) != 3:
                print("Invalid input! Example: 10 + 5")
                continue

            a = float(parts[0])
            operator = parts[1]
            b = float(parts[2])

            if operator not in ["+", "-", "*", "/"]:
                print("Invalid operator! Use +, -, * or /.")
                continue

            result = calculate(a, operator, b)
            print("Result:", result)

        except ValueError:
            print("Invalid input! Please enter valid numbers.")


if __name__ == "__main__":
    main()
