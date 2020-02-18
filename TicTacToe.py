from tkinter import *
import tkinter as tk
from tkinter import messagebox


c=0
e=0
player=''
print("Hey There!! Welcome to the Game")
a='O'
b='X'
print("Who will Play First?\nPlayer 1(O) or Player 2(X)?")
print("Enter 1 for Player 1(O) and 2 for Player 2(X): ")


def chance(p):
    global a, b, player, p1, p2, l1, b1, b2, b3, b4, b5, b6, b7, b8, b9
    p1.config(state=DISABLED)
    p2.config(state=DISABLED)
    b1.config(state=NORMAL)
    b2.config(state=NORMAL)
    b3.config(state=NORMAL)
    b4.config(state=NORMAL)
    b5.config(state=NORMAL)
    b6.config(state=NORMAL)
    b7.config(state=NORMAL)
    b8.config(state=NORMAL)
    b9.config(state=NORMAL)
    l1.config(text='PLAYER CHANCE')
    if p=='1':
        player = a
        p1.config(bg='red')
    elif p=='2':
        player = b
        p2.config(bg='red')
board=[['*','*','*'],
       ['*','*','*'],
       ['*','*','*']]
for i in board:
    print(i)
    
    
def play_check(pos1):
    game_board(pos1)
    check()
    

def game_board(pos):
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, player, c, board, p1, p2, oc, root
    print("Choose Position(1-9)")
    if pos=='1':
        row=0
        column=0
        b1.config(state=DISABLED, text=player)
        c+=1
    elif pos=='2':
        row=0
        column=1
        b2.config(state=DISABLED, text=player)
        c+=1
    elif pos=='3':
        row=0
        column=2
        b3.config(state=DISABLED, text=player)
        c+=1
    elif pos=='4':
        row=1
        column=0
        b4.config(state=DISABLED, text=player)
        c+=1
    elif pos=='5':
        row=1
        column=1
        b5.config(state=DISABLED, text=player)
        c+=1
    elif pos=='6':
        row=1
        column=2
        b6.config(state=DISABLED, text=player)
        c+=1
    elif pos=='7':
        row=2
        column=0
        b7.config(state=DISABLED, text=player)
        c+=1
    elif pos=='8':
        row=2
        column=1
        b8.config(state=DISABLED, text=player)
        c+=1
    elif pos=='9':
        row=2
        column=2
        b9.config(state=DISABLED, text=player)
        c+=1
    board[row][column]=player
    if player==a:
        player=b
        p2.config(bg='red')
        p1.config(bg=oc)
    elif player==b:
        player=a
        p1.config(bg='red')
        p2.config(bg=oc)
    for i in board:
        print(i)
        

