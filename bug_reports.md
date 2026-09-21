# Bug Reports - Coffee Shop

---

## BUG-001: Menu validation allowed items unavailable in the selected branch

**Severity:** Medium

**Steps to reproduce:**
1. Select Branch 1
2. Enter an item that is only available in Branch 2

**Expected Result:**
Should reject the item because it is not available in the selected branch

**Actual Result:**
The item was accepted because the validation checked the general items list instead of the selected branch menu

---

## BUG-002: Payment loop repeated after valid payment

**Severity:** Medium

**Steps to reproduce:**
1. Enter a payment amount equal to or greater than the item price

**Expected Result:**
Payment should be accepted and the order should be confirmed

**Actual Result:**
The payment loop continued even after entering a sufficient payment

---

## Summary

| Bug ID | Description | Severity | Status |
|--------|-------------|----------|--------|
| BUG-001 | Menu validation allowed items unavailable in selected branch | Medium | Open |
| BUG-002 | Payment loop repeated after valid payment | Medium | Open |
