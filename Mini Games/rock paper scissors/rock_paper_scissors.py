from tkinter import *
import random 

#main window TK
root = Tk()

root.title('Rock Paper Scissors')

root.iconbitmap('roc.ico')
root.resizable(width=False,height=False)

click = True

#photoImage of hands position for dictaion of rock paper scissors
rHandPhoto = PhotoImage(file = 'rHand.png')
pHandPhoto = PhotoImage(file = 'pHand.png')
sHandPhoto = PhotoImage(file = 'sHand.png')

#symbol photoImage of rock paper scissors
rockPhoto = PhotoImage(file = 'rock.png')
paperPhoto = PhotoImage(file = 'paper.png')
scissorsPhoto = PhotoImage(file = 'scissors.png')

#win,lose,tie photos
winPhoto = PhotoImage(file = 'win.png')
loosePhoto = PhotoImage(file = 'loose.png')
tiePhoto = PhotoImage(file = 'tie.png')

rHandButton = ''
pHandButton = ''
sHandButton = ''

#for arraging pictures in grid
def play():
    global rHandButton,pHandButton,sHandButton
    #for your selection
    rHandButton = Button(root,image = rHandPhoto, command = lambda:youPick('rock'))
    pHandButton = Button(root,image = pHandPhoto,
                                          command = lambda:youPick('paper'))
    sHandButton = Button(root,image = sHandPhoto,
                                          command = lambda:youPick('scissors'))
    #Arraging picture in grid
    rHandButton.grid(row = 0,column = 0)
    pHandButton.grid(row = 0,column = 1)
    sHandButton.grid(row = 0,column = 2)

def computerPick():
    #computer random choice out of three
    choice = random.choice(['rock','paper','scissors'])
    return choice

def youPick(yourChoice):
    #our picked option
    global click

    compPick = computerPick()

    #win and lose 
    if click == True:
        #our choice rock
        if yourChoice == 'rock':
            rHandButton.configure(image = rockPhoto)
            #our choice rock and comparing with computer answers
            if compPick == 'rock':
                pHandButton.configure(image = rockPhoto)
                sHandButton.configure(image = tiePhoto)
                click = False
            elif compPick == 'paper':
                pHandButton.configure(image = paperPhoto)
                sHandButton.configure(image = loosePhoto)
                click = False
            else:
                pHandButton.configure(image = scissorsPhoto)
                sHandButton.configure(image = winPhoto)
                click = False


        #now our choice paper
        elif yourChoice == 'paper':
            pHandButton.configure(image = paperPhoto)
            if compPick == 'rock':
                rHandButton.configure(image = rockPhoto)
                sHandButton.configure(image = winPhoto)
                click = False
            elif compPick == 'paper':
                rHandButton.configure(image = paperPhoto)
                sHandButton.configure(image = tiePhoto)
                click = False
            else:
                rHandButton.configure(image = scissorsPhoto)
                sHandButton.configure(image = loosePhoto)
                click = False


        #now our choice scissors                
        elif yourChoice == 'scissors':
            sHandButton.configure(image = scissorsPhoto)
            if compPick == 'rock':
                pHandButton.configure(image = rockPhoto)
                rHandButton.configure(image = loosePhoto)
                click = False
            elif compPick == 'paper':
                pHandButton.configure(image = paperPhoto)
                rHandButton.configure(image = winPhoto)
                click = False
            else:
                pHandButton.configure(image = scissorsPhoto)
                rHandButton.configure(image = tiePhoto)
                click = False

    #After the results back to play option            
    else:
        if yourChoice == 'rock' or yourChoice == 'paper' or yourChoice == 'scissors':
            rHandButton.configure(image = rHandPhoto)
            pHandButton.configure(image = pHandPhoto)
            sHandButton.configure(image = sHandPhoto)
            click = True

play()

root.mainloop()

