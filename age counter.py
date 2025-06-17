def check_age():
    try:
        age_input = input("Enter your age: ")
        age = int(age_input)

        if age < 0:
            raise ValueError("Age cannot be negative.")

        if age % 2 == 0:
            print(f"The age {age} is even.")
        else:
            print(f"The age {age} is odd.")

    except ValueError as e:
        print(f"Invalid input! {e}")

# Run the function
check_age()
