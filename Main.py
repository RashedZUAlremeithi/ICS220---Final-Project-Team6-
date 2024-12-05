import tkinter as tk
from tkinter import ttk, messagebox
import pickle
import os
from datetime import datetime
from enum import Enum

# Define TicketType Enum
class TicketType(Enum):
    SINGLE_DAY = "Single-Day Pass"
    TWO_DAY = "Two-Day Pass"
    ANNUAL = "Annual Membership"
    CHILD = "Child Ticket"
    GROUP = "Group Discount"
    VIP = "VIP Experience Pass"

#PaymentType Enum
class PaymentType(Enum):
    CREDIT_CARD = "Credit Card"
    DEBIT_CARD = "Debit Card"
    CASH_ON_ARRIVAL = "Cash on Arrival"

#This function allows customer to view all types available
def display_all_ticket_types():
    """Displays all available ticket types."""
    print("Available Ticket Types:")
    for ticket_type in TicketType:
        print(ticket_type.name + ": " + ticket_type.value)

# Define Ticket Class
class Ticket:
    def __init__(self, ticket_type, description, price, validity, discount, limitations, visit_date):
        self.ticket_type = ticket_type  # Should be a TicketType Enum
        self.description = description
        self.price = price
        self.validity = validity
        self.discount = discount
        self.limitations = limitations
        self.visit_date = visit_date


    # Getter and setter for ticket_type
    def get_ticket_type(self):
        return self.ticket_type

    def set_ticket_type(self, ticket_type):
        self.ticket_type = ticket_type

    # Getter and setter for description
    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    # Getter and setter for price
    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    # Getter and setter for validity
    def get_validity(self):
        return self.validity

    def set_validity(self, validity):
        self.validity = validity

    # Getter and setter for discount
    def get_discount(self):
        return self.discount

    def set_discount(self, discount):
        self.discount = discount

    # Getter and setter for limitations
    def get_limitations(self):
        return self.limitations

    def set_limitations(self, limitations):
        self.limitations = limitations

    # Getter and setter for visit_date
    def get_visit_date(self):
        return self.visit_date

    def set_visit_date(self, visit_date):
        self.visit_date = visit_date

    #String Function for ticket


    def apply_discount(self):
        """Applies a discount based on the ticket type and updates the price."""
        base_price = 100  # Base price for Single-Day Pass

        # Apply discount based on ticket type
        if self.ticket_type == TicketType.TWO_DAY:
            self.price = base_price * 0.90  # 10% discount for Two-Day Pass
        elif self.ticket_type == TicketType.ANNUAL:
            self.price = base_price * 0.70  # 30% discount for Annual Membership
        elif self.ticket_type == TicketType.CHILD:
            self.price = base_price * 0.75  # 25% discount for Child Ticket
        elif self.ticket_type == TicketType.GROUP:
            # Assuming the group discount is for 5 or more people
            group_size = 5  # Example group size
            if group_size >= 5:
                self.price = base_price * 0.60  # 40% discount for groups of 5 or more
            else:
                self.price = base_price  # No discount for smaller groups
        elif self.ticket_type == TicketType.VIP:
            self.price = base_price * 2.00  # 200% price for VIP Experience (Double the price)
        else:
            self.price = base_price  # No discount for other types



# Define Customer Class
class Customer:
    def __init__(self, name, email, username, password):
        self.name = name
        self.email = email
        self.username = username
        self.password = password
        self.purchase_history = []

    # Getter and setter for name
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    # Getter and setter for email
    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    # Getter and setter for username
    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    # Getter and setter for password
    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    # Getter and setter for purchase_history
    def get_purchase_history(self):
        return self.purchase_history

    def set_purchase_history(self, purchase_history):
        self.purchase_history = purchase_history

    # Function that creates account for customer
    def create_account(self, name, email, username, password):
        new_customer = Customer(name, email, username, password)
        return new_customer

    #Function that displays all the order/purchase history for the customer
    def display_order_history(self):
        """Prints the order history for the customer."""
        for order in self.purchase_history:
            print(order)


