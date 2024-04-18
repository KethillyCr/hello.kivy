from kivy.app import App 
from kivy.uix.button import Button
class myApp(App):
    def build(self):
        return Button(text="Hello World! This is my first progam in kivy. I'm a SESIANO student, and i love my Teacher")
if __name__ == '__main__':
    myApp().run()