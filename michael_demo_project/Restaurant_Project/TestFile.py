import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyAppDevelopment(GridLayout):
    def __int__(self, **kwargs):
        super(MyGrid, self).__int__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="Type of Investment: "))
        self.investment = TextInput(multiline=False)
        self.add_widget(self.investment)

class MyApp(App):
    def build(self):
         return MyAppDevelopment()

if __name__== "__main__":
    MyApp().run()