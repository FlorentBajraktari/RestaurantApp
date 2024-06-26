from base_model import Restaurant, Product, Client, Order, Menu
from order_utils import OrderPrinter, OrderManager
from menu_utils import MenuPrinter
from location_utils import LocationManager
from calculator_utils import OrderCalculatorFactory

class RestaurantApp:
      
      def __init__(self):
            self.__current_location = None
            
      def start(self, application_mode, location_as_string):
            self.__current_location = LocationManager.get_location_from_string(location_as_string)
            
            match application_mode:
                  case "ORDER":
                        self.run_order_process()
                  case "TABLE_RESERVATION":
                        self.run_table_reservation_process()
                  case _:
                        raise Exception("No valid applicaion mode is selected")
                        
      def run_order_process(self):
            #Create an object of restaurant
            restaurant = Restaurant("Route 66","Te Heroinat, Prishtine")
            
            #Create a Client object
            client = Client("Sumea Qadraku", "+383123123")

            menu = Menu()
            menuprinter = MenuPrinter()
            menuprinter.print_menu(menu)
            
            order_manager = OrderManager()
            order = order_manager.create_order(menu)
            order_manager.get_orders().append(order)
            
            self.__calculate_and_print_order_details(restaurant, client, order)
            
            
      def __calculate_and_print_order_details(self, restaurant, client, order):
            order_calculator = self.get_order_calculator()
            order_amount = order_calculator.calculate_order_amount(order)
            
            order_printer = OrderPrinter()
            order_printer.print_order_info(restaurant, client, order, order_amount, order_calculator.get_vat_rate(False))
            
      def run_table_reservation_process(self):
            print("Table reservation is completed successfully.")
            
      def get_order_calculator(self):
            return OrderCalculatorFactory.get_order_calculator_by_location(self.__current_location)
      
restaurant_app = RestaurantApp()
restaurant_app.start("ORDER","KOSOVO")



