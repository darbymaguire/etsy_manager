# Main driver file for Etsy Order Manager

# Purpose: A basic application to keep track of Etsy shop orders, like an electronic bulletin board.
# There are statuses:
# - Ordered
# - Model Made
# - Sliced
# - Printed
# - Done and Ready to Ship

# Orders automatically start in the "Ordered" status.

# There are actions:
# - View
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

if (action == "Help"):
    print("Available actions are: \n- View (\"vw\")\n- Add (\"add\")\n- Move (\"mv\")\n- Cancel (\"cx\")\n- Exit (\"exit\")")
    print("Please enter the appropriate command for your desired action.")