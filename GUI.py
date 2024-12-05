import tkinter as tk
from tkinter import ttk, messagebox
import pickle
import os
from datetime import datetime


class AccountAndTicketApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Account and Ticket Management System")
        self.current_user = None
        self.current_role = None

        # Initialize storage
        self.accounts_file = "accounts.pkl"
        self.orders_file = "orders.pkl"
        self.sales_file = "sales.pkl"
        self.accounts = self.load_data(self.accounts_file)
        self.orders = self.load_data(self.orders_file)
        self.sales = self.load_data(self.sales_file)

        # Ticket Data
        self.tickets = [
            {"type": "Single-Day Pass", "price": 50.0, "validity": "1 Day", "features": "Access to all rides"},
            {"type": "Multi-Day Pass", "price": 120.0, "validity": "3 Days", "features": "Access to all rides"},
            {"type": "Group Pass", "price": 200.0, "validity": "1 Day", "features": "Access for up to 5 people"},
        ]

        # Discounts
        self.discounts = {"Single-Day Pass": 0, "Multi-Day Pass": 0, "Group Pass": 0}

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

    def clear_frame(self):
        """Clears all widgets from the current frame."""
        for widget in self.root.winfo_children():
            widget.destroy()

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
            tk.Button(self.root, text="Admin Dashboard", command=self.admin_dashboard).pack(pady=5)
        elif self.current_role == "Customer":
            tk.Button(self.root, text="Buy Tickets", command=self.buy_tickets).pack(pady=5)
            tk.Button(self.root, text="My Orders", command=self.view_customer_orders).pack(pady=5)

        tk.Button(self.root, text="Logout", command=self.show_login_page).pack(pady=5)

    def admin_dashboard(self):
        """Displays the admin dashboard."""
        self.clear_frame()

        tk.Label(self.root, text="Admin Dashboard", font=("Arial", 16)).pack(pady=10)

        tk.Button(self.root, text="View Ticket Sales", command=self.view_ticket_sales).pack(pady=5)
        tk.Button(self.root, text="Modify Discounts", command=self.modify_discounts).pack(pady=5)
        tk.Button(self.root, text="Back to Dashboard", command=self.show_dashboard).pack(pady=10)

    def view_ticket_sales(self):
        """Displays ticket sales data."""
        self.clear_frame()

        tk.Label(self.root, text="Ticket Sales", font=("Arial", 16)).pack(pady=10)

        sales_table = ttk.Treeview(self.root, columns=("Date", "Ticket", "Quantity"), show="headings")
        sales_table.heading("Date", text="Date")
        sales_table.heading("Ticket", text="Ticket")
        sales_table.heading("Quantity", text="Quantity")
        sales_table.pack(padx=10, pady=10)

        for date, daily_sales in self.sales.items():
            for ticket, quantity in daily_sales.items():
                sales_table.insert("", "end", values=(date, ticket, quantity))

        tk.Button(self.root, text="Back to Admin Dashboard", command=self.admin_dashboard).pack(pady=10)

    def modify_discounts(self):
        """Allows the admin to modify discounts for tickets."""
        self.clear_frame()

        tk.Label(self.root, text="Modify Discounts", font=("Arial", 16)).pack(pady=10)

        for ticket in self.tickets:
            ticket_type = ticket["type"]
            tk.Label(self.root, text=f"{ticket_type} Discount (%):").pack(pady=5)
            discount_var = tk.StringVar(value=str(self.discounts[ticket_type]))
            discount_entry = tk.Entry(self.root, textvariable=discount_var)
            discount_entry.pack(pady=5)

            def save_discount(t_type=ticket_type, d_var=discount_var):
                try:
                    self.discounts[t_type] = max(0, min(100, float(d_var.get())))
                    messagebox.showinfo("Success", f"Discount updated for {t_type}")
                except ValueError:
                    messagebox.showerror("Error", "Invalid discount value!")

            tk.Button(self.root, text=f"Save {ticket_type} Discount", command=save_discount).pack(pady=5)

        tk.Button(self.root, text="Back to Admin Dashboard", command=self.admin_dashboard).pack(pady=10)

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
            discounted_price = ticket["price"] * (1 - self.discounts[ticket["type"]] / 100)
            self.ticket_table.insert("", "end", values=(
                ticket["type"],
                f"${discounted_price:.2f}",
                ticket["validity"],
                ticket["features"]
            ))

        tk.Label(self.root, text="Select Quantity:").pack(pady=5)
        self.quantity_spinbox = tk.Spinbox(self.root, from_=1, to=10, width=5)
        self.quantity_spinbox.pack(pady=5)

        tk.Button(self.root, text="Proceed to Payment", command=self.show_payment_page).pack(pady=10)
        tk.Button(self.root, text="Back to Dashboard", command=self.show_dashboard).pack(pady=5)

    def show_payment_page(self):
        """Displays the payment page."""
        selected_item = self.ticket_table.focus()
        if not selected_item:
            messagebox.showerror("Error", "Please select a ticket.")
            return

        selected_ticket = self.ticket_table.item(selected_item)["values"]
        if not selected_ticket or len(selected_ticket) < 2:
            messagebox.showerror("Error", "Invalid ticket selection.")
            return

        self.selected_ticket = selected_ticket
        self.selected_quantity = int(self.quantity_spinbox.get())
        self.total_price = self.selected_quantity * float(self.selected_ticket[1].replace('$', ''))

        self.clear_frame()

        tk.Label(self.root, text="Payment Page", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text=f"Ticket: {self.selected_ticket[0]}").pack(pady=5)
        tk.Label(self.root, text=f"Quantity: {self.selected_quantity}").pack(pady=5)
        tk.Label(self.root, text=f"Total Price: ${self.total_price:.2f}").pack(pady=5)

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

        if not isinstance(self.orders, dict):
            self.orders = {}

        order_id = f"ORDER-{len(self.orders) + 1}"
        self.orders[order_id] = {
            "customer": self.current_user,
            "ticket": self.selected_ticket[0],
            "quantity": self.selected_quantity,
            "total_price": self.total_price,
        }
        self.save_data(self.orders_file, self.orders)

        today = datetime.now().strftime("%Y-%m-%d")
        if today not in self.sales:
            self.sales[today] = {}
        self.sales[today][self.selected_ticket[0]] = self.sales[today].get(self.selected_ticket[0], 0) + self.selected_quantity
        self.save_data(self.sales_file, self.sales)

        messagebox.showinfo("Success", f"Purchase Confirmed!\nOrder ID: {order_id}")
        self.show_dashboard()

    def view_customer_orders(self):
        """Displays the current user's orders."""
        self.clear_frame()

        tk.Label(self.root, text="My Orders", font=("Arial", 16)).pack(pady=10)

        orders_table = ttk.Treeview(self.root, columns=("Order ID", "Ticket", "Quantity", "Total Price"), show="headings")
        orders_table.heading("Order ID", text="Order ID")
        orders_table.heading("Ticket", text="Ticket")
        orders_table.heading("Quantity", text="Quantity")
        orders_table.heading("Total Price", text="Total Price ($)")
        orders_table.pack(padx=10, pady=10)

        for order_id, order in self.orders.items():
            if order["customer"] == self.current_user:
                orders_table.insert("", "end", values=(
                    order_id,
                    order["ticket"],
                    order["quantity"],
                    f"${order['total_price']:.2f}",
                ))

        tk.Button(self.root, text="Back to Dashboard", command=self.show_dashboard).pack(pady=10)


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = AccountAndTicketApp(root)
    root.mainloop()