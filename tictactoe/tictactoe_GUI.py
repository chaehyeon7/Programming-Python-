import tkinter
from tkinter import messagebox

from tictactoe_gameengine import TictactoeGameEngine

class TictactoeGUI:
    def __init__(self):
        self.game_engine = TictactoeGameEngine()
        self.init_GUI()

    def init_GUI(self):
        self.CANVAS_SIZE = 300
        self.root = tkinter.Tk()
        self.root.title('틱택토')
        self.root.geometry(f'{self.CANVAS_SIZE}x{self.CANVAS_SIZE}')  # 문자열
        self.root.resizable(width=False, height=False)

        self.canvas = tkinter.Canvas(self.root, bg='white', width=self.CANVAS_SIZE, height=self.CANVAS_SIZE)
        self.canvas.pack()

        self.images = {}  # {'X' : PhotoImage 객체, 'O' : PhotoImage 객체}
        self.images['X'] = tkinter.PhotoImage(file='X.gif')
        self.images['O'] = tkinter.PhotoImage(file='O.gif')

        self.canvas.bind('<Button-1>', self.click_handler)  # ***

        self.root.mainloop()

    def click_handler(self, event):
        row, col = self.coordinate_to_position(event.x, event.y)
        # set row, col
        self.game_engine.set(row, col)
        # show board
        self.game_engine.show_board()
        # set winner
        winner = self.game_engine.set_winner()
        # 승자가 있거나 무승부면, 게임오버, 결과 표시하자
        if winner == 'O' or winner == 'X':
            messagebox.showinfo('Game Over', f'{winner} 이김!!✨')
        elif winner == 'd':
            messagebox.showinfo('Game Over', '무승부!!')
            self.root.quit()
        # change_turn
        self.game_engine.change_turn()

    def draw_board(self):
        pass

    def coordinate_to_position(self, x, y):
        # row
        # if 0 <= y <100:
        #     row = 1
        # elif 100 <= y < 200:
        #     row = 2
        # elif 200 <= y < 300:
        #     row = 3
        #
        # # col
        # if 0 <= x <100:
        #     row = 1
        # elif 100 <= x < 200:
        #     row = 2
        # elif 200 <= x < 300:
        #     row = 3
        #
        # return row, col

        # return int(y/100)+1, int(x/100)+1

        return y//(self.CANVAS_SIZE // self.game_engine.SIZE) + 1, x // (self.CANVAS_SIZE // self.game_engine.SIZE) +1
if __name__ == '__main__':
    ttt_GUI = TictactoeGUI()