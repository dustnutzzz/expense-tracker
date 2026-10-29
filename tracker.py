# Expense Tracker Installment 4, Author: Dustin Z. Lacandazo, A simple console-based landing page for a personal expense tracker.

print("=" * 40)
print(f"\t\tEXPENSE TRACKER")
print(f"\tKnow where your money goes.")
print("=" * 40)

print(f"\nMAIN MENU")
print(f"  [1] Add an expense\t\t(coming soon)")
print(f"  [2] View all expenses\t\t(coming soon)")
print(f"  [3] Show total spent\t\t(coming soon)")
print(f"  [4] Exit\t\t\t(coming soon)\n")

name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.\n")

subtotal = 0

item1 = input("First expense? ")
amount1 = float(input("Amount? "))
if amount1 > 200:
    print("  Huge expense - are you sure?")
elif amount1 > 100:
    print("  Big expense.")
elif amount1 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")
subtotal += amount1

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
if amount2 > 200:
    print("  Huge expense - are you sure?")
elif amount2 > 100:
    print("  Big expense.")
elif amount2 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")
subtotal += amount2

if amount1 > 100 and amount2 > 100:
    print("  Two big expenses in a row - slow down!")

average = subtotal / 2

tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

tax = subtotal * (tax_percent / 100)
total = subtotal + tax
over_budget = total > budget
left = budget - total

print(f"\n{'-' * 40}")
print("SUMMARY")
print(f"  - {item1}:\t${amount1}")
print(f"  - {item2}:\t${amount2}")
print(f"Subtotal:\t${subtotal}")
print(f"Average:\t${average}")
print(f"Tax ({tax_percent}%):\t${tax}")
print(f"Grand total:\t${total}")

if over_budget:
    print(f"Over budget by ${total - budget}!")
elif total > budget * 0.90:
    print(f"Careful: only ${left} left.")
else:
    print(f"Within budget. ${left} left.")

print("-" * 40)
print("Made by: Dustin Z. Lacandazo | Installment 4")