Bug Reports - Coffee Shop

BUG-001: Menu validation allowed items unavailable in the selected branch

Steps to reproduce: Select Branch 1 and enter an item that is only available in Branch 2
Expected: Should reject the item because it is not available in the selected branch
Actual: The item was accepted because the validation checked the general items list instead of the selected branch menu
Severity: Medium

BUG-002: Payment loop repeated after valid payment

Steps to reproduce: Enter a payment amount equal to or greater than the item price
Expected: Payment should be accepted and the order should be confirmed
Actual: The payment loop continued even after entering a sufficient payment
Severity: Medium