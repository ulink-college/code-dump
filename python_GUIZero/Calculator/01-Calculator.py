from guizero import App, Text, TextBox, PushButton, Box

calcApp = App(title="guiZero Calculator")

boxDisplay = Box(calcApp, width="fill", align="top", border=True)
calcDisplay = Text(boxDisplay, text="0", width="fill")

boxNumbers = Box(calcApp, layout="grid", align="left")

btnNine = PushButton(boxNumbers, text="9", grid=[2,0])
btnEight = PushButton(boxNumbers, text="8", grid=[1,0])
btnSeven = PushButton(boxNumbers, text="7", grid=[0,0])
btnSix = PushButton(boxNumbers, text="6", grid=[2,1])
btnFive = PushButton(boxNumbers, text="5", grid=[1,1])
btnFour = PushButton(boxNumbers, text="4", grid=[0,1])
btnThree = PushButton(boxNumbers, text="3", grid=[2,2])
btnTwo = PushButton(boxNumbers, text="2", grid=[1,2])
btnOne = PushButton(boxNumbers, text="1", grid=[0,2])
btnZero = PushButton(boxNumbers, text="    0    ", grid=[0,3,2,3])
btnDot = PushButton(boxNumbers, text=".", grid=[2,3])



calcApp.display()