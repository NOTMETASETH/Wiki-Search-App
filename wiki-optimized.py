import tkinter as tk
from tkinter import ttk, Text
from ttkthemes import ThemedStyle
import wikipedia

class WikipediaSearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Wikipedia Search App")

        style = ThemedStyle(self.root)
        style.set_theme("radiance")  # Radiance theme has round buttons

        self.question_label = ttk.Label(self.root, text='Question')
        self.question_label.pack()

        self.query_entry = ttk.Entry(self.root)
        self.query_entry.pack()

        self.submit_button = ttk.Button(self.root, text='Search', command=self.search)
        self.submit_button.pack()

        self.text_frame = ttk.Frame(self.root)
        self.text_frame.pack()

        self.text_box = Text(self.text_frame, wrap='word')
        self.text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scroll_bar = ttk.Scrollbar(self.text_frame)
        self.scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)

        self.text_box.config(yscrollcommand=self.scroll_bar.set)
        self.scroll_bar.config(command=self.text_box.yview)

    def search(self):
        query = self.query_entry.get()
        self.query_entry.delete(0, tk.END)  # Clear the query entry box
        self.text_box.delete(1.0, tk.END)  # Clear the text box
        self.text_box.insert(tk.INSERT, "Searching...\n")
        self.root.update()  # Update the UI
        try:
            result = wikipedia.summary(query)
            self.text_box.delete(1.0, tk.END)  # Clear the "Searching..." message
            result = '\n\n'.join(result.split('\n'))
            self.text_box.insert(tk.INSERT, result)
        except wikipedia.DisambiguationError:
            self.text_box.insert(tk.INSERT, "Multiple results found. Please refine your query.")
        except wikipedia.PageError:
            self.text_box.insert(tk.INSERT, "Page does not exist. Please try another query.")


def main():
    root = tk.Tk()
    app = WikipediaSearchApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