def check():
    global a, b, board, b1, b2, b3, b4, b5, b6, b7, b8, b9, c
    if board[0][0]==a and board[0][1]==a and board[0][2]==a:
        print("Player",a,"Wins!")
        b1.config(state=DISABLED, bg='red')
        b2.config(state=DISABLED, bg='red')
        b3.config(state=DISABLED, bg='red')
        b4.config(state=DISABLED)
        b5.config(state=DISABLED)
        b6.config(state=DISABLED)
        b7.config(state=DISABLED)
        b8.config(state=DISABLED)
        b9.config(state=DISABLED)
        messagebox.showinfo('YEAH!', 'Player '+a+' Won!')
    elif board[0][0]==b and board[0][1]==b and board[0][2]==b:
        print("Player",b,"Wins!")
        b1.config(state=DISABLED, bg='red')
        b2.config(state=DISABLED, bg='red')
        b3.config(state=DISABLED, bg='red')
        b4.config(state=DISABLED)
        b5.config(state=DISABLED)
        b6.config(state=DISABLED)
        b7.config(state=DISABLED)
        b8.config(state=DISABLED)
        b9.config(state=DISABLED)
        messagebox.showinfo('YEAH!', 'Player '+b+' Won!')
    elif board[1][0]==a and board[1][1]==a and board[1][2]==a:
        print("Player",a,"Wins!")
        b1.config(state=DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)
        b4.config(state=DISABLED, bg='red')
        b5.config(state=DISABLED, bg='red')
        b6.config(state=DISABLED, bg='red')
        b7.config(state=DISABLED)
        b8.config(state=DISABLED)
        b9.config(state=DISABLED)
        messagebox.showinfo('YEAH!', 'Player '+a+' Won!')
    elif board[1][0]==b and board[1][1]==b and board[1][2]==b:
        print("Player",b,"Wins!")
        b1.config(state=DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)
        b4.config(state=DISABLED, bg='red')
        b5.config(state=DISABLED, bg='red')
        b6.config(state=DISABLED, bg='red')
        b7.config(state=DISABLED)
        b8.config(state=DISABLED)
        b9.config(state=DISABLED)
        messagebox.showinfo('YEAH!', 'Player '+b+' Won!')
    elif board[2][0]==a and board[2][1]==a and board[2][2]==a:
        print("Player",a,"Wins!")
        b1.config(state=DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)
        b4.config(state=DISABLED)
        b5.config(state=DISABLED)
        b6.config(state=DISABLED)
        b7.config(state=DISABLED, bg='red')
        b8.config(state=DISABLED, bg='red')
        b9.config(state=DISABLED, bg='red')
        messagebox.showinfo('YEAH!', 'Player '+a+' Won!')
    elif board[2][0]==b and board[2][1]==b and board[2][2]==b:
        print("Player",b,"Wins!")
        b1.config(state=DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)
        b4.config(state=DISABLED)
        b5.config(state=DISABLED)
        b6.config(state=DISABLED)
        b7.config(state=DISABLED, bg='red')
        b8.config(state=DISABLED, bg='red')
        b9.config(state=DISABLED, bg='red')
        messagebox.showinfo('YEAH!', 'Player '+b+' Won!')
    elif board[0][0]==a and board[1][0]==a and board[2][0]==a:
        print("Player",a,"Wins!")
        b1.config(state=DISABLED, bg='red')
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)
        b4.config(state=DISABLED, bg='red')
        b5.config(state=DISABLED)
        b6.config(state=DISABLED)
        b7.config(state=DISABLED, bg='red')
        b8.config(state=DISABLED)
        b9.config(state=DISABLED)
        messagebox.showinfo('YEAH!', 'Player '+a+' Won!')
    elif board[0][0]==b and board[1][0]==b and board[2][0]==b:
        print("Player",b,"Wins!")
        b1.config(state=DISABLED, bg='red')
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)
        b4.config(state=DISABLED, bg='red')
        b5.config(state=DISABLED)
        b6.config(state=DISABLED)
        b7.config(state=DISABLED, bg='red')
        b8.config(state=DISABLED)
        b9.config(state=DISABLED)
        messagebox.showinfo('YEAH!', 'Player '+b+' Won!')
    elif board[0][1]==a and board[1][1]==a and board[2][1]==a:
        print("Player",a,"Wins!")
        b1.config(state=DISABLED)
        b2.config(state=DISABLED, bg='red')
        b3.config(state=DISABLED)
        b4.config(state=DISABLED)
        b5.config(state=DISABLED, bg='red')
        b6.config(state=DISABLED)
        b7.config(state=DISABLED)
        b8.config(state=DISABLED, bg='red')
        b9.config(state=DISABLED)
        messagebox.showinfo('YEAH!','Player '+a+' Won!')
    elif board[0][1]==b and board[1][1]==b and board[2][1]==b:
        print("Player",b,"Wins!")
        b1.config(state=DISABLED)
        b2.config(state=DISABLED, bg='red')
        b3.config(state=DISABLED)
        b4.config(state=DISABLED)
        b5.config(state=DISABLED, bg='red')
        b6.config(state=DISABLED)
        b7.config(state=DISABLED)
        b8.config(state=DISABLED, bg='red')
        b9.config(state=DISABLED)
        messagebox.showinfo('YEAH!', 'Player '+b+' Won!')
    elif board[0][2]==a and board[1][2]==a and board[2][2]==a:
        print("Player",a,"Wins!")
        b1.config(state=DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED, bg='red')
        b4.config(state=DISABLED)
        b5.config(state=DISABLED)
        b6.config(state=DISABLED, bg='red')
        b7.config(state=DISABLED)
        b8.config(state=DISABLED)
        b9.config(state=DISABLED, bg='red')
        messagebox.showinfo('YEAH!', 'Player '+a+' Won!')
    elif board[0][2]==b and board[1][2]==b and board[2][2]==b:
        print("Player",b,"Wins!")
        b1.config(state=DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED, bg='red')
        b4.config(state=DISABLED)
        b5.config(state=DISABLED)
        b6.config(state=DISABLED, bg='red')
        b7.config(state=DISABLED)
        b8.config(state=DISABLED)
        b9.config(state=DISABLED, bg='red')
        messagebox.showinfo('YEAH!', 'Player '+b+' Won!')
    elif board[0][0]==a and board[1][1]==a and board[2][2]==a:
        print("Player",a,"Wins!")
        b1.config(state=DISABLED, bg='red')
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)
        b4.config(state=DISABLED)
        b5.config(state=DISABLED, bg='red')
        b6.config(state=DISABLED)
        b7.config(state=DISABLED)
        b8.config(state=DISABLED)
        b9.config(state=DISABLED, bg='red')
        messagebox.showinfo('YEAH!', 'Player '+a+' Won!')
    elif board[0][0]==b and board[1][1]==b and board[2][2]==b:
        print("Player",b,"Wins!")
        b1.config(state=DISABLED, bg='red')
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)
        b4.config(state=DISABLED)
        b5.config(state=DISABLED, bg='red')
        b6.config(state=DISABLED)
        b7.config(state=DISABLED)
        b8.config(state=DISABLED)
        b9.config(state=DISABLED, bg='red')
        messagebox.showinfo('YEAH!', 'Player '+b+' Won!')
    elif board[0][2]==a and board[1][1]==a and board[2][0]==a:
        print("Player",a,"Wins!")
        b1.config(state=DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED, bg='red')
        b4.config(state=DISABLED)
        b5.config(state=DISABLED, bg='red')
        b6.config(state=DISABLED)
        b7.config(state=DISABLED, bg='red')
        b8.config(state=DISABLED)
        b9.config(state=DISABLED)
        messagebox.showinfo('YEAH!', 'Player '+a+' Won!')
    elif board[0][2]==b and board[1][1]==b and board[2][0]==b:
        print("Player",b,"Wins!")
        b1.config(state=DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED, bg='red')
        b4.config(state=DISABLED)
        b5.config(state=DISABLED, bg='red')
        b6.config(state=DISABLED)
        b7.config(state=DISABLED, bg='red')
        b8.config(state=DISABLED)
        b9.config(state=DISABLED)
        messagebox.showinfo('YEAH!', 'Player '+b+' Won!')
    elif c==9:
        messagebox.showinfo('SOS', 'The Game Is Unplayable!')
        root.destroy()
        
        
