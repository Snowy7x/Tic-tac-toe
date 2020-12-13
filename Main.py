from tkinter import *
import tkinter.messagebox
import tkinter.font as font
from functools import partial
import random

class FrameO(object):
    name = "Main"
    frame = None

    def __init__(self, fname="Main", newFrame=None):
        self.frame = newFrame
        self.name = fname

isAi= False
buttons=list()
usedButtons=list()
nextMove = "X"
lastIndex = 0

app = Tk()
app.resizable(False, False)
app.title("X AND O From Scratch")

mainFrame = FrameO("Main", Frame(master=app, width=600, height=500))
gameFrame = FrameO("Game", Frame(master=app, width=600, height=500))
inGameFrame = FrameO("InGame", Frame(master=app, width=600, height=500))

def setAi(ai=False):
    global isAi
    isAi = ai
    print(f"Ai mode set to {ai}!")
    gameFrame.frame.pack_forget()
    gameFrame.frame.destroy()
    InGameMenu()

def getFrame(isMain=True, inGame=False):
    if isMain:
        return mainFrame
    elif inGame == False:
        return gameFrame
    else:
        return inGameFrame

def setFrame(name="Main", frame=None):
    name = name.lower()
    setattr(getFrame(name == "main"), "frame", frame)

def start():
    mainFrame.frame.pack_forget()
    mainFrame.frame.destroy()
    GameMenu()
    print("Started!")

def StartMenu():
    frame = Frame(master=app, width=600, height=500)
    frame.pack()
    start_btn = Button(master=frame, text="Start!", bg="gray", width=20, height=2, command=start)
    start_btn.place(x=210, y=190)
    start_btn = Button(master=frame, text="Options!", bg="gray", width=20, height=2)
    start_btn.place(x=210, y=250)
    setFrame("Main", frame)

def Back():
    gameFrame.frame.pack_forget()
    gameFrame.frame.destroy()
    StartMenu()
    print("Went Back")

def GameMenu():
    frame = Frame(master=app, width=600, height=500)
    frame.pack()
    aiT = partial(setAi, True)
    aiF = partial(setAi, False)
    start_btn = Button(master=frame, text="P1 vs PC(AI)", bg="gray", width=20, height=2, command=aiT)
    start_btn.place(x=210, y=190)
    start_btn = Button(master=frame, text="P1 vs P2!", bg="gray", width=20, height=2, command=aiF)
    start_btn.place(x=210, y=250)
    setFrame("Game", frame)

def hasValue(index):
    global buttons
    btn = buttons[index].cget('text')
    if(btn == 'X' or btn == 'O'):
        print(f"isi {btn}")
        return True
    else:
        return False
def hasBtnOnRight(index):
    hasRight = [0, 1, 3, 4, 6, 7]
    if index in hasRight:
        return True
    else:
        return False

def hasBtnOnLeft(index):
    hasLeft = [1, 2, 4, 5, 7, 8]
    if index in hasLeft:
        return True
    else:
        return False

def hasBtnUp(index):
    hasUp = [3, 4, 5, 6, 7, 8]
    if index in hasUp:
        return True
    else:
        return False

def hasBtnDown(index):
    hasDown = [0, 1, 2, 3, 4, 5]
    if index in hasDown:
        return True
    else:
        return False

def getBtnOnRight(index):
    btnInd = index+1
    global buttons
    btn = buttons[btnInd]
    return btn

def getBtnOnLeft(index):
    btnInd = index-1
    global buttons
    btn = buttons[btnInd]
    return btn

def getBtnUp(index):
    btnInd = index-3
    global buttons
    btn = buttons[btnInd]
    return btn

def getBtnDown(index):
    btnInd = index+3
    global buttons
    btn = buttons[btnInd]
    return btn

def isAngleTRandBL(index):
    angleInd = [2, 4, 6]
    if index in angleInd:
        return True
    else:
        return False
def isAngleTLandBR(index):
    angleInd = [0, 4, 8]
    if index in angleInd:
        return True
    else:
        return False
def isAngleWin():
    global buttons
    val1 = buttons[0].cget('text')
    val2 = buttons[2].cget('text')
    val3 = buttons[4].cget('text')
    val4 = buttons[6].cget('text')
    val5 = buttons[8].cget('text')
    if val3 == "":
        return False
    if val2 == val3 and val3 == val4:
        if val2 != "" or val4 != "":
            print('-1')
            return True
    if val1 == val3 and val3 == val5:
        if val1 != "" or val5 != "":
            print('-2')
            return True
    else:
        print('-3')
        return False

def won(who="O"):
    msg = tkinter.messagebox.showinfo("Winner", f"PLayer playing with {who} is the winner")
    Back()
    print(f"{who} is Winner")

def checkValues(val1, val2, val3):
    if(val1 == "" or val2 == "" or val3 == ""):
        return False
    elif(val3 == val2 == val1):
        return True
    else:
        return False

