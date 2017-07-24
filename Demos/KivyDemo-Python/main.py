from kivy.config import Config
Config.set("graphics", "window_state", "maximized")

from kivy.app           import App
from kivy.graphics      import Color
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button    import Button
from kivy.uix.label     import Label
from kivy.uix.textinput import TextInput


class DemoApp(App):

	def build(self):
		self.root = BoxLayout()
		self._create_layout()

	def _create_layout(self):
		self.root.orientation = "vertical"
		self.root.padding = (500, 200)
		self.root.spacing = 15

		self.input_1 = TextInput()
		self.input_1.multiline = False
		self.input_1.write_tab = False
		self.input_1.hint_text = "first name"
		self.input_1.font_size = 50
		self.root.add_widget(self.input_1)

		self.input_2 = TextInput()
		self.input_2.multiline = False
		self.input_2.write_tab = False
		self.input_2.hint_text = "last name"
		self.input_2.font_size = 50
		self.root.add_widget(self.input_2)

		self.button = Button()
		self.button.pos_hint = {"left": 0.5, "center_y": 0.5}
		self.button.background_color = Color(0.6, 0.7, 0.8, 1, mode="hsv").rgba
		self.button.text = "Submit"
		self.button.font_size = 50
		self.button.bind(on_press=self._on_button_press)
		self.root.add_widget(self.button)

		self.label = Label()
		self.label.font_size = 100
		self.root.add_widget(self.label)

	def _on_button_press(self, button):
		self.label.text = "Hello, {} {}!".format(self.input_1.text, self.input_2.text)


DemoApp().run()
