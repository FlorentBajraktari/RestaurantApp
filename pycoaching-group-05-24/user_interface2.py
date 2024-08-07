from kivy.uix.gridlayout import product
from kivymd.uix.bottomnavigation.bottomnavigation import WindowSDL
from kivymd.app import MDApp
from kivy.core.window import Window 
from kivy.lang import Builder
from menu_utils import MenuImporter
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from base_model import Restaurant, Client, Order, Product
from order_calculators import OrderCalculatorKS, OrderCalculatorGER
from order_utils import OrderManager
class RestaurantApp(MDApp):
    
    __selected_product = None
    
    def build(self):
        
        Window.size = (900,600)
        self.screen = Builder.load_file('restaurant_app_gui2.kv')
        
        first_box_layout = self.screen.ids.first_box_layout
        second_box_layout = self.screen.ids.second_box_layout
        self.quanity_input = self.screen.ids.qiantity_input
        self.spiner = self.screen.ids.spiner
        self.check_box_ks = self.screen.ids.check_box_ks
        self.check_box_ger = self.screen.ids.check_box_ger
        self.name_field = self.screen.ids.name_field
        self.phone_field = self.screen.ids.phone_field
        self.invoice_lebel = self.screen.ids.invocice_lebel
        
        
        menu_importer = MenuImporter()
        menu = menu_importer.import_menu('menu-liste.csv')
        product_list = list(menu.get_menu_items().values())
        
        table_row_data = []
        for product in product_list:
            table_row_data.append((product.get_product_id(), product.get_name(), product.get_price()))
        
        # Step 2:
        menu_table = MDDataTable(
            pos_hint = {'center_x': 0.5, 'center_y': 0.5},
            size_hint = (0.9, 0.6),
            check=True,
            
            column_data = [
                ("Id", dp(30)),
                ("name", dp(75)),
                ("Price", dp(30))
            ],
            row_data = table_row_data
        )    
        first_box_layout.add_widget(menu_table)
        menu_table.bind(on_row_press = self.on_row_press)
        
        self.order_table = MDDataTable(
            size_hint=(1,1),
            padding=[0,30,0,0],
            check=True,
            column_data=[
                ("Id", dp(20)),
                ("name", dp(20)),
                ("Price", dp(20)),
                ("Quantity", dp(20)),
                ("Size", dp(20))
                
            ],
            row_data = []
          
            
        )
        second_box_layout.add_widget(self.order_table)
        self.order_table.bind(on_row_press = self.on_row_press)
        
        return self.screen

    def on_row_press(self, instance_table, instance_row):
        row_number = int(instance_row.index/len(instance_table.column_data))
        self.__selected_product = instance_table.row_data[row_number]
        
    def add_to_order(self, instance):
        if self.__selected_product is None:
            message = 'Please select a product'
        elif self.quantity_input.text == " ":
            message = 'Please enter a quantity'
        elif self.spinner.text =='Select Size':
            message = 'Please select an order item size'
        
        if 'message' in locals():
            popup = Popup(tittle='Invalid data', content=Label(text=message),
                          size_hint=(None, None), size=(400, 200))
            popup.open()
        
        
        else:
            quantity = self.quantity_tnput.text 
        order_item_size = self.spinner.text
        
        if quantity and order_item_size:
            product_data = [
                self.__selected_product[0], #id: 
                self.__selected_product[1], #NAME
                self.__selected_product[2], #PRICE
                quantity,
            order_item_size
            ]       
            self.order_table.row_data.append(product_data)
            self.order_table.update_row_data

            self.__selected_product = None
            self.quanity_input.text = ""
            self.spiner.tex = "Select Size"

    def delete_from_order(self, instance):
        if self.__selected_product is None:
            return
        
        selected_row = None
        for row in self.order_table.row_data:
            if row[0] == self.__selected_product[0] and row[1] == self.__selected_product[1]:
                selected_row = row
                break
        
        if selected_row:
            self.order_table.row_data.remove(selected_row)
            self.order_table.update_row
        
    def reset(self, istance):
        self.order_table.row_data = [1]
        self.quanity_input.text = " " 
        self.spinner.text = "Select Size"
        self.name_field.text = " "
        self.phone_field.text = " "
        self.invoice_lebel.text = " Invoice will be printed here. "
        
    def calculate_amount(self, instance):
        restaurant = Restaurant("Route 66", "Te Heroinat, Prishtine")
        name = self.name_field.text 
        phone_number = self.phone_field.text
        client = Client(name, phone_number)
        order_calculator = OrderCalculatorKS() if self.check_box_ks.active else OrderCalculatorGER()
        order = Order()
        order_menager = OrderManager()
        
        
        
        for product in self.order_table.row_data:
            product_id = int(product[0])
            product_name = str(product[1])
            priec = float(product[2])
            quantity = float(product[3])
            size = self._get_size(str(product[4]))
            order_product = Product(product_id, product_name, priec)
            order_menager.add_order_item(order,product,order_product, size, quantity)
        order_amount = order_calculator.calculate_order_amount(order)
        
              
            
            
        
        
        
             

RestaurantApp().run()   
            
        
