"""
    Exercise2 : write a Python class Restaurant with attributes like menu_items, book_table,
                and customer_orders, and methods like add_item_to_menu, book_tables, and customer_order.
                Perform the following tasks now : 
                    -Now add items to the menu.
                    -Make tabke reservations. 
                    -Take customer orders.
                    -Print the menu. 
                    -Print table reservations. 
                    -Print customer orders. 
                Note: Use dictionaries and lists to store the data 
"""

class Restaurant: 
    def __init__(self):
        self.menu_items = {}
        self.book_table = []
        self.customer_orders = []
        
    def add_item_to_menu(self, item, price ):    
        self.menu_items[item] = price 
        
    def book_tables(self, table_number):
        self.book_table.append(table_number)
        
    def customer_order(self, table_number,order):
        order_details = {"table_number":table_number, "order": order}
        self.customer_orders.append(order_details)
        
    def print_menu_items(self):
        for item, price in self.menu_items.items():
            print("{}: {}".format(item, price ))
            
    def print_table_reservations(self):
        for table in self.book_table:
            print("==>Table {}".format(table))
            
    def print_customer_orders(self):
        for order in self.customer_orders:
            print("==>Table {}: {}".format(order["table_number"], order[ "order"]))
restaurant =Restaurant()

# Add items 
restaurant.add_item_to_menu("==>Cheeseburger", 9.99)
restaurant.add_item_to_menu("==>Grilled Salmon", 19.99)
restaurant.add_item_to_menu("==>French Fries", 3.99)
restaurant.add_item_to_menu("==>Fish & Chips", 15)

# Book table 
restaurant.book_tables(1) 
restaurant.book_tables(2) 
restaurant.book_tables(3) 

# Orders items
restaurant.customer_order(1, "Cheeseburger")
restaurant.customer_order(1, "Grilled Salmon")
restaurant.customer_order(2, "Fish & Chips")
restaurant.customer_order(2, "Grilled Salmon")
restaurant.customer_order(3, "French Fries")
print("------------------------------------------------------------ ")
print("Popular dishes in the restaurant along with their prices")
restaurant.print_menu_items()
print("------------------------------------------------------------ ")
print("Table reserved in the restaurant: ")
restaurant.print_table_reservations()
print("------------------------------------------------------------ ")
print("Print customer orders: ")
restaurant.print_customer_orders()
print("------------------------------------------------------------ ")