from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
import wikipedia

class WikipediaSearchApp(App):
    def build(self):
        return Builder.load_file('wiki.kv')

    def search(self, query):
        self.root.ids.result_label.text = "Searching..."
        try:
            result = wikipedia.summary(query)
            result = '\n\n'.join(result.split('\n'))
            self.root.ids.result_label.text = result
        except wikipedia.DisambiguationError:
            self.root.ids.result_label.text = "Multiple results found. Please refine your query."
        except wikipedia.PageError:
            self.root.ids.result_label.text = "Page does not exist. Please try another query."


if __name__ == "__main__":
    WikipediaSearchApp().run()
