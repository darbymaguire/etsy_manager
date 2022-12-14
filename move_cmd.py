# Move order from one status to the next

# Usage:
# Enter "mv" command followed by the Order name
# Without arguments, the mv command will move the order up one status (ie from "Model Made" to "Sliced")
# Optionally the user can enter arguments after the mv command:
# - C (order goes to "Conversation" status, this should never really happen though)
# - O (order goes to "ordered" status)
# - MM (order goes to "model made" status)
# - S (order goes to "sliced" status)
# - P (order goes to "printed" status)
# - D (order goes to "done and ready to ship" status)

# Example:
# User enters mv sp_23
# The order with the id "sp_23" moves from it's current status (ordered) to the next status, model made.

# Another Example:
# User enters mv sp_23 S
# The order with the id "sp_23" moves from it's current status (ordered) to the user-specified status, sliced.
#
#

