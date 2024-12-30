from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import Config

Config.set('graphics', 'resizable', True)

# Set app size
Window.size = (500, 700)
Window.clearcolor = (1, 1, 1, 1)

# Design file
Builder.load_file('calc2.kv')

class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'
    # Button press function
    def button_press(self, button):
        # variable containing previous input
        history = self.ids.calc_input.text

        # check for errors
        if "Error" in history:
            history = ''

        # check for 0
        if history == '0':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{history}{button}'

    # Backspace function
    def remove(self):
        history = self.ids.calc_input.text
        history = history[:-1]
        self.ids.calc_input.text = history

    # Negative function
    def pos_neg(self):
        history = self.ids.calc_input.text
        # check for -
        if '-' in history:
            self.ids.calc_input.text = f'{history.replace("-", "")}'
        else:
            self.ids.calc_input.text = f'-{history}'
 
    # Decimal function
    def period(self):
        history = self.ids.calc_input.text

        if '.' in history:
            pass
        else:
            history = f'{history}.'
            self.ids.calc_input.text = history

    # Percent function
    def percent(self):
        history = self.ids.calc_input.text
        self.ids.calc_input.text = f'{float(history)*0.01}'


    # Math sign function
    def math_sign(self, sign):
        history = self.ids.calc_input.text
        self.ids.calc_input.text = f'{history}{sign}'

    # Evaluate function
    def equals(self):
        history = self.ids.calc_input.text
        # solve errors
        try:
            # evaluate text box contents
            result = eval(history)
            self.ids.calc_input.text = str(result)
        except:
            self.ids.calc_input.text = "Error"


class CalculatorApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    CalculatorApp().run()