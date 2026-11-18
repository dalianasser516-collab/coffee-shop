# Coffee Shop – Manual Test Cases

---

## 1. Project Overview

| Field | Details |
|-------|---------|
| Application | Coffee Shop |
| Testing Type | Manual Functional Testing |
| Test Design Techniques | Equivalence Partitioning, Boundary Value Analysis |
| Test Environment | Python Application – Terminal |
| Test Execution Status | Completed |

---

## 2. Branch Selection Testing

**Requirement:** The user must select either Branch 1 or Branch 2.

| Test Case ID | Test Scenario | Test Data | Expected Result | Actual Result | Status |
|--------------|---------------|-----------|-----------------|---------------|--------|
| BR-01 | Verify selecting Branch 1 | 1 | Branch 1 menu is displayed | Branch 1 menu displayed | Pass |
| BR-02 | Verify selecting Branch 2 | 2 | Branch 2 menu is displayed | Branch 2 menu displayed | Pass |
| BR-03 | Verify rejection of zero | 0 | Display invalid choice message | Invalid choice message displayed | Pass |
| BR-04 | Verify rejection of a number greater than 2 | 3 | Display invalid choice message | Invalid choice message displayed | Pass |
| BR-05 | Verify rejection of negative numbers | -1 | Display invalid choice message | Invalid choice message displayed | Pass |
| BR-06 | Verify rejection of decimal numbers | 1.5, 2.1 | Display invalid choice message | Invalid choice message displayed | Pass |
| BR-07 | Verify rejection of alphabetic input | abc | Display invalid choice message | Invalid choice message displayed | Pass |
| BR-08 | Verify rejection of empty input | Empty input | Display invalid choice message | Invalid choice message displayed | Pass |

**Test Design Technique:** Equivalence Partitioning
- Valid Partition: 1 and 2.
- Invalid Partition: Any input other than 1 or 2.

---

## 3. Order Selection Testing

**Requirement:** The user can select only products available in the selected branch menu. Product names are case-insensitive.

| Test Case ID | Test Scenario | Test Data | Expected Result | Actual Result | Status |
|--------------|---------------|-----------|-----------------|---------------|--------|
| OR-01 | Verify selecting a valid product | mocha | Accept the order and display its price | Product accepted and price displayed | Pass |
| OR-02 | Verify uppercase product input | MOCHA | Accept the order after converting input to lowercase | Product accepted | Pass |
| OR-03 | Verify mixed-case product input | CAKES | Accept the order after converting input to lowercase | Product accepted | Pass |
| OR-04 | Verify selecting a product unavailable in the selected branch | salted caramel in Branch 1 | Reject the order | Order is not found | Pass |
| OR-05 | Verify rejection of a non-existing product | burger | Reject the order | Order is not found in both branches | Pass |
| OR-06 | Verify rejection of product names with spaces between letters | m o c h a | Reject the order | Order is not found | Pass |

**Test Design Technique:** Equivalence Partitioning
- Valid Partition: Products available in the selected branch menu, regardless of letter case.
- Invalid Partition: Products not available in the selected branch menu or product names with incorrect formatting.

---

## 4. Payment Validation Testing

**Requirement:** The payment amount must be equal to or greater than the product price.

| Test Case ID | Test Scenario | Test Data | Expected Result | Actual Result | Status |
|--------------|---------------|-----------|-----------------|---------------|--------|
| PAY-01 | Verify rejection of zero payment | 0 (Branch 1, matcha, price 110) | Reject payment and request another amount | Insufficient amount message displayed | Pass |
| PAY-02 | Verify rejection of negative payment | -130 (Branch 2, salted caramel, price 130) | Reject payment and request another amount | Insufficient amount message displayed | Pass |
| PAY-03 | Verify rejection of alphabetic input | GTHK | Display a valid number error message | Please enter a valid number | Pass |
| PAY-04 | Verify rejection of non-numeric product text as payment | FRESH JUICES | Display a valid number error message | Please enter a valid number | Pass |
| PAY-05 | Verify rejection of "nan" as payment | nan (Branch 1, matcha, price 110) | Display a valid number error message | Insufficient amount message displayed instead of rejecting the input. See BUG-003. | Fail |
| PAY-06 | Verify the payment loop stops after a sufficient payment | 110 (Branch 1, matcha, price 110) | Accept payment, confirm the order, and stop asking | Payment successful, order confirmed, loop ended. See BUG-002. | Pass |

**Test Design Techniques:**
- Equivalence Partitioning
- Boundary Value Analysis
- Negative Testing

### Boundary Value Analysis – Payment Amount

**Selected Product:** Matcha, Price 80 EGP (used for boundary analysis only)

| Test Case ID | Boundary Position | Test Data | Expected Result | Actual Result | Status |
|--------------|-------------------|-----------|-----------------|---------------|--------|
| BVA-01 | Below boundary | 79.99 | Reject payment | Payment rejected | Pass |
| BVA-02 | At boundary | 80.00 | Accept payment | Payment accepted | Pass |
| BVA-03 | Above boundary | 80.99 | Accept payment | Payment accepted | Pass |

---

## 5. Test Execution Summary

| Testing Area | Test Cases | Passed | Failed |
|--------------|-----------|--------|--------|
| Branch Selection | 8 | 8 | 0 |
| Order Selection | 6 | 6 | 0 |
| Payment Validation | 6 | 5 | 1 |
| Boundary Value Analysis | 3 | 3 | 0 |
| **Total Manual Test Cases** | **23** | **22** | **1** |

**Execution Result:** 22 of 23 manual test cases passed. PAY-05 failed due to BUG-003.

---

## 6. Notes

- Manual test cases were executed through the application terminal.
- Equivalence Partitioning was used to identify valid and invalid input groups.
- Boundary Value Analysis was applied to payment validation.
- Automated tests are maintained separately in `tests/test_coffee_shop.py` using pytest.
- The current automated test suite contains 18 tests, all of which passed during execution.
- User input scenarios are currently documented as manual tests and are not included in the 18 automated tests.