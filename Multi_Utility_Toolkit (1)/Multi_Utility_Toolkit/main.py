from datetime import datetime
import math
import random
import string
import time
import uuid

from utilities import file_operations, math_utils


def pause():
    input("\nPress Enter to continue...")


def get_number(prompt, cast=float):
    while True:
        try:
            return cast(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def datetime_menu():
    while True:
        print("""
Datetime and Time Operations:
1. Display current date and time
2. Difference between two dates
3. Format date into custom format
4. Stopwatch
5. Countdown timer
6. Back to Main Menu
""")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            print("Current Date and Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        elif choice == "2":
            try:
                first = datetime.strptime(input("Enter first date (YYYY-MM-DD): "), "%Y-%m-%d")
                second = datetime.strptime(input("Enter second date (YYYY-MM-DD): "), "%Y-%m-%d")
                print("Difference:", abs((second - first).days), "days")
            except ValueError:
                print("Invalid date. Use YYYY-MM-DD.")
        elif choice == "3":
            try:
                date_text = input("Enter date (YYYY-MM-DD): ")
                date_value = datetime.strptime(date_text, "%Y-%m-%d")
                fmt = input("Enter format (e.g. %d-%m-%Y): ").strip() or "%d-%m-%Y"
                print("Formatted date:", date_value.strftime(fmt))
            except ValueError:
                print("Invalid date or format.")
        elif choice == "4":
            input("Press Enter to start the stopwatch...")
            start = time.perf_counter()
            input("Press Enter to stop...")
            print(f"Elapsed time: {time.perf_counter() - start:.2f} seconds")
        elif choice == "5":
            seconds = get_number("Enter countdown seconds: ", int)
            if seconds < 0:
                print("Seconds cannot be negative.")
            else:
                try:
                    while seconds:
                        print(f"Time remaining: {seconds} second(s)", end="\\r", flush=True)
                        time.sleep(1)
                        seconds -= 1
                    print("\\nTime is up!")
                except KeyboardInterrupt:
                    print("\\nCountdown cancelled.")
        elif choice == "6":
            return
        else:
            print("Invalid choice.")
        pause()


def math_menu():
    while True:
        print("""
Mathematical Operations:
1. Calculate Factorial
2. Solve Compound Interest
3. Trigonometric Calculations
4. Area of Geometric Shapes
5. Unit Conversion (km to miles)
6. Back to Main Menu
""")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            n = get_number("Enter a non-negative integer: ", int)
            if n < 0:
                print("Factorial is not defined for negative integers.")
            else:
                print("Factorial:", math.factorial(n))
        elif choice == "2":
            principal = get_number("Enter principal amount: ")
            rate = get_number("Enter annual interest rate (%): ")
            years = get_number("Enter time (years): ")
            frequency = get_number("Compounding periods per year (e.g. 1, 4, 12): ", int)
            if principal < 0 or years < 0 or frequency <= 0:
                print("Amounts/time must be non-negative and frequency must be positive.")
            else:
                amount = principal * (1 + rate / (100 * frequency)) ** (frequency * years)
                print(f"Final Amount: {amount:.2f}")
                print(f"Compound Interest: {amount - principal:.2f}")
        elif choice == "3":
            degrees = get_number("Enter angle in degrees: ")
            radians = math.radians(degrees)
            print(f"sin({degrees}) = {math.sin(radians):.4f}")
            print(f"cos({degrees}) = {math.cos(radians):.4f}")
            print(f"tan({degrees}) = {math.tan(radians):.4f}" if abs(math.cos(radians)) > 1e-10 else "tan is undefined for this angle.")
        elif choice == "4":
            print("1. Circle  2. Rectangle  3. Triangle")
            shape = input("Choose shape: ").strip()
            if shape == "1":
                radius = get_number("Enter radius: ")
                print(f"Area: {math.pi * radius ** 2:.2f}" if radius >= 0 else "Radius cannot be negative.")
            elif shape == "2":
                length = get_number("Enter length: ")
                width = get_number("Enter width: ")
                print(f"Area: {length * width:.2f}" if length >= 0 and width >= 0 else "Dimensions cannot be negative.")
            elif shape == "3":
                b = get_number("Enter base: ")
                h = get_number("Enter height: ")
                print(f"Area: {0.5 * b * h:.2f}" if b >= 0 and h >= 0 else "Dimensions cannot be negative.")
            else:
                print("Invalid shape.")
        elif choice == "5":
            km = get_number("Enter distance in kilometres: ")
            print(f"{km} km = {math_utils.km_to_miles(km):.2f} miles")
        elif choice == "6":
            return
        else:
            print("Invalid choice.")
        pause()


def random_menu():
    while True:
        print("""
Random Data Generation:
1. Generate Random Number
2. Generate Random List
3. Create Random Password
4. Generate Random OTP
5. Random Sample from Dataset
6. Coin Toss Game
7. Back to Main Menu
""")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            low = get_number("Minimum: ", int)
            high = get_number("Maximum: ", int)
            if low <= high:
                print("Random number:", random.randint(low, high))
            else:
                print("Minimum must not exceed maximum.")
        elif choice == "2":
            count = get_number("How many numbers? ", int)
            low = get_number("Minimum value: ", int)
            high = get_number("Maximum value: ", int)
            if count < 0 or low > high:
                print("Please enter a valid count and range.")
            else:
                print("Random list:", [random.randint(low, high) for _ in range(count)])
        elif choice == "3":
            length = get_number("Enter password length (minimum 4): ", int)
            if length < 4:
                print("Password length must be at least 4.")
            else:
                alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
                password = [random.choice(string.ascii_lowercase), random.choice(string.ascii_uppercase),
                            random.choice(string.digits), random.choice("!@#$%^&*")]
                password += [random.choice(alphabet) for _ in range(length - 4)]
                random.shuffle(password)
                print("Generated password:", "".join(password))
        elif choice == "4":
            digits = get_number("OTP length (4-8): ", int)
            if 4 <= digits <= 8:
                print("Generated OTP:", "".join(random.choices(string.digits, k=digits)))
            else:
                print("Choose an OTP length from 4 to 8.")
        elif choice == "5":
            data = [item.strip() for item in input("Enter comma-separated items: ").split(",") if item.strip()]
            count = get_number("Sample size: ", int)
            if 0 <= count <= len(data):
                print("Random sample:", random.sample(data, count))
            else:
                print("Sample size must be between 0 and", len(data))
        elif choice == "6":
            print("Coin toss:", random.choice(["Heads", "Tails"]))
        elif choice == "7":
            return
        else:
            print("Invalid choice.")
        pause()


def file_menu():
    while True:
        print("""
File Operations (Custom Module):
1. Create a new file
2. Write to a file (overwrite)
3. Read from a file
4. Append to a file
5. Back to Main Menu
""")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            name = input("Enter file name: ").strip()
            print(file_operations.create_file(name))
        elif choice == "2":
            name = input("Enter file name: ").strip()
            content = input("Enter data to write: ")
            print(file_operations.write_file(name, content))
        elif choice == "3":
            name = input("Enter file name: ").strip()
            try:
                print("\nFile Content:\n" + file_operations.read_file(name))
            except (OSError, FileNotFoundError) as exc:
                print("Could not read file:", exc)
        elif choice == "4":
            name = input("Enter file name: ").strip()
            content = input("Enter data to append: ")
            print(file_operations.append_file(name, content))
        elif choice == "5":
            return
        else:
            print("Invalid choice.")
        pause()


def explore_module():
    modules = {
        "math": math,
        "datetime": __import__("datetime"),
        "time": time,
        "random": random,
        "uuid": uuid,
        "file_operations": file_operations,
        "math_utils": math_utils,
    }
    print("Available modules:", ", ".join(modules))
    name = input("Enter module name to explore: ").strip()
    if name in modules:
        print(f"Available attributes in {name} module:")
        print(dir(modules[name]))
    else:
        print("Module not found in the toolkit's supported list.")


def main():
    while True:
        print("""
==============================
Welcome to Multi-Utility Toolkit
==============================
Choose an option:
1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations (Custom Module)
6. Explore Module Attributes (dir())
7. Exit
==============================""")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            datetime_menu()
        elif choice == "2":
            math_menu()
        elif choice == "3":
            random_menu()
        elif choice == "4":
            print("Generated UUID:", uuid.uuid4())
            pause()
        elif choice == "5":
            file_menu()
        elif choice == "6":
            explore_module()
            pause()
        elif choice == "7":
            print("Thank you for using the Multi-Utility Toolkit!")
            break
        else:
            print("Invalid choice. Please select 1-7.")


if __name__ == "__main__":
    main()
