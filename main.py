# Main driver file for Etsy Order Manager

# Purpose: A basic application to keep track of Etsy shop orders, like an electronic bulletin board.
# There are statuses:
# - Conversation
# - Ordered
# - Model Made
# - Sliced
# - Printed
# - Done and Ready to Ship

# Orders automatically start in the "Ordered" status, the "Conversation" status must be manually assigned.
# The conversation status is for active conversations with Etsy users who have not yet placed an order.

# There are actions:
# - Add
# - Move
# - Cancel
# - Exit

# There is an "Order" object that contains:
# - Order ID (a unique identifier that is able to be recalled for actions to this object)
# - Description of item ordered (this is what is shown on the bulletin board for readability and simplicity reasons)
# - Name of person who ordered the item
# - Shipping address
# - Goal ship date
# - Status
# - Notes (nullable)

print("Welcome to Summit3DP Etsy Shop Manager")
print("What actions would you like to take? Enter 'Help' for options")

action = input()
print("You chose: " + action)