#tic tac toe side project
#just for fun

import tkinter as tk


piece = [" "," "," "," "," "," "," "," "," "]
order = ['X','O','X','O','X','O','X','O','X']
plays = {0:' ',1:'',2:' ',3:'',4:'  ',5:'',6:' ',7:'',8:' '}

game = tk.Tk()
game.title("TIC TAC TOE")
game.geometry("400x360")

prompt = tk.Label(game, text = "PLAY TIC TAC TOE", font = ("arial, 10"))
prompt.grid(row = 0, column = 2)
board = []
count = 0

def checkWin():
    global count
    if((plays[0] == plays[1]) & (plays[0] == plays[2])): #first row
        prompt['text'] = str(plays[0]) + " wins!"
        
    elif((plays[0] == plays[3]) & (plays[3] == plays[6])): #first column
        prompt['text'] = str(plays[0]) + " wins!"
        
    elif((plays[1] == plays[4]) & (plays[1] == plays[7])): #second column
        prompt['text'] = str(plays[1]) + " wins!"
        
    elif((plays[2] == plays[5]) & (plays[5] == plays[8])): #third column
        prompt['text'] = str(plays[2]) + " wins!"
        
    elif((plays[3] == plays[4]) & (plays[4] == plays[5])): #second row
        prompt['text'] = str(plays[3]) + " wins!"
        
    elif((plays[6] == plays[7]) & (plays[8] == plays[7])): #third row
        prompt['text'] = str(plays[7]) + " wins!"
        
    elif((plays[0] == plays[4]) & (plays[4] == plays[8])): #top left to bot right diag
        prompt['text'] = str(plays[0]) + " wins!"
        
    elif((plays[2] == plays[6]) & (plays[4] == plays[6])): #bot left to top right 
        prompt['text'] = str(plays[2]) + " wins!"
        
    elif(count > 8):
        prompt['text'] = "It's a tie"
                  
    

def zero():
    global count
    print(plays[0])
    if(plays[0] == ' '):
        if(count < 8):
            plays[0] = order[count]
            board[0]['text'] = order[count]
            count = count+ 1
    checkWin()
            
def one():
    global count
    print(1)
    if(plays[1] == ''):
        if(count < 9):
            plays[1] = order[count]
            board[1]['text'] = order[count]
            count = count+ 1
    checkWin()
    
def two():
    global count
    if(plays[2] == ' '):
        if(count < 9):
            plays[2] = order[count]
            board[2]['text'] = order[count]
            count = count+ 1
    checkWin()
            
def three():
    global count
    if(plays[3] == ''):
        if(count < 9):
            plays[3] = order[count]
            board[3]['text'] = order[count]
            count = count+ 1
    checkWin()
            
def four():
    global count
    print(4)
    if(plays[4] == '  '):
        if(count < 9):
            plays[4] = order[count]
            board[4]['text'] = order[count]
            count = count+ 1
    checkWin()
            
def five():
    global count
    print(5)
    if(plays[5] == ''):
        if(count < 9):
            plays[5] = order[count]
            board[5]['text'] = order[count]
            count = count+ 1
    checkWin()
            
def six():
    global count
    print(6)
    if(plays[6] == ' '):
        if(count < 9):
            plays[6] = order[count]
            board[6]['text'] = order[count]
            count = count+ 1
    checkWin()
            
def seven():
    global count
    print(7)
    if(plays[7] == ''):
        if(count < 9):
            plays[7] = order[count]
            board[7]['text'] = order[count]
            count = count+ 1
    checkWin()
            
def eight():
    global count
    print(8)
    if(plays[8] == ' '):
        if(count < 9):
            plays[8] = order[count]
            board[8]['text'] = order[count]
            count = count+ 1
    checkWin()
            
    print(plays)

funcList = [zero, one, two, three, four, five, six, seven, eight]

x = -1


for i in range(3):
    for j in range(3):
        x = 1 + x
        board.append(tk.Button(game, text = piece[i + j], padx = 60, pady = 40, command = funcList[x]))
        board[-1].grid(row = i + 1, column = j + 1)
