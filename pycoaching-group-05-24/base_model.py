# create class Restaurant
class Restaurant:
    #__name --> private
    #_name --> protected
    #name --> public
    
    def __init__(self, name, address):
        self.__name = name
        self.__address = address
    
    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def set_address(self, address):
        self.__address = address
        
    def get_address(self):
        return self.__address

# create class client
class Client:
    def __init__(self, name, phone_nr):
        self.__name = name
        self.__phone_nr = phone_nr
        
    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def set_phone(self, phone_nr):
        self.__phone_nr = phone_nr
    
    def get_phone(self):
        return self.__phone_nr
    
    
# create class Order
class Order:
    def __init__(self):
        self.__product_list = []
        
    def get_order_items(self):
        return self.__product_list
   
class Product:
    
    def __init__(self,product_id, name, price):
       self.__name = name
       self.__product_id = product_id
       self.__price = price
       
    def set_name(self, name):
        self.__name = name
        
    def get_name(self):
        return self.__name 
    
    def get_product_id(self):
        return self.__product_id
    
    def set_product_id(self, product_id):
        self.__product_id = product_id
        
    def get_price(self):
        return self.__price
    
    def set_price(self, price):
        self.__price = price
        
class Meal(Product):
    def __init__(self, product_id, name, price, description):
        super().__init__(product_id, name, price)
        self.__description = description
        
    def get_description(self):
        return self.__description
    
    def set_description(self, description):
        self.__description = description

class Drink(Product):
    def __init__(self, product_id, name, price, sugar_free):
        super().__init__(product_id, name, price)
        self.__sugar_free = sugar_free
        #Boolean expression / sugar-free
        
    def is_sugar_free(self):
        return self.__sugar_free
    
    def set_sugar_free(self, sugar_free):
        self.__sugar_free = sugar_free
        
        
class OrderAmount:
    def __init__(self, total_order_amount, total_order_amount_vat, total_order_amount_with_vat):
        self.__total_order_amount = total_order_amount
        self.__total_order_amount_vat = total_order_amount_vat
        self.__total_order_amount_with_vat = total_order_amount_with_vat
        
        
    def get_total_order_amount(self):
        return self.__total_order_amount
    
    def set_total_order_amount(self, total_order_amount):
        self.__total_order_amount = total_order_amount
        
    def get_total_order_amount_vat(self):
        return self.__total_order_amount_vat
    
    def set_total_order_amount_vat(self, total_order_amount_vat):
        self.__total_order_amount_vat = total_order_amount_vat
        
    def get_total_order_amount_with_vat(self):
        return self.__total_order_amount_with_vat
    
    def set_total_order_amount_with_vat(self, total_order_amount_with_vat):
        self.__total_order_amount_with_vat = total_order_amount_with_vat
        
        
class OrderItem:
    def __init__(self, product, order_item_size, quantity):
        self.__product = product
        self.__order_item_size = order_item_size
        self.__quantity = quantity
        
        self.__order_item_price = 0.0
        
    
    def get_product(self):
        return self.__product
    
    def get_order_item_size(self):
        return self.__order_item_size
    
    def get_quantity(self):
        return self.__quantity
    
    def set_product(self, product):
        self.__product = product
        
    def set_order_item_size(self, order_item_size):
        self.__order_item_size = order_item_size
        
    def set_quantity(self, quantity):
        self.__quantity = quantity
    
    def get_order_item_price(self):
        return self.__order_item_price
    
    def set_order_item_price(self, order_item_price):
        self.__order_item_price = order_item_price

class Menu:
    
    def __init__(self):
        self.__menu_items = dict({})
        self.__initialize_menu_products()
    
    def __initialize_menu_products(self):
        self.__menu_items.update({100: Meal(100,"Hamburger",  4.5, "Angus beef patty, tomato, red onion")})
        self.__menu_items.update({101: Meal(101,"Cheeseburger",  5, "Angus beef patty, cheese, tomato, red onion")})
        self.__menu_items.update({102: Meal(102,"Sandwich",  3.5, "Chicken, mayonnaise, peppers")})
        self.__menu_items.update({103: Meal(103,"Hotdog",  3, "Beef, mustard, ketchup, onion, cucumber")})
        self.__menu_items.update({104: Meal(104,"Pizza", 6, "Margarita, tomato sauce, mozarella")})
        self.__menu_items.update({105: Meal(105,"Fries",  2, "french fries with ketchup and mayonnaise")})
        self.__menu_items.update({200: Drink(200,"Coca Cola", 1, False)})
        self.__menu_items.update({201: Drink(201,"Coca Cola Zero", 1, True)})
        self.__menu_items.update({202: Drink(202,"Fanta",  1, False)})
        self.__menu_items.update({203: Drink( 203,"Sprite", 1, False)})
        self.__menu_items.update({204: Drink(204,"Red Bull",  2, False)})
        self.__menu_items.update({205: Drink(205,"Coffee",  0.5, False)})
        self.__menu_items.update({300: Meal(300,"Ice cream", 1, "Homemade ice cream")})
        self.__menu_items.update({301: Meal(300, "Waffle", 2.5, "Homemade waffles")})
        self.__menu_items.update({302: Meal(300,"Brownie",  1.5, "Homemade brownies")})

    def get_menu_items(self):
        return self.__menu_items
    
    


    
    
    
    
    
    
    


    

        

