from Main import *

# Setup: Delete existing data files for a clean slate
if os.path.exists("accounts.pkl"):
    os.remove("accounts.pkl")
if os.path.exists("orders.pkl"):
    os.remove("orders.pkl")

# Create root Tkinter window
root = tk.Tk()
app = AccountAndTicketApp(root)

# Test 1: Load Data
print("--- Test 1: Load Data ---")
print("Accounts loaded:", app.accounts)
print("Orders loaded:", app.orders)

# Test 2: Create Account
print("\n--- Test 2: Create Account ---")
app.new_username_entry = type("MockEntry", (), {"get": lambda: "testuser"})
app.new_password_entry = type("MockEntry", (), {"get": lambda: "password123"})
app.role_var = type("MockVar", (), {"get": lambda: "Customer"})
app.create_account()
print("Accounts after account creation:", app.accounts)

# Test 3: Duplicate Account Creation
print("\n--- Test 3: Duplicate Account Creation ---")
app.create_account()  # Attempt to create the same account again
print("Accounts after attempting duplicate account creation:", app.accounts)

# Test 4: Login with Correct Credentials
print("\n--- Test 4: Login with Correct Credentials ---")
app.username_entry = type("MockEntry", (), {"get": lambda: "testuser"})
app.password_entry = type("MockEntry", (), {"get": lambda: "password123"})
app.login()
print("Current user after login:", app.current_user)
print("Current role after login:", app.current_role)

# Test 5: Login with Incorrect Credentials
print("\n--- Test 5: Login with Incorrect Credentials ---")
app.username_entry = type("MockEntry", (), {"get": lambda: "wronguser"})
app.password_entry = type("MockEntry", (), {"get": lambda: "wrongpass"})
app.login()
print("Current user after failed login:", app.current_user)

# Test 6: Display Dashboard
print("\n--- Test 6: Display Dashboard ---")
app.show_dashboard()
print("Dashboard displayed successfully.")

# Test 7: Buy Tickets
print("\n--- Test 7: Buy Tickets ---")
app.buy_tickets()
app.selected_ticket = app.tickets[0]  # Mocking ticket selection
app.quantity_spinbox = type("MockSpinbox", (), {"get": lambda: "2"})  # Mock quantity
app.show_payment_page()
print("Selected ticket:", app.selected_ticket)
print("Selected quantity:", app.selected_quantity)
print("Total price:", app.total_price)

# Test 8: Confirm Purchase
print("\n--- Test 8: Confirm Purchase ---")
app.card_number_entry = type("MockEntry", (), {"get": lambda: "1234567890123456"})
app.card_name_entry = type("MockEntry", (), {"get": lambda: "John Doe"})
app.cvv_entry = type("MockEntry", (), {"get": lambda: "123"})
app.confirm_purchase()
print("Orders after purchase:", app.orders)

# Test 9: View My Orders
print("\n--- Test 9: View My Orders ---")
app.view_my_orders()
print("My orders displayed successfully.")

# Test 10: Admin Role - Manage Customers
print("\n--- Test 10: Admin Role - Manage Customers ---")
# Create an admin account for testing
app.new_username_entry = type("MockEntry", (), {"get": lambda: "adminuser"})
app.new_password_entry = type("MockEntry", (), {"get": lambda: "adminpass"})
app.role_var = type("MockVar", (), {"get": lambda: "Admin"})
app.create_account()

# Log in as admin
app.username_entry = type("MockEntry", (), {"get": lambda: "adminuser"})
app.password_entry = type("MockEntry", (), {"get": lambda: "adminpass"})
app.login()

app.manage_customers()
print("Customers managed successfully.")

# Test 11: Admin Role - View Sold Tickets
print("\n--- Test 11: Admin Role - View Sold Tickets ---")
app.view_sold_tickets()
print("Sold tickets displayed successfully.")

# Test 12: Data Persistence
print("\n--- Test 12: Data Persistence ---")
# Restart app and reload data
new_app = AccountAndTicketApp(root)
print("Accounts after restart:", new_app.accounts)
print("Orders after restart:", new_app.orders)