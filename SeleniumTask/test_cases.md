# Automated Test Cases - Saucedemo

## 1. Login Functionality

### 1.1 Positive Test Cases

| ID   | Test Name  | Description                                 | Steps                                                                                            | Expected Result                                             |
| ---- | ---------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------ | ----------------------------------------------------------- |
| TC01 | test_login | Verify successful login for different users | 1. Open login page <br> 2. Enter valid username <br> 3. Enter valid password <br> 4. Click Login | User is redirected to Inventory Page with title "Swag Labs" |

### 1.2 Negative Test Cases

| ID   | Test Name               | Description                                     | Steps                                                                    | Expected Result                                                                           |
| ---- | ----------------------- | ----------------------------------------------- | ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| TC02 | test_locked_user        | Verify error message for locked user            | 1. Enter locked_out_user <br> 2. Enter password <br> 3. Click Login      | Error message "Epic sadface: Sorry, this user has been locked out."                       |
| TC03 | test_error_username     | Verify error when username field is empty       | 1. Leave username empty <br> 2. Enter valid password <br> 3. Click Login | Error message "Epic sadface: Username is required"                                        |
| TC04 | test_error_password     | Verify error when password field is empty       | 1. Enter valid username <br> 2. Leave password empty <br> 3. Click Login | Error message "Epic sadface: Password is required"                                        |
| TC05 | test_error_not_matching | Verify error for incorrect username or password | 1. Enter invalid username or password <br> 2. Click Login                | Error message "Epic sadface: Username and password do not match any user in this service" |

---

## 2. Cart Functionality

### 2.1 Inventory Page Verification

| ID   | Test Name                       | Description                    | Steps                                                                                        | Expected Result                                        |
| ---- | ------------------------------- | ------------------------------ | -------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| TC06 | test_inventory_page_elements    | Verify inventory page elements | 1. Open inventory page <br> 2. Check all product buttons <br> 3. Check cart icon and counter | All items visible, cart count = 0                      |
| TC07 | test_add_item_to_cart           | Add one item to cart           | 1. Click "Add to Cart" for one item                                                          | Cart count = 1, "Remove" button visible                |
| TC08 | test_remove_item_from_cart      | Remove one item from cart      | 1. Add item to cart <br> 2. Click "Remove"                                                   | Cart count = 0, "Add" button visible                   |
| TC09 | test_add_all_items_to_cart      | Add all items to cart          | 1. Click "Add to Cart" for all items                                                         | Cart count = total items, all "Remove" buttons visible |
| TC10 | test_remove_all_items_from_cart | Remove all items from cart     | 1. Add all items <br> 2. Remove all items                                                    | Cart count = 0, all "Add" buttons visible              |

### 2.2 Cart Page Verification

| ID   | Test Name                  | Description                 | Steps                              | Expected Result                                                             |
| ---- | -------------------------- | --------------------------- | ---------------------------------- | --------------------------------------------------------------------------- |
| TC11 | test_cart_with_empty_state | View cart with no items     | 1. Open cart page                  | Cart title "Your Cart", labels QTY and Description visible, buttons visible |
| TC12 | test_cart_add_item         | Verify added item in cart   | 1. Add item <br> 2. Open cart      | Cart contains the item with correct name                                    |
| TC13 | test_cart_with_added_items | Verify multiple added items | 1. Add all items <br> 2. Open cart | All items are present in cart                                               |

---

## 3. Checkout Functionality (End-to-End)

| ID   | Test Name                 | Description               | Steps                                                                                       | Expected Result                                                                 |
| ---- | ------------------------- | ------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| TC14 | test_checkout_of_one_item | Checkout for one product  | 1. Add item to cart <br> 2. Proceed to checkout <br> 3. Fill info <br> 4. Complete checkout | Total price correct, order completion message, cart empty after completion      |
| TC15 | test_checkout_all_items   | Checkout for all products | 1. Add all items <br> 2. Proceed to checkout <br> 3. Fill info <br> 4. Complete checkout    | Total price correct, all items present in checkout, cart empty after completion |
