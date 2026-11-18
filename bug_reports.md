# Bug Reports – Coffee Shop

---

## BUG-001: Menu validation allowed items unavailable in the selected branch

**Severity:** Medium

**Status:** Fixed

**Steps to reproduce:**
1. Run the application.
2. Select Branch 1.
3. Enter "salted caramel" as the item (available only in Branch 2).

**Expected Result:**
The application should reject the item because it is not available in the selected branch menu.

**Actual Result (before fix):**
The item was accepted because the validation checked the general items list instead of the selected branch menu.

**Fix:**
Updated the validation logic to check the selected branch menu.

**Retest Result:**
The application now displays "Order is not found" when entering an item unavailable in the selected branch.

---

## BUG-002: Payment loop repeated after valid payment

**Severity:** Medium

**Status:** Fixed

**Steps to reproduce:**
1. Run the application.
2. Select Branch 1.
3. Enter "matcha" as the item (price 110).
4. Enter "110" as the payment.

**Expected Result:**
The application should accept the payment, confirm the order, and exit the payment loop.

**Actual Result (before fix):**
The payment loop continued even after entering a sufficient payment amount.

**Fix:**
Updated the payment validation and loop control logic to exit the loop after successful payment.

**Retest Result:**
The application now displays the payment confirmation message and ends after receiving a sufficient payment.

---

## BUG-003: Non-finite payment values are not properly validated

**Severity:** Medium

**Status:** Open

**Steps to reproduce (nan):**
1. Run the application.
2. Select Branch 2.
3. Enter "salted caramel" as the item (price 130).
4. Enter "nan" as the payment.

**Steps to reproduce (inf):**
1. Run the application.
2. Select Branch 2.
3. Enter "salted caramel" as the item (price 130).
4. Enter "inf" as the payment.

**Expected Result:**
The application should reject "nan" and "inf" and display "Please enter a valid number".

**Actual Result:**
- With "nan", the application displays "Sorry, the amount entered is not enough. Please enter at least 130 EGP." instead of rejecting the input.
- With "inf", the application displays "Payment successful, your order has been confirmed" and accepts the order without a real payment amount.

**Root Cause:**
`float()` accepts the text "nan" and "inf" without raising a ValueError. "nan" fails the comparison and is reported as insufficient payment, and "inf" passes the comparison and is accepted as a successful payment.

**Suggested Fix:**
Reject non-finite values before comparing the payment with the price, for example by checking `math.isfinite(value)`.

**Status Note:**
Root cause identified. Fix pending.

---

## Bug Report Summary

| Bug ID | Description | Severity | Status |
|--------|-------------|----------|--------|
| BUG-001 | Menu validation allowed items unavailable in the selected branch | Medium | Fixed |
| BUG-002 | Payment loop repeated after valid payment | Medium | Fixed |
| BUG-003 | Non-finite payment values are not properly validated | Medium | Open |

---

## Notes

- Fixed bugs were retested after updating the application.
- BUG-003 remains open. Root cause identified; fix pending.
- Severity indicates the impact of each issue on application functionality.