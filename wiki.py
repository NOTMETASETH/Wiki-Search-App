from tkinter import *
import wikipedia

def on_press():
    q=get_q.get()
    text.insert(INSERT,wikipedia.summary(q))

root = Tk()
root.title("Wikipedia Search App")
question = Label(root,text='Question')
question.pack()
get_q= Entry(root,bd=5)
get_q.pack()
submit=Button(root,text='Search',command=on_press)
submit.pack()
text=Text(root)
text.pack()

root.mainloop()