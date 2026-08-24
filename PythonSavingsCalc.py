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

#add a profile section where if there are no text files ending in _profile ask to create a profile and then you can login into your profile and keep track of saving.

# Add a choise where you can choose yearly or monthly income

# Ask for Monthly Income
#
## Create a Monthly Function
#
while True:
    try:
        Income = float(input("Enter Monthly Income: R"))

        if Income < 0:
            print("Please enter a positive amount.")
            continue

        break

    except ValueError:
        print("Invalid input! Please enter a number.")
#
## Create a Yearly Function
#
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

# Show yearly saving 

#Features to add
#╔══════════════════════════════╗
#║       BUDGET PLANNER         ║
#╠══════════════════════════════╣
#║  1. Enter Income             ║
#║  2. View Budget              ║
#║  3. Add Expense              ║
#║  4. View Expenses            ║
#║  5. Savings Goal             ║
#║  6. Reports                  ║
#║  7. Exit                     ║
#╚══════════════════════════════╝
#
#Save Progress