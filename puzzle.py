from Tkinter import *
from sys import exit
from time import sleep
from astar import *

class PuzzleApp:
    def __init__(self,master,puzzle,goalState):
        self.frame = Frame(master)
        self.frame.grid()
        self.title = Label(self.frame,text="8 Puzzle")
        self.title.grid(row=0,column=1)
        self.goalTitle = Label(self.frame,text="Goal State")
        self.goalTitle.grid(row=0,column=4)
        self.puzzle = puzzle
        self.goalState = goalState
        self.puzzlePieces = [[],[],[]]
        self.goalPieces = [[],[],[]]
        for i in range(len(puzzle)):
            for j in range(len(puzzle[0])):
                self.puzzlePieces[i].append(Canvas(self.frame,width=25,height=25))
                self.puzzlePieces[i][j].create_rectangle(2,2,25,25, fill="red")
                if(puzzle[i][j] != 0):
                    self.puzzlePieces[i][j].create_text(12,12,text=puzzle[i][j])
                    self.puzzlePieces[i][j].bind('<ButtonPress-1>', self.on_puzzle_click)
                self.puzzlePieces[i][j].grid(row=i+1, column=j)
                self.goalPieces[i].append(Canvas(self.frame,width=25,height=25))
                self.goalPieces[i][j].create_rectangle(2,2,25,25,fill="blue")
                if(goalState[i][j] != 0):
                    self.goalPieces[i][j].create_text(12,12,text=goalState[i][j])
                    self.goalPieces[i][j].bind('<ButtonPress-1>', self.on_goal_click)
                self.goalPieces[i][j].grid(row=i+1, column=j+3)
        self.button = Button(self.frame, text="Run algorithm", command=self.run_simulation)
        self.button.grid(row=4,columnspan=6)
    def run_simulation(self):
        actions = astar(self.puzzle,self.goalState,heuristic_evaluation)
        print actions
        for action in actions:
            self.update_puzzle(action)
    def update_puzzle(self,puzzle):
        for i in range(len(puzzle)):
            for j in range(len(puzzle[0])):
                self.puzzlePieces[i][j].grid_forget()
                self.puzzlePieces[i][j] = Canvas(self.frame,width=25,height=25)
                self.puzzlePieces[i][j].create_rectangle(2,2,25,25,fill="red")
                if(puzzle[i][j] != 0):
                    self.puzzlePieces[i][j].create_text(12,12,text=puzzle[i][j])
                    self.puzzlePieces[i][j].bind('<ButtonPress-1>', self.on_puzzle_click)
                self.puzzlePieces[i][j].grid(row=i+1, column=j)
        self.frame.update()
        sleep(0.5)
        self.puzzle = puzzle
    def update_goal(self,goalState):
        for i in range(len(goalState)):
            for j in range(len(goalState)): 
                self.goalPieces[i][j].grid_forget()
                self.goalPieces[i][j] = Canvas(self.frame,width=25,height=25)
                self.goalPieces[i][j].create_rectangle(2,2,25,25,fill="blue")
                if(goalState[i][j] != 0):
                    self.goalPieces[i][j].create_text(12,12,text=goalState[i][j])
                    self.goalPieces[i][j].bind('<ButtonPress-1>', self.on_goal_click)
                self.goalPieces[i][j].grid(row=i+1, column=j+3)
        self.frame.update()
        self.goalState = goalState
    def on_puzzle_click(self,event):
        for i in range(len(self.puzzlePieces)):
            for j in range(len(self.puzzlePieces[0])):
                if(self.puzzle[i][j] == 0):
                    zeroi = i
                    zeroj = j
                if(self.puzzlePieces[i][j] == event.widget):
                    piecei = i
                    piecej = j
        if((abs(zeroi-piecei) == 1 and abs(zeroj - piecej) == 0) or (abs(zeroi-piecei) == 0 and abs(zeroj - piecej) == 1)):
            self.puzzle[zeroi][zeroj] = self.puzzle[piecei][piecej]
            self.puzzle[piecei][piecej] = 0
            self.update_puzzle(self.puzzle)
    def on_goal_click(self,event):
        for i in range(len(self.goalState)):
            for j in range(len(self.goalState[0])):
                if(self.goalState[i][j] == 0):
                    zeroi = i
                    zeroj = j
                if(self.goalPieces[i][j] == event.widget):
                    piecei = i
                    piecej = j
        if((abs(zeroi-piecei) == 1 and abs(zeroj - piecej) == 0) or (abs(zeroi-piecei) == 0 and abs(zeroj - piecej) == 1)):
            self.goalState[zeroi][zeroj] = self.goalState[piecei][piecej]
            self.goalState[piecei][piecej] = 0
            self.update_goal(self.goalState)

examplePuzzle = [[2,1,6],[4,0,8],[7,5,3]]
goalState = [[1,2,3],[8,0,4],[7,6,5]]
root = Tk()
app = PuzzleApp(root,examplePuzzle,goalState)
root.mainloop()