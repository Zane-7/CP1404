from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Greeter Program"
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root

    def handle_greet(self):
        print('test')
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        print('clear')
        self.root.ids.output_label.text = ' '


BoxLayoutDemo().run()
