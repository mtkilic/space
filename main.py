from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


class MyBox(BoxLayout):
    pass

class SpaceApp(App):
    def build(self):
        return MyBox()

if __name__ == '__main__':
    SpaceApp().run()