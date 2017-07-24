from kivy.config import Config
Config.set("graphics", "window_state", "maximized")

from kivy.app           import App
from kivy.uix.boxlayout import BoxLayout


class DemoLayout(BoxLayout):
  pass

class DemoApp(App):
  def build(self):
    self.root = DemoLayout()


DemoApp().run()

