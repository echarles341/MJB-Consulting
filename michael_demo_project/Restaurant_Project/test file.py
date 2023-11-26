import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class MyGrid(GridLayout):
    def __int__(self, **kwargs):
        super(MyGrid, self).__int__(**kwargs)
        self.inside.cols = 2
        self.add_widget(Label(text="Type of Investment: "))
        self.investment = TextInput(multiline=False)
        self.add_widget(self.investment)


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
