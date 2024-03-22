# Difficulty: 2.0
# Result: Run-time error
# Tests passed: 0/2
# Error: run-time
# Response: 
def generate_order_report():
  """
  Reads diner orders and generates a report of who ordered each item.

  Stops processing when number of customers for a day is 0.
  """

  while True:
    # Read number of customers for this day
    num_customers = int(input())

    # Exit loop when no more customers (end of input)
    if num_customers == 0:
      break

    # Initialize empty dictionary to store orders: customer -> list of items
    orders = {}
    for _ in range(num_customers):
      # Read customer name and split ordered items
      customer_name = input().strip()
      ordered_items = input().strip().split()

      # Add customer and their ordered items to the dictionary
      orders.setdefault(customer_name, []).extend(ordered_items)

    # Generate report for this day
    print_order_report(orders)
    print()  # Print a blank line after each day's report

def print_order_report(orders):
  """
  Prints a report of who ordered each menu item.

  Args:
      orders: A dictionary mapping customer names to lists of ordered items.
  """

  # Sort menu items alphabetically
  menu_items = sorted(set(item for order in orders.values() for item in order))

  # Print report for each menu item
  for item in menu_items:
    # Get customers who ordered the item
    customers = sorted([customer for customer, items in orders.items() if item in items])
    # Print item name and space-separated list of customers
    print(f"{item}: {' '.join(customers)}")

# Main program
generate_order_report()