#Define order class
class Order:
    def __init__(self, customer, ticket, quantity, amount_paid, payment_type):
        self.customer = customer  # Customer placing the order
        self.ticket = ticket  # Ticket being purchased
        self.quantity = quantity  # How many tickets they want
        self.total_price = ticket.price * quantity  # Total price for the order
        self.amount_paid = amount_paid  # Amount paid for the order
        self.payment_type = payment_type
        self.order_date = datetime.now()

    # Getter and setter for customer
    def get_customer(self):
        return self.customer

    def set_customer(self, customer):
        self.customer = customer

    # Getter and setter for ticket
    def get_ticket(self):
        return self.ticket

    def set_ticket(self, ticket):
        self.ticket = ticket

    # Getter and setter for quantity
    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity

    # Getter and setter for total_price
    def get_total_price(self):
        return self.total_price

    def set_total_price(self, total_price):
        self.total_price = total_price

    # Getter and setter for amount_paid
    def get_amount_paid(self):
        return self.amount_paid

    def set_amount_paid(self, amount_paid):
        self.amount_paid = amount_paid

    # Getter and setter for payment_type
    def get_payment_type(self):
        return self.payment_type

    def set_payment_type(self, payment_type):
        self.payment_type = payment_type

    # Getter and setter for order_date
    def get_order_date(self):
        return self.order_date

    def set_order_date(self, order_date):
        self.order_date = order_date

# Define Admin Class
class Admin:
    def __init__(self):
        self.ticket_sales = {}  # Track sales for each TicketType

# Define Park Class
class Park:
    def __init__(self, name, location, operating_hours):
        self.name = name
        self.location = location
        self.operating_hours = operating_hours  # Dictionary, e.g., {"Monday": "9 AM - 9 PM"}
        self.current_visitors = 0
        self.attractions = []  # List of attraction names
        self.events = []  # List of event names
        self.services = []  # List of park services


    # Getter and setter for name
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    # Getter and setter for location
    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    # Getter and setter for operating_hours
    def get_operating_hours(self):
        return self.operating_hours

    def set_operating_hours(self, operating_hours):
        self.operating_hours = operating_hours

    # Getter and setter for current_visitors
    def get_current_visitors(self):
        return self.current_visitors

    def set_current_visitors(self, current_visitors):
        self.current_visitors = current_visitors

    # Getter and setter for attractions
    def get_attractions(self):
        return self.attractions

    def set_attractions(self, attractions):
        self.attractions = attractions

    # Getter and setter for events
    def get_events(self):
        return self.events

    def set_events(self, events):
        self.events = events

    # Getter and setter for services
    def get_services(self):
        return self.services

    def set_services(self, services):
        self.services = services

    # Function that adds an attraction to the attraction list in the park
    def add_attraction(self, attraction_name):
        """Adds a new attraction to the park."""
        self.attractions.append(attraction_name)

    # Function that removes an attraction from the attraction list in the park
    def remove_attraction(self, attraction_name):
        """Removes an attraction from the park."""
        if attraction_name in self.attractions:
            self.attractions.remove(attraction_name)

    # Function that adds an event to the event list in the park
    def add_event(self, event_name):
        """Adds a new event to the park."""
        self.events.append(event_name)

    # Function that removes an event from the event list in the park
    def remove_event(self, event_name):
        """Removes an event from the park."""
        if event_name in self.events:
            self.events.remove(event_name)

    # Function that adds a service to the services list in the park
    def add_service(self, service_name):
        """Adds a new service to the park."""
        self.services.append(service_name)

    # Function that removes a service from the services list in the park
    def remove_service(self, service_name):
        """Removes a service from the park."""
        if service_name in self.services:
            self.services.remove(service_name)

    # Functions below allow the customer to see the park's attractions, events, and services
    def list_attractions(self):
        """Returns a list of all park attractions."""
        return self.attractions

    def list_events(self):
        """Returns a list of all park events."""
        return self.events

    def list_services(self):
        """Returns a list of all park services."""
        return self.services


class AccountAndTicketApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Account and Ticket Management System")
        self.current_user = None
        self.current_role = None

        # Initialize storage
        self.accounts_file = "accounts.pkl"
        self.orders_file = "orders.pkl"
        self.accounts = self.load_data(self.accounts_file)
        self.orders = self.load_data(self.orders_file)

        # Ticket Data
        self.tickets = [
            {"type": "Single-Day Pass", "price": 50.0, "validity": "1 Day", "features": "Access to all rides"},
            {"type": "Multi-Day Pass", "price": 120.0, "validity": "3 Days", "features": "Access to all rides"},
            {"type": "Group Pass", "price": 200.0, "validity": "1 Day", "features": "Access for up to 5 people"},
        ]

        # Login Page
        self.show_login_page()

    def load_data(self, file_path):
        """Loads data from a pickle file."""
        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                return pickle.load(f)
        return {}

    def save_data(self, file_path, data):
        """Saves data to a pickle file."""
        with open(file_path, "wb") as f:
            pickle.dump(data, f)

    def show_login_page(self):
        """Displays the login page."""
        self.clear_frame()

        tk.Label(self.root, text="Login", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="Username:").pack(pady=5)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)

        tk.Label(self.root, text="Password:").pack(pady=5)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self.root, text="Login", command=self.login).pack(pady=10)
        tk.Button(self.root, text="Create Account", command=self.show_create_account_page).pack(pady=5)

    def show_create_account_page(self):
        """Displays the account creation page."""
        self.clear_frame()

        tk.Label(self.root, text="Create Account", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="Username:").pack(pady=5)
        self.new_username_entry = tk.Entry(self.root)
        self.new_username_entry.pack(pady=5)

        tk.Label(self.root, text="Password:").pack(pady=5)
        self.new_password_entry = tk.Entry(self.root, show="*")
        self.new_password_entry.pack(pady=5)

        tk.Label(self.root, text="Role:").pack(pady=5)
        self.role_var = tk.StringVar(value="Customer")
        tk.OptionMenu(self.root, self.role_var, "Admin", "Customer").pack(pady=5)

        tk.Button(self.root, text="Submit", command=self.create_account).pack(pady=10)
        tk.Button(self.root, text="Back to Login", command=self.show_login_page).pack(pady=5)

    def create_account(self):
        """Handles account creation."""
        username = self.new_username_entry.get()
        password = self.new_password_entry.get()
        role = self.role_var.get()

        if not username or not password:
            messagebox.showerror("Error", "Both fields are required!")
            return

        if username in self.accounts:
            messagebox.showerror("Error", "Username already exists!")
        else:
            self.accounts[username] = {"password": password, "role": role}
            self.save_data(self.accounts_file, self.accounts)
            messagebox.showinfo("Success", "Account created successfully!")
            self.show_login_page()

    def login(self):
        """Handles user login."""
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in self.accounts and self.accounts[username]["password"] == password:
            self.current_user = username
            self.current_role = self.accounts[username]["role"]
            messagebox.showinfo("Login Successful", f"Welcome, {username}! Role: {self.current_role}")
            self.show_dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def show_dashboard(self):
        """Displays the dashboard based on the user's role."""
        self.clear_frame()

        tk.Label(self.root, text=f"Welcome, {self.current_user}", font=("Arial", 16)).pack(pady=10)

        if self.current_role == "Admin":
            tk.Button(self.root, text="Manage Customers", command=self.manage_customers).pack(pady=5)
            tk.Button(self.root, text="View Sold Tickets", command=self.view_sold_tickets).pack(pady=5)
        elif self.current_role == "Customer":
            tk.Button(self.root, text="Buy Tickets", command=self.buy_tickets).pack(pady=5)
            tk.Button(self.root, text="My Orders", command=self.view_my_orders).pack(pady=5)

        tk.Button(self.root, text="Logout", command=self.show_login_page).pack(pady=5)

    def buy_tickets(self):
        """Displays the ticket purchasing page."""
        self.clear_frame()

        tk.Label(self.root, text="Buy Tickets", font=("Arial", 16)).pack(pady=10)
        self.ticket_table = ttk.Treeview(self.root, columns=("Type", "Price", "Validity", "Features"), show="headings")
        self.ticket_table.heading("Type", text="Type")
        self.ticket_table.heading("Price", text="Price ($)")
        self.ticket_table.heading("Validity", text="Validity")
        self.ticket_table.heading("Features", text="Features")
        self.ticket_table.pack(padx=10, pady=10)

        for ticket in self.tickets:
            self.ticket_table.insert("", "end", values=(ticket["type"], ticket["price"], ticket["validity"], ticket["features"]))

        tk.Label(self.root, text="Select Quantity:").pack(pady=5)
        self.quantity_spinbox = tk.Spinbox(self.root, from_=1, to=10, width=5)
        self.quantity_spinbox.pack(pady=5)

        tk.Button(self.root, text="Proceed to Payment", command=self.show_payment_page).pack(pady=10)

    def show_payment_page(self):
        """Displays the payment page."""
        selected_item = self.ticket_table.focus()
        if not selected_item:
            messagebox.showerror("Error", "Please select a ticket.")
            return

        selected_ticket = self.ticket_table.item(selected_item)["values"]
        if not selected_ticket:
            messagebox.showerror("Error", "Invalid ticket selection.")
            return

        self.selected_ticket = selected_ticket
        self.selected_quantity = int(self.quantity_spinbox.get())
        self.total_price = self.selected_quantity * float(self.selected_ticket[1])

        self.clear_frame()

        tk.Label(self.root, text="Payment Page", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text=f"Ticket: {self.selected_ticket[0]}").pack(pady=5)
        tk.Label(self.root, text=f"Quantity: {self.selected_quantity}").pack(pady=5)
        tk.Label(self.root, text=f"Total Price: ${self.total_price:.2f}").pack(pady=5)

        tk.Label(self.root, text="Enter Payment Details").pack(pady=10)
        tk.Label(self.root, text="Card Number:").pack(pady=5)
        self.card_number_entry = tk.Entry(self.root)
        self.card_number_entry.pack(pady=5)

        tk.Label(self.root, text="Cardholder Name:").pack(pady=5)
        self.card_name_entry = tk.Entry(self.root)
        self.card_name_entry.pack(pady=5)

        tk.Label(self.root, text="CVV:").pack(pady=5)
        self.cvv_entry = tk.Entry(self.root, show="*")
        self.cvv_entry.pack(pady=5)

        tk.Button(self.root, text="Confirm Purchase", command=self.confirm_purchase).pack(pady=10)

    def confirm_purchase(self):
        """Confirms ticket purchase."""
        card_number = self.card_number_entry.get()
        card_name = self.card_name_entry.get()
        cvv = self.cvv_entry.get()

        if not card_number or not card_name or not cvv:
            messagebox.showerror("Error", "Please complete all fields.")
            return

        order_id = f"ORDER-{len(self.orders) + 1}"
        self.orders[order_id] = {
            "customer": self.current_user,
            "ticket": self.selected_ticket[0],
            "quantity": self.selected_quantity,
            "total_price": self.total_price,
        }
        self.save_data(self.orders_file, self.orders)

        messagebox.showinfo("Success", f"Purchase Confirmed!\nOrder ID: {order_id}")
        self.show_dashboard()

    def view_my_orders(self):
        """Displays the current user's orders."""
        self.clear_frame()

        tk.Label(self.root, text="My Orders", font=("Arial", 16)).pack(pady=10)
        self.orders_table = ttk.Treeview(self.root, columns=("Order ID", "Ticket", "Quantity", "Total Price"),
                                         show="headings")
        self.orders_table.heading("Order ID", text="Order ID")
        self.orders_table.heading("Ticket", text="Ticket")
        self.orders_table.heading("Quantity", text="Quantity")
        self.orders_table.heading("Total Price", text="Total Price ($)")
        self.orders_table.pack(padx=10, pady=10)

        # Ensure self.orders is a dictionary and contains the necessary data
        if not isinstance(self.orders, dict):
            self.orders = {}

        # Populate the orders table
        for order_id, order_data in self.orders.items():
            if order_data.get("customer") == self.current_user:
                self.orders_table.insert("", "end", values=(
                    order_id,
                    order_data.get("ticket", "Unknown"),
                    order_data.get("quantity", 0),
                    f"${order_data.get('total_price', 0):.2f}"
                ))

        tk.Button(self.root, text="Back to Dashboard", command=self.show_dashboard).pack(pady=10)

    def view_sold_tickets(self):
        """Allows admins to view all sold tickets."""
        self.clear_frame()

        tk.Label(self.root, text="Sold Tickets", font=("Arial", 16)).pack(pady=10)
        self.orders_table = ttk.Treeview(self.root, columns=("Order ID", "Customer", "Ticket", "Quantity", "Total Price"), show="headings")
        self.orders_table.heading("Order ID", text="Order ID")
        self.orders_table.heading("Customer", text="Customer")
        self.orders_table.heading("Ticket", text="Ticket")
        self.orders_table.heading("Quantity", text="Quantity")
        self.orders_table.heading("Total Price", text="Total Price ($)")
        self.orders_table.pack(padx=10, pady=10)

        for order_id, order_data in self.orders.items():
            self.orders_table.insert("", "end", values=(order_id, order_data["customer"], order_data["ticket"], order_data["quantity"], order_data["total_price"]))

        tk.Button(self.root, text="Back to Dashboard", command=self.show_dashboard).pack(pady=10)

    def manage_customers(self):
        """Allows admins to manage customers."""
        self.clear_frame()

        tk.Label(self.root, text="Manage Customers", font=("Arial", 16)).pack(pady=10)
        self.customer_table = ttk.Treeview(self.root, columns=("Username", "Role"), show="headings")
        self.customer_table.heading("Username", text="Username")
        self.customer_table.heading("Role", text="Role")
        self.customer_table.pack(padx=10, pady=10)

        for username, data in self.accounts.items():
            self.customer_table.insert("", "end", values=(username, data["role"]))

        tk.Button(self.root, text="Back to Dashboard", command=self.show_dashboard).pack(pady=10)

    def clear_frame(self):
        """Clears all widgets from the current frame."""
        for widget in self.root.winfo_children():
            widget.destroy()


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = AccountAndTicketApp(root)
    root.mainloop()

