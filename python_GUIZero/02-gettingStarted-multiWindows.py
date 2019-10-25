from guizero import *         # REquires installation of guiZero. Check out https://lawsie.github.io/guizero/ for guidance


def open_window():
    window.show(wait=True)

def close_window():
    window.hide()


app = App(title="Hello world")

window = Window(app, title="2nd Window")
window.hide()

openButton = PushButton(app, text="Open", command=open_window)
closeButton = PushButton(window, text="Close", command=close_window)


app.display()