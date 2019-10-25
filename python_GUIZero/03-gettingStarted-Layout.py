from guizero import *         # REquires installation of guiZero. Check out https://lawsie.github.io/guizero/ for guidance


app = App()
top_text = Text(app, text="at the top", align="top")
bottom_text = Text(app, text="at the bottom", align="bottom")
left_text = Text(app, text="to the left", align="left")
right_text = Text(app, text="to the right", align="right")


app.display()