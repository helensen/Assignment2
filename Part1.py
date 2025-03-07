food_charge = float(input("Enter the charge for the food: $"))


tip = food_charge * 0.18
tax = food_charge * 0.07

total = food_charge + tip + tax
print(f"\nFood Charge: ${food_charge:.2f}")
print(f"Tip (18%): ${tip:.2f}")
print(f"Sales Tax (7%): ${tax:.2f}")
print(f"Total Amount: ${total:.2f}")