def CheckWin(index):
    global buttons
    btn = buttons[index].cget('text')
    val1 = btn
    val2 = "O"
    val3 = "X"

    if(isAngleTRandBL(index) or isAngleTLandBR(index)):
        if(isAngleWin()):
            won(val1)
            print("1")
            return True

    if hasBtnOnRight(index) and (hasBtnOnLeft(index) == False):
        val2 = getBtnOnRight(index).cget('text')
        val3 = getBtnOnRight(index+1).cget('text')
        if(checkValues(val1, val2, val3)):
            won(val1)
            print("2")
            return True

    if hasBtnOnLeft(index) and (hasBtnOnRight(index) is False):
        val2 = getBtnOnLeft(index).cget('text')
        val3 = getBtnOnLeft(index-1).cget('text')
        if(checkValues(val1, val2, val3)):
            print(f"2={val2} - 3={val3} - 1={val1}")
            won(val1)
            print("3")
            return True

    if(hasBtnOnLeft(index) and hasBtnOnRight(index)):
        val2 = getBtnOnLeft(index).cget('text')
        val3 = getBtnOnRight(index).cget('text')
        if(checkValues(val1, val2, val3)):
            won(val1)
            print("4")
            return True

    if hasBtnUp(index) and (hasBtnDown(index) == False):
        val2 = getBtnUp(index).cget('text')
        val3 = getBtnUp(index-3).cget('text')
        if(checkValues(val1, val2, val3)):
            won(val1)
            print("5")
            return True

    if hasBtnDown(index) and (hasBtnUp(index) == False):
        val2 = getBtnDown(index).cget('text')
        val3 = getBtnDown(index+3).cget('text')
        if(checkValues(val1, val2, val3)):
            won(val1)
            print("6")
            return True

    if(hasBtnUp(index) and hasBtnDown(index)):
        val2 = getBtnUp(index).cget('text')
        val3 = getBtnDown(index).cget('text')
        if(checkValues(val1, val2, val3)):
            won(val1)
            print("7")
            return True
    return False

def test(index, isAII=False):
    global isAi
    if(usedButtons[index]):
        print("Wrong Move!")
        return
    global nextMove
    if(nextMove == "X"):
        nextMove="O"
    else:
        nextMove="X"
    global lastIndex
    lastIndex = index
    usedButtons[index] = True
    btn = buttons[index]
    btn.configure(text=nextMove)
    if CheckWin(index) == False:
        if isAi:
            if isAII == False:
                AiMove()

"""0   1   2
   3   4   5
   6   7   8"""

def getFreeBtn():
    global buttons
    global usedButtons
    btns = list()
    i = 0
    for i in range(0, 9):
        if usedButtons[i] is False:
           btns.insert(len(btns), i)

    x = random.randint(0, len(btns) - 1)
    print(f"x = {x}")
    return btns[x]

def AiMove():
    print("Ai Turn")
    global nextMove
    global lastIndex
    global buttons
    btn = buttons[lastIndex]
    putindex = ""
    val1 = btn.cget('text')
    val2 = ""
    ch3 = [0, 2, 6, 8]
    ch4 = 4
    ch2 = [1, 3, 5, 7]

    if (hasBtnDown(lastIndex)):
        if(hasBtnDown(lastIndex)):
            if(getBtnDown(lastIndex).cget('text') == val1):
                print("1")
                putindex = lastIndex+6
        if(hasBtnDown(lastIndex+3)):
            if getBtnDown(lastIndex+3).cget('text') == val1:
                print("2")
                putindex = lastIndex+3

    if (hasBtnUp(lastIndex)):
        if(hasBtnUp(lastIndex)):
            if(getBtnUp(lastIndex).cget('text') == val1):
                putindex = lastIndex-6
        if(hasBtnUp(lastIndex-3)):
            if getBtnUp(lastIndex-3).cget('text') == val1:
                putindex = lastIndex-3

    if (hasBtnOnLeft(lastIndex)):
        if(hasBtnOnLeft(lastIndex)):
            if(getBtnOnLeft(lastIndex).cget('text') == val1):
                putindex = lastIndex-2
        if(hasBtnOnLeft(lastIndex-1)):
            if getBtnOnLeft(lastIndex-1).cget('text') == val1:
                putindex = lastIndex-1

    if (hasBtnOnRight(lastIndex)):
        if(hasBtnOnRight(lastIndex)):
            if(getBtnOnRight(lastIndex).cget('text') == val1):
                putindex = lastIndex+2
        if(hasBtnOnRight(lastIndex+1)):
            if getBtnOnRight(lastIndex+1).cget('text') == val1:
                putindex = lastIndex+1

    if (putindex != ""):
        if hasValue(putindex) is False:
            print("AI Moved")
            test(putindex, True)
        else:
            print("Could not move, Genrating random move")
            putindex = getFreeBtn()
            test(putindex, True)
    else:
        putindex = getFreeBtn()
        test(putindex, True)

def InGameMenu():
    global buttons
    global usedButtons
    global lastIndex
    lastIndex = 0
    buttons=list()
    usedButtons=list()
    buttons.clear()
    usedButtons.clear()

    frame = Frame(master=app, width=600, height=500)
    frame.pack()
    i = 0
    y = 0
    x = 0
    for i in range(0, 9):
        event = partial(test, i)
        buttonFont = font.Font(family='Helvetica', size=16, weight='bold')
        button = Button(master=frame, text=f"", bg="gray", width= 15, height=7, font=buttonFont, command=event)
        button.place(x=x, y=y)
        buttons.insert(i, button)
        usedButtons.insert(i, False)
        x += 200
        if(i == 2 or i == 5):
            x=0
            y+= 140
    start_btn = Button(master=frame, text="Exit!", bg="red", width=20, height=2, command=Back)
    start_btn.place(x=0, y=451)
    setFrame("InGame", frame)

StartMenu()
app.mainloop()
