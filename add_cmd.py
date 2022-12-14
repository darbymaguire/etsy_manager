# Add command ("add")
# Adds a new order to the board
# Status defaults to "ordered"

# After the user enters the "add" command, they will be promopted to create a profile for the order, which entails filling out all fields in the Order object.
import order

print("You have chosen to add a new order to the board. Please fill out the following fields.")

oid = input("Please enter the Order ID for this order: ")
desc = input("Please enter the description for this order. Press enter when done.\n")
name = input("Please enter the name of the person who ordered this: ")
address = input("Please enter the shipping address for this order: ")
date = input("Please enter the goal shipping date for this order: ")
status = "ordered"
notes = input("Please enter any notes for this order below. Press enter when done\n")

newOrder = order.Order(oid, desc, name, address, date, status, notes)

print(order.__str__(newOrder))