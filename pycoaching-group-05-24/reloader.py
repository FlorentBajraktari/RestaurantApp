from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder

class MDLive(App, MDApp):
    AUTORELOADER_PATHS = [
        (".", {"recursive": True})
    ]
    
    def build(self, *args):
        return Builder.load_file('restaurant_app_gui2.kv')

MDLive().run()    
       