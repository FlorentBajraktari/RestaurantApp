from kivy.uix.gridlayout import product
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from menu_utils import MenuImporter
from kivy.core.window import Window
from kivy.lang import Builder

class RestaurantAppGUI(MDApp):
    __selected_product = None
    
    def build(self):
        # Step 1:
        Window.size= (900, 700)
        screen = Builder.load_file('restaurant_app_gui.kv')
        
        menu_importer = MenuImporter()
        menu = menu_importer.import_menu('menu-list.csv')
        
        product_list = list(menu.get_menu_items().values())
        
        table_row_data = []
        for product in product_list:
            table_row_data.append((product.get_product_id(), product.get_name(), product.get_price()))
        
        # Step 2:
        menu_table = MDDataTable(
            pos_hint = {'center_x': 0.5, 'center_y': 0.5},
            size_hint = (0.9, 0.6),
            check = True,
            
            column_data = [
                ("Id", dp(30) ),
                ("name", dp(75)),
                ("Price", dp(30))
            ],
            row_data = table_row_data
          
        )
        menu_table.bind(on_check_press=self.checked)
        menu_table.bind(on_row_press=self.on_row_press)
        
        
        screen.children[0].add_widget(menu_table)
        return screen
    
    def checked(self, instance_table, current_row):
        print(current_row)
        
    def on_row_press(self, instance_table, instance_row):
        row_number = int(instance_row.index/len(instance_table.column_data))
        self.__selected_product = instance_table.row_data[row_number]
        
        self.get_text_field_box_layout().children[2].tet = str(self.__selected_product[0])
        self.get_text_field_box_layout().children[1].tet = str(self.__selected_product[1])
        self.get_text_field_box_layout().children[0].tet = str(self.__selected_product[2])
        
    def add_row(self):
        id = self.get_text_field_box_layout().children[2].text 
        name = self.get_text_field_box_layout().children[1].text
        price = self.get_text_field_box_layout().children[0].text
        self.get_menu_datatable_widget().row_data.append([id, name, price])
        
    def update_row(self):
        id = int(self.get_text_field_box_layout().children[2].text) 
        name = self.get_text_field_box_layout().children[1].text
        price = float(self.get_text_field_box_layout().children[0].text)
        updated_row_data = (id, name, price)
        
        row_data = self.get_menu_datatable_widget().row_data
        index = self.get_menu_datatable_widget().row_data.index(self.__selected_product)
        row_data[index] = updated_row_data
    
    def delete_row(self):
        table_data = self.get_menu_datatable_widget().row_data
        table_data.remove(self.__selected_product)
        
        
    def get_menu_datatable_widget(self):
        md_card = self.root.children[0]
        menu_table = md_card.children[0]
        return menu_table
    
    def get_text_field_box_layout(self):
        md_card = self.root.children[0]
        general_box_layout = md_card.children[1]
        text_field_box_layout = general_box_layout.children[1]
        return text_field_box_layout
    
        
 
RestaurantAppGUI().run()       
        
        
