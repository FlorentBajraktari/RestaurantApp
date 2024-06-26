from base_model import Order, OrderAmount, OrderItem
from base_enum import OrderItemSize

class OrderPrinter:
    # create new method Print order item info
    def print_order_info(self, restaurant, client, order, order_amount, vat_rate):
        self.__print_order_info_header(client)
        order_products = order.get_order_items()
        for order_product in order_products:
            self.__print_order_item_info(order_product)
        self.__print_order_info_footer(restaurant, order_amount, vat_rate)
        
        
        
    def __print_order_item_info(self, order_item):
        product = order_item.get_product()
        total_order_item_price = order_item.get_order_item_price() * order_item.get_quantity()
        
        print(str(order_item.get_quantity()) + " x | " + str(product.get_product_id()) + " . " + product.get_name() + 
              " | " + str(order_item.get_order_item_price()) + " | " + str(total_order_item_price) + " Euro.")
        
    
    # create new method print order item info header
    def __print_order_info_header(self, client):
        print("-----------------------------------------")
        print("Order from: " + str(client.get_name()) + ": ")
        print("Contact Number: " + str(client.get_phone()))
        print("------------------------------------------")
    
    # create new method print order info footer
    
    def __print_order_info_footer(self, restaurant, order_amount, vat_rate):
        print("-------------------------------------------")
        print("The total price of the order is: ")
        print("SUB TOTAL: " + str(order_amount.get_total_order_amount()) + " Euro.")
        print("VAT: " +  str(int(vat_rate)) + str(order_amount.get_total_order_amount_vat()) + " Euro.")
        print("TOTAL: " + str(order_amount.get_total_order_amount_with_vat()) + " Euro.")
        print("-------------------------------------------------")
        print(restaurant.get_name() + " in " + restaurant.get_address())

    
        
class OrderManager:
    
    def __init__(self):
        self.__orders = []
        
    def get_orders(self):
        return self.__orders
    
    def create_order(self, menu):
        order = Order()
        
        self.add_order_item(order, menu.get_menu_items().get(100), 0, OrderItemSize.XXL)
        self.add_order_item(order, menu.get_menu_items().get(101), 2, OrderItemSize.MEDIUM)
        self.add_order_item(order, menu.get_menu_items().get(200), 1, OrderItemSize.LARGE)
        self.add_order_item(order, menu.get_menu_items().get(201), 3, OrderItemSize.XXL)
        
        return order
    
    def add_order_item(self, order, product, quantity, order_item_size):
        order_item = self.create_order_item(product, order_item_size, quantity)
        order.get_order_items().append(order_item)
        
    def create_order_item(self, product, order_item_size, quantity):
        order_item = OrderItem(product, order_item_size, quantity)
        return order_item
            
            
            
                
        
            
        
           
            
    
    
        
        
        
        
        
        