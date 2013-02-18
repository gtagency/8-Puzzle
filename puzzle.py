from Tkinter import *
from sys import exit
from time import sleep
from astar import *

class PuzzleApp:
    def __init__(self,master,puzzle,goalState):
        self.frame = Frame(master)
        self.frame.grid()
        self.title = Label(self.frame,text="8 Puzzle Simulation")
        self.title.grid(row=0,column=1)
        self.puzzle = puzzle
        self.goalState = goalState
        self.puzzlePieces = [[],[],[]]
        for i in range(len(puzzle)):
            for j in range(len(puzzle[0])):
                self.puzzlePieces[i].append(Canvas(self.frame,width=25,height=25))
                self.puzzlePieces[i][j].create_rectangle(0,0,25,25)
                if(puzzle[i][j] != 0):
                    self.puzzlePieces[i][j].create_text(12,12,text=puzzle[i][j])
                self.puzzlePieces[i][j].grid(row=i+1, column=j)
        self.button = Button(self.frame, text="Run simulation", command=self.run_simulation)
        self.button.grid(row=4,column=1)
    def run_simulation(self):
        actions = astar(self.puzzle,self.goalState,heuristic_evaluation)
        print actions
        for action in actions:
            self.update_puzzle(action)
            #sleep(0.5)
    def update_puzzle(self,puzzle):
        for i in range(len(self.puzzlePieces)):
            for j in range(len(self.puzzlePieces[0])):
                self.puzzlePieces[i][j].grid_forget()
        for i in range(len(puzzle)):
            for j in range(len(puzzle[0])):
                self.puzzlePieces[i][j] = Canvas(self.frame,width=25,height=25)
                self.puzzlePieces[i][j].create_rectangle(0,0,25,25)
                if(puzzle[i] != 0):
                    self.puzzlePieces[i][j].create_text(12,12,text=puzzle[i][j])
                self.puzzlePieces[i][j].grid(row=i+1, column=j)
        self.frame.update()
        sleep(0.5)
#examplePuzzle = [[2,1,6],[4,0,8],[7,5,3]]
examplePuzzle = [[1,3,4],[8,0,2],[7,6,5]]
goalState = [[1,2,3],[8,0,4],[7,6,5]]
root = Tk()
app = PuzzleApp(root,examplePuzzle,goalState)
root.mainloop()