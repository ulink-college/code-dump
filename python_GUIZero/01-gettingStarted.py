from guizero import *         # REquires installation of guiZero. Check out https://lawsie.github.io/guizero/ for guidance


def say_hello():
    message.value = "Hello!"


app = App(title="Hello world")
button = PushButton(app, command=say_hello)
message = Text(app)

app.display()