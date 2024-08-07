from base_model import Restaurant, Product, Client, Order, Menu
from order_utils import OrderPrinter, OrderManager
from menu_utils import MenuPrinter, MenuImporter
from location_utils import LocationManager
from calculator_utils import OrderCalculatorFactory
from base_enum import Location, ApplicationMode
from application_utils import ApplicationModeMenager

class RestaurantApp:
    def __init__(self):
        self.__current_location = None
        self.__file_path = 'menu-list.csv'

    def start(self):
        self.__current_location = self.get_current_location()
        application_mode = self.get_application_mode()
        self.execute_application_mode(application_mode)

    def get_current_location(self):
        print("Please select the location (type number): ")
        location_options = "".join([str(location_option.value) + ". " + location_option.name + "\n" for location_option in Location])
        print(location_options)
        
        location_id_input = input()
        location_id = int(location_id_input)
        location = LocationManager.get_location_from_id(location_id)
        return location

    def get_application_mode(self):
        print("Please select the application mode (type number)")
        application_mode_options = ''.join([str(app_mode.value) + '. ' + app_mode.name + ' \n' for app_mode in ApplicationMode])
        print(application_mode_options)
        
        application_mode_input = input()
        application_mode_id = int(application_mode_input)
        application_mode = ApplicationModeMenager.get_application_mode_from_id(application_mode_id)
        return application_mode

    def execute_application_mode(self, application_mode):
        match application_mode:
            case ApplicationMode.ORDER:
                self.run_order_process()
            case ApplicationMode.TABLE_RESERVATION:
                self.run_table_reservation_process()
            case _:
                raise Exception("No valid application mode is selected")

    def run_order_process(self):
        restaurant = Restaurant("Route 66", "Te Heroinat, Prishtine")
        client = Client("Florent Bajraktari", "+417831233")

        menu_importer = MenuImporter()
        menu = menu_importer.import_menu(self.__file_path)
        
        menu_printer = MenuPrinter()
        menu_printer.print_menu(menu)
        
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
restaurant_app.start()
