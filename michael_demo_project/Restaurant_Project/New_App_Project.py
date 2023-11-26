import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __int__(self, **kwargs):
        super(MyGrid, self).__int__(**kwargs)
        self.inside.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="Type of Investment: "))
        self.investment = TextInput(multiline=False)
        self.inside.add_widget(self.investment)

        self.inside.add_widget(Label(text="SPY: "))
        self.spyentry = TextInput(multiline=False)
        self.inside.add_widget(self.spyentry)

        self.inside.add_widget(Label(text="AAPL: "))
        self.aaplentry = TextInput(multiline=False)
        self.inside.add_widget(self.aaplentry)

        self.inside.add_widget(Label(text="TESLA: "))
        self.tslaentry = TextInput(multiline=False)
        self.inside.add_widget(self.tslaentry)

        self.inside.add_widget(Label(text="PLTR: "))
        self.pltrentry = TextInput(multiline=False)
        self.inside.add_widget(self.pltrentry)

        self.inside.add_widget(Label(text="EMAIL: "))
        self.emailentry = TextInput(multiline=False)
        self.inside.add_widget(self.emailentry)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", Font_size =40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        index1 = self.tslaentry.text
        index2 = self.pltrentry.text
        index3 = self.spyentry.text
        index4 = self.aaplentry.text
        email = self.emailentry.text

        print("TSLA:", index1, "PLTR:", index2, "SPY:", index3, "AAPL:", index4)
        self.tslaentry.text = ""
        self.pltrentry.text = ""
        self.spyentry.text = ""
        self.aaplentry.text = ""
        self.emailentry.text = ""
#        print("Pressed")

# The following command is to return all the fields declared in GUI
class MyApp(App):
    def build(self):
         return MyGrid()

if __name__== "__main__":
    MyApp().run()