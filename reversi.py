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

# xが行、yが列

    # 置く石の周囲を検索するメソッド
    # def check(self, y, x, color):
    #     # NONE以外ならば、False
    #     if self.cells[x][y] != NONE :
    #         return False
    #     tmp = []
    #     for i in range(8):
    #         for j in range(8):
    #             if 0 <= x+i < 8 and 0 <= y+j < 8 :
    #                 if self.cells[x + i][y+j] == color :
    #                     if tmp != [] :
    #                         # 石をひっくり返す処理
    #                         print('石をひっくり返す処理')
    #                 elif self.cells[x + i][y+j] == NONE :
    #                     break
    #                 else :
    #                     # 獲得できるかもしれない石を一時保存
    #                     tmp.append((x+i, y+j))

    def check(x, y, dir_x, dir_y, color) :

        # 置く石の色
        put_stone = WHITE if color == WHITE else BLACK

        # 隣接する場所へ
        x += dir_x
        y += dir_y

        # 盤面外ならばfalse
        if x < 0 or 8 <= x or y < 0 or 8 <= y :
            return False
        
        # 置く石と隣が一緒だったならばFalse
        if self.cells[x][y] == put_stone :
            return False
        
        # 隣が空白ならばFalse
        if self.cells[x][y] == NONE :
            return False
        
        # さらに隣を調べる
        x += dir_x
        y += dir_y


    # 石を置くメソッド
    def put(self, y, x):
        if self.cells[x][y] == NONE :
            if self.check(y, x, WHITE) == True :
                self.cells[x][y] = WHITE
        else :
            print('すでに石が置かれています。')

board = Reversi()
board.call()
# while True :
y, x = [int(i) for i in input().split()]
board.put(y, x)
board.call()
