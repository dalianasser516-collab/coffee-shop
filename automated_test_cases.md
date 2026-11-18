# Coffee Shop – Automated Test Cases

---

## 1. Project Overview

| Field | Details |
|-------|---------|
| Application | Coffee Shop |
| Testing Type | Automated Testing |
| Programming Language | Python |
| Automation Framework | pytest |
| Test File | `tests/test_coffee_shop.py` |
| Execution Command | `pytest tests/test_coffee_shop.py -v` |

---

## 2. Automated Test Cases

### A. Menu Testing

| Test Case ID | Test Scenario | Test Function | Test Data | Expected Result | Actual Result | Status |
|--------------|---------------|---------------|-----------|-----------------|---------------|--------|
| AT-01 | Verify displaying a coffee shop menu | `test_show_menu` | `["mocha", "matcha"]` | The function returns the correct menu | `["mocha", "matcha"]` | Pass |
| AT-02 | Verify displaying an empty menu | `test_show_menu_empty` | Empty list | The function returns an empty list | `[]` | Pass |

### B. Branch Data Testing

| Test Case ID | Test Scenario | Test Function | Test Data | Expected Result | Actual Result | Status |
|--------------|---------------|---------------|-----------|-----------------|---------------|--------|
| AT-03 | Verify Branch 1 minimum charge | `test_branch1_minimum_charge` | Branch 1 | Minimum charge is 500 | 500 | Pass |
| AT-04 | Verify Branch 2 minimum charge | `test_branch2_minimum_charge` | Branch 2 | Minimum charge is 700 | 700 | Pass |
| AT-05 | Verify Branch 1 rating | `test_branch1_rating` | Branch 1 | Rating is 10 | 10 | Pass |
| AT-06 | Verify Branch 2 rating | `test_branch2_rating` | Branch 2 | Rating is 8.6 | 8.6 | Pass |
| AT-07 | Verify Branch 1 menu items | `test_branch1_menu` | Branch 1 | The menu contains the expected products | `['iced spanish latte', 'matcha', 'mocha', 'cakes', 'cheese cakes']` | Pass |
| AT-08 | Verify Branch 2 menu items | `test_branch2_menu` | Branch 2 | The menu contains the expected products | `['iced spanish latte', 'matcha', 'salted caramel', 'cakes', 'fresh juices']` | Pass |

### C. Object Representation and Comparison Testing

| Test Case ID | Test Scenario | Test Function | Test Data | Expected Result | Actual Result | Status |
|--------------|---------------|---------------|-----------|-----------------|---------------|--------|
| AT-09 | Verify Branch 1 string representation | `test_branch1_str` | Branch 1 object | Returns the expected string representation | Expected string returned | Pass |
| AT-10 | Verify Branch 2 string representation | `test_branch2_str` | Branch 2 object | Returns the expected string representation | Expected string returned | Pass |
| AT-11 | Verify Branch 1 and Branch 2 are not equal | `test_branch1_eq_branch2` | Branch 1, Branch 2 | Comparison returns False | False | Pass |
| AT-12 | Verify Branch 1 rating is not lower than Branch 2 | `test_branch1_lt_branch2` | Branch 1, Branch 2 | Comparison returns False | False | Pass |
| AT-13 | Verify Branch 2 rating is lower than Branch 1 | `test_branch2_lt_branch1` | Branch 2, Branch 1 | Comparison returns True | True | Pass |

### D. Rating Validation Testing

| Test Case ID | Test Scenario | Test Function | Test Data | Expected Result | Actual Result | Status |
|--------------|---------------|---------------|-----------|-----------------|---------------|--------|
| AT-14 | Verify a place with a rating of 9.5 is considered good | `test_is_good_place_true` | Rating = 9.5 | Returns True | True | Pass |
| AT-15 | Verify a place with a rating of 8.0 is not considered good | `test_is_good_place_false` | Rating = 8.0 | Returns False | False | Pass |

### E. Special Offers Testing

| Test Case ID | Test Scenario | Test Function | Test Data | Expected Result | Actual Result | Status |
|--------------|---------------|---------------|-----------|-----------------|---------------|--------|
| AT-16 | Verify creating a special offer object | `test_special_offers` | Special offer method | Returns an object with the expected menu, minimum charge of 400, and rating of 9.8 | Menu `['two iced spanish latte', 'two cheese cakes']`, minimum charge 400, rating 9.8 | Pass |

### F. Payment Function Testing

| Test Case ID | Test Scenario | Test Function | Test Data | Expected Result | Actual Result | Status |
|--------------|---------------|---------------|-----------|-----------------|---------------|--------|
| AT-17 | Verify sufficient payment | `test_is_payment_sufficient_true` | Payment = 600, Price = 500 | Returns True | True | Pass |
| AT-18 | Verify insufficient payment | `test_is_payment_sufficient_false` | Payment = 400, Price = 500 | Returns False | False | Pass |

---

## 3. Test Execution Summary

| Metric | Result |
|--------|--------|
| Total Automated Test Cases | 18 |
| Passed | 18 |
| Failed | 0 |
| Execution Status | All Tests Passed |

---

## 4. Notes

- Automated test cases were implemented using pytest.
- Assertions were used to compare actual results with expected results.
- The tests cover menu functionality, branch data, object methods, ratings, special offers, and payment validation.
- User input scenarios are documented separately in `test_cases.md`.
- All 18 automated tests passed during the recorded execution.
- The automated tests cover the `Coffee_shop` class and helper functions. They do not cover the `main()` flow, so BUG-001, BUG-002, and BUG-003 are covered only by the manual test cases.