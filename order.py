# Order Object Definition

# The "Order" object contains:
# - Order ID (a unique identifier that is able to be recalled for actions to this object)
# - Description of item ordered (this is what is shown on the bulletin board for readability and simplicity reasons)
# - Name of person who ordered the item
# - Shipping address
# - Goal ship date
# - Status
# - Notes (nullable)

# Possible Order statuses:
# - Conversation
# - Ordered
# - Model Made
# - Sliced
# - Printed
# - Done and Ready to Ship

# Rules for the Order ID:
# - All IDs must be a unique combination of sets of characters (codes) separated by underscores
# - The first code is the actual shop listing being ordered (ie if it's a stomp pad, the code is "sp")
# -- Refer to the README for all of the object codes
# - The second code is a numeric value corresponding to the current counter of orders for that shop listing (ie if you have sold 22 stomp pads so far, the next stomp pad you sell will get the ID sp_23)

class Order:
  def __init__(self, oid, desc, name, address, date, status, notes):
    self.oid = oid
    self.desc = desc
    self.name = name
    self.address = address
    self.date = date
    self.status = "ordered"
    self.notes = notes

def __str__(self):
    return Format.underline + "New order summary:\n" + Format.end + "Order ID: " + self.oid + "\n" + "Order Description: " + self.desc + "\n" + "Name of buyer: " + self.name + "\n" + "Shipping Address: " + self.address + "\n" + "Ship date: " + self.date + "\n" + "Order Status: " + self.status + "\n" + "Notes: " + self.notes

class Format:
    end = '\033[0m'
    underline = '\033[4m'