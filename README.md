# Coffee Shop

A simple Python console application developed to practice Python programming concepts and apply software testing techniques. The program allows users to select a coffee shop branch, view its menu, choose an item, and complete the payment process.

---

## Features

- Select between two coffee shop branches
- Display the menu of the selected branch
- Validate customer orders based on branch availability
- Calculate item prices
- Validate payment amounts
- Handle invalid inputs using exception handling
- Display order confirmation messages

---

## Project Structure
coffee-shop/
├── shop.py
├── tests/
│   └── test_coffee_shop.py
├── manual_test_cases.md
├── automated_test_cases.md
├── bug_reports.md
├── README.md
└── .gitignore

---

## Python Concepts Applied

- Object-Oriented Programming (OOP)
- Classes and Objects
- Instance, Class, and Static Methods
- Dunder Methods
- Conditional Statements and Loops
- Functions
- Exception Handling

---

## Testing

Testing was performed using both manual and automated testing techniques.

### Manual Testing

- Tested branch selection and input validation.
- Tested order selection and menu availability.
- Tested payment validation, including boundary values and invalid inputs.
- Documented test cases and execution results.

**Results:** 23 manual test cases executed, 22 passed, and 1 failed (PAY-05, related to BUG-003).

See [Manual Test Cases](./manual_test_cases.md).

### Automated Testing

Automated tests were implemented using pytest to verify:

- Menu functionality
- Branch attributes and menu data
- String representation
- Equality and comparison methods
- Static and class methods
- Payment validation function

**Results:** 18 automated tests executed, 18 passed, and 0 failed.

To run the automated tests:
pip install pytest
pytest tests/test_coffee_shop.py -v

See [Automated Test Cases](./automated_test_cases.md).

### Bug Reporting

During testing, three bugs were documented:

| Bug ID | Description | Status |
|--------|-------------|--------|
| BUG-001 | Menu validation allowed unavailable items | Fixed |
| BUG-002 | Payment loop repeated after valid payment | Fixed |
| BUG-003 | Non-finite payment values were not properly validated | Open |

BUG-001 and BUG-002 were fixed and retested. BUG-003 remains open, with its root cause identified and a suggested fix documented.

See [Bug Reports](./bug_reports.md).

---

## Future Improvements

- Add more automated tests for user inputs.
- Separate application logic from user interaction.
- Improve the overall application structure.

---

## Tech Stack

- Python
- pytest
- Git
- GitHub
