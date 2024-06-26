from base_model import Meal, Drink


class MenuPrinter:
    def print_menu(self, menu):
        menu_items = menu.get_menu_items()
        for key in menu_items:
            product = menu_items[key]
            if(isinstance(product, Meal)):
                description_text = "" if product.get_description() == "" else " ( " + product.get_description() + " ) "
                print(str(product.get_product_id()) + " . " + product.get_name() + description_text + " | " + str(product.get_price()) + " Euro.")
            elif(isinstance(product, Drink)):
                sugar_free_text = "yes" if product.is_sugar_free() else "no"
                print(str(product.get_product_id()) + " . " + product.get_name() + " (Sugar free " + sugar_free_text + ") |" + str(product.get_price()) + " Euro.")
                
                