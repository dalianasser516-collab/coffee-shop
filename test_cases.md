Test Cases - Coffee Shop

ID| Description| Input| Expected Result| Actual Result| Status
TC01| Valid branch selection - Branch 1| "1"| Should accept the input and display Branch 1 menu| Branch 1 menu was displayed successfully| ✅ Pass
TC02| Valid branch selection - Branch 2| "2"| Should accept the input and display Branch 2 menu| Branch 2 menu was displayed successfully| ✅ Pass
TC03| Invalid branch selection - negative number| "-1"| Should reject the input and ask the user to choose 1 or 2| Invalid choice message was displayed| ✅ Pass
TC04| Invalid branch selection - zero| "0"| Should reject the input and ask the user to choose 1 or 2| Invalid choice message was displayed| ✅ Pass
TC05| Invalid branch selection - other number| "3"| Should reject the input and ask the user to choose 1 or 2| Invalid choice message was displayed| ✅ Pass
TC06| Invalid branch selection - text| "abc"| Should reject the input and ask the user to choose 1 or 2| Invalid choice message was displayed| ✅ Pass
TC07| Valid menu item selection| "latte"| Should accept the item if it is available in the selected branch and display its price| Item was accepted and its price was displayed| ✅ Pass
TC08| Invalid menu item selection| Item not available in selected branch| Should reject the item and display "order is not found"| "order is not found" was displayed| ✅ Pass
TC09| Uppercase menu item input| "LATTE"| Should accept the item regardless of capitalization| Input was converted to lowercase and the item was accepted| ✅ Pass
TC10| Menu item from another branch| An item available in Branch 1 but not Branch 2| Should reject the item if it is not available in the selected branch| "order is not found" was displayed| ✅ Pass
TC11| Insufficient payment| Payment less than item price| Should reject the payment and ask for a sufficient amount| Insufficient payment message was displayed| ✅ Pass
TC12| Exact payment| Payment equal to item price| Should accept the payment and confirm the order| Payment was accepted and order was confirmed| ✅ Pass
TC13| Payment greater than price| Payment greater than item price| Should accept the payment and confirm the order| Payment was accepted and order was confirmed| ✅ Pass
TC14| Decimal payment| "130.00" for an item costing "130"| Should accept a valid decimal payment| Payment was accepted and order was confirmed| ✅ Pass
TC15| Invalid payment input| "abc"| Should handle invalid input without crashing and ask for a valid number| "please enter a valid number" was displayed and the user could enter another value| ✅ Pass
TC16| Negative payment| "-100"| Should reject the payment as insufficient| Insufficient payment message was displayed| ✅ Pass
TC17| End-to-end valid order flow| Valid branch → valid item → sufficient payment| Should complete the order successfully| Order was confirmed and preparation message was displayed| ✅ Pass