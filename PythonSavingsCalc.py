# Welcome Screen
print("""
===============================
        WELCOME!
===============================

       BUDGET PLANNER

   Manage your money wisely
   Save • Plan • Spend

===============================
""")

# Ask for Monthly Income
while True:
    try:
        Income = float(input("Enter Monthly Income: R"))

        if Income < 0:
            print("Please enter a positive amount.")
            continue

        break

    except ValueError:
        print("Invalid input! Please enter a number.")

# Determine amount
Savings = Income * .25
Rainy = Income * .15
Essentials = Income * .5
Cash = Income * .1

# Give output
print("===============================")
print(f"Savings : R{Savings:.2f}")
print(f"Rainy : R{Rainy:.2f}")
print(f"Essentials : R{Essentials:.2f}")
print(f"Cash : R{Cash:.2f}")
print("===============================")