root = Tk()
root.title("Tic Tac Toe")  
frame = Frame(root)
frame.pack()
p1 = Button(frame, width=5, height=2, text="O", font=("Courier", 10), command=lambda: chance('1'))
p1.grid(row=0, column=0)
l1 = Label(frame, text="CHOOSE PLAYER", font=("Courier", 10))
l1.grid(row=0, column=1)
p2 = Button(frame, width=5, height=2, text="X", font=("Courier", 10), command=lambda: chance('2'))
p2.grid(row=0, column=2)
b1 = Button(frame, width=10, height=5, command=lambda: play_check('1'), state=DISABLED)
b1.grid(row=1, column=0)
b2 = Button(frame, width=10, height=5, command=lambda: play_check('2'), state=DISABLED)
b2.grid(row=1, column=1)
b3 = Button(frame, width=10, height=5, command=lambda: play_check('3'), state=DISABLED)
b3.grid(row=1, column=2)
b4 = Button(frame, width=10, height=5, command=lambda: play_check('4'), state=DISABLED)
b4.grid(row=2, column=0)
b5 = Button(frame, width=10, height=5, command=lambda: play_check('5'), state=DISABLED)
b5.grid(row=2, column=1)
b6 = Button(frame, width=10, height=5, command=lambda: play_check('6'), state=DISABLED)
b6.grid(row=2, column=2)
b7 = Button(frame, width=10, height=5, command=lambda: play_check('7'), state=DISABLED)
b7.grid(row=3, column=0)
b8 = Button(frame, width=10, height=5, command=lambda: play_check('8'), state=DISABLED)
b8.grid(row=3, column=1)
b9 = Button(frame, width=10, height=5, command=lambda: play_check('9'), state=DISABLED)
b9.grid(row=3, column=2)
oc = b1.cget('bg')
root.mainloop()
