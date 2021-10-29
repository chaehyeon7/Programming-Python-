class TictactoeGameEngine:
    def __init__(self):
        self.board = list('.' * 9) # ['.','.','.','.','.','.','.','.','.']

    def show_board(self):
        pass
    def __set__(self, row, col):
        pass
    def set_winner(self):
        # - 3줄
        # | 3줄


        # /
        # \
        # 무승부: 위의 조건 다 통과, 더 이상 놓을 자리가 없음: self.board에 빈칸이 없음: slef.board에 '.' 없음
        return 'd' # draw

        pass
    def change_turn(self):
        pass

if __name__ == '__main__':
    game_engine = TictactoeGameEngine()
    game_engine.show_board()        #...\n...\n
    game_engine.ser(2,2)
    game_engine.show_board()        # ['.','.','.','.','X','.','.','.','.']
    game_engine.ser(2,1)
    game_engine.ser(2,3)
    game_engine.show_board()        # ['.','.','.','.','X','X','X','.','.']
    game_engine.board = ['.','.','.','X','X','X','.','.','.']
    game_engine.set_winner()    # '_' -> 'x'
    game_engine.change_turn()
    print(game_engine.turn)     # 'o'
    game_engine.change_turn()
    print(game_engine.turn)     # 'x'

