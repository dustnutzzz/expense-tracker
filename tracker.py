# Expense Tracker Installment 2, Author: Dustin Z. Lacandazo, A simple console-based landing page for a personal expense tracker.

print("=" * 40)
print(f"\t\tEXPENSE TRACKER")
print(f"\tKnow where your money goes.")
print("=" * 40)

print(f"\nMAIN MENU")
print(f"  [1] Add an expense" + "\t\t(coming soon)")
print(f"  [2] View all expenses" + "\t\t(coming soon)")
print(f"  [3] Show total spent" + "\t\t(coming soon)")
print(f"  [4] Exit" + "\t\t\t(coming soon)\n")

name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.\n")

item1 = input("First expense? ")
amount1 = float(input("Amount? "))
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
total = amount1 + amount2
average = total / 2

print(f"\n{ '-' * 40}")
print("SUMMARY")
print(f"  - {item1}: \t${amount1:}")
print(f"  - {item2}: \t${amount2:}")
print(f"Total spent: \t${total}")
print(f"Average: \t${average}")
print("-" * 40)

print("Made by: Dustin Z. Lacandazo | Installment 2")
