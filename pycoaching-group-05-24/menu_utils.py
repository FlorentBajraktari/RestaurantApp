from base_model import Meal, Drink, Menu
import csv
from custom_exceptions import InvalidMenuFile

class MenuPrinter:
    def print_menu(self, menu):
        print("----------MENU-----------")
        menu_items = menu.get_menu_items()
        for key in menu_items:
            menu_item = menu_items[key]
            print(str(menu_item.get_product_id()) + " . " + menu_item.get_name() + " | " + str(menu_item.get_price()))
        print("-------------------------------")

class MenuImporter:
    
    def import_menu(self, file_path):
        menu_file = open(file_path)
        csv_reader = csv.reader(menu_file)
        
        return self._transform_csv_menu_data_to_menu(csv_reader)
    
    def _transform_csv_menu_data_to_menu(self, csv_reader):
        imported_menu = Menu(True)
        for row in csv_reader:
            product_id = int(row[0])
            product_name = row[1]
            product_price = float(row[2])
            product_category = row[3]
            
            if "meal" == product_category:
                product = Meal(product_id, product_name, product_price, "")
            elif "drink" == product_category:
                sugar_free = row[4]
                product = Drink(product_id, product_name, product_price, sugar_free)
            else:
                exeption_message = "".join("The menu field couldn't be proccesed as the product category from product liste ")
                raise InvalidMenuFile(exeption_message)
            
            imported_menu.get_menu_items().update({product_id:product})
            
        return imported_menu