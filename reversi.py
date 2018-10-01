# 石
NONE = 0
WHITE = 1
BLACK = 2

# 周囲8方向の座標
search_list = [[-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0]]

# リバーシクラス
class Reversi(object):
# 盤面を生成するコンストラクタ
    def __init__(self):
        # 盤面を初期化
        self.cells = [[0 for i in range(8)] for j in range(8)]

        # 石を初期配置する
        self.cells[3][3] = BLACK
        self.cells[3][4] = WHITE
        self.cells[4][3] = WHITE
        self.cells[4][4] = BLACK

    # 現在の盤面を描画するメソッド
    def call(self):
        print('--------------------------')
        for i in range(8):
                for j in range(8):
                    print('|', end = '')

                    if self.cells[i][j] == WHITE :
                        print('○ ', end = '')
                    elif self.cells[i][j] == BLACK :
                        print('● ', end = '')
                    else :
                        print('　', end = '')

                print('|')
        print('--------------------------')

# columnが行、rowが列

    # 置く石の周囲を検索するメソッド
    def check(self, row, column, color):
        # NONE以外ならば、False
        if self.cells[column][row] != NONE :
            return False
        tmp = []
        for i in range(8):
            for j in range(8):
                if 0 <= column+i < 8 and 0 <= row+j < 8 :
                    if self.cells[column + i][row+j] == color :
                        if tmp != [] :
                            # 石をひっくり返す処理
                            print('石をひっくり返す処理')
                    elif self.cells[column + i][row+j] == NONE :
                        break
                    else :
                        # 獲得できるかもしれない石を一時保存
                        tmp.append((column+i, row+j))
                    

    # 石を置くメソッド
    def put(self, row, column):
        if self.cells[column][row] == NONE :
            if self.check(row, column, WHITE) == True :
                self.cells[column][row] = WHITE
        else :
            print('すでに石が置かれています。')

for i in search_list:
    for j in i :
        print(j)

board = Reversi()
board.call()
# while True :
row, column = [int(i) for i in input().split()]
board.put(row, column)
board.call()
