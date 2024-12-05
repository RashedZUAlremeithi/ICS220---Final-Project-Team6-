from Main import *
# Ticket Class Test
print("--- Ticket Class Test ---")
ticket1 = Ticket(TicketType.TWO_DAY, "Two-Day Park Pass", 100, "2 days", 0, "Non-transferable", datetime(2024, 12, 25))
print("Original Price:", ticket1.get_price())
ticket1.apply_discount()
print("Price after applying discount:", ticket1.get_price())
print("Ticket Description:", ticket1.get_description())

# Customer Class Test
print("--- Customer Class Test ---")
customer1 = Customer("Ahmed", "Ahmed@example.com", "Ahmed", "securepassword")
print("Customer Name:", customer1.get_name())
print("Customer Email:", customer1.get_email())
customer1.set_name("Jane Doe")
print("Updated Customer Name:", customer1.get_name())

# Order Class Test
print("--- Order Class Test ---")
order1 = Order(customer1, ticket1, 2, 180, PaymentType.CREDIT_CARD)
print("Order Details: Customer:", order1.get_customer().get_name())
print("Ticket Type:", order1.get_ticket().get_ticket_type().value)
print("Quantity:", order1.get_quantity())
print("Total Price:", order1.get_total_price())
print("Amount Paid:", order1.get_amount_paid())
print("Payment Type:", order1.get_payment_type().value)
print("Order Date:", order1.get_order_date())

# Park Class Test
print("--- Park Class Test ---")
park1 = Park("Wonderland", "abu dhabi", {"Monday": "9 AM - 9 PM", "Tuesday": "9 AM - 9 PM"})
print("Park Name:", park1.get_name())
print("Park Location:", park1.get_location())
park1.add_attraction("Roller Coaster")
park1.add_attraction("Ferris Wheel")
print("Attractions:", park1.list_attractions())
park1.remove_attraction("Ferris Wheel")
print("Attractions after removal:", park1.list_attractions())
park1.add_event("Music Festival")
print("Events:", park1.list_events())
park1.add_service("Free Wi-Fi")
print("Services:", park1.list_services())