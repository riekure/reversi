# 石
NONE = 0
WHITE = 1
BLACK = 2

# 周囲8方向の座標
search_list = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]

# リバーシクラス
class Reversi(object):
# 盤面を生成するコンストラクタ
    def __init__(self):
        # 盤面を初期化
        self.cells = [[0 for i in range(8)] for j in range(8)]
        self.player = BLACK

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

    # 石が打てるか探索するメソッド①
    def check(self, x, y) :

        # 盤面外ならばFalse
        if x >= 8 or y >= 8 :
            return False
        
        # すでに石があったらFalse
        if self.cells[x][y] != NONE :
            return False
        
        # 8方向チェック
        for dir in search_list :
            if self.check_dir(x, y, dir[0], dir[1], self.player) :
                return True
        
        # 8方向すべて該当なしならばFalse
        return False


    # 石が打てるか探索するメソッド②
    def check_dir(self, x, y, dir_x, dir_y, color) :

        # 隣接する場所へ
        x += dir_x
        y += dir_y

        # 盤面外ならばfalse
        if x < 0 or 8 <= x or y < 0 or 8 <= y :
            return False
        
        # 置く石と隣が一緒だったならばFalse
        if self.cells[x][y] == color :
            return False
        
        # 隣が空白ならばFalse
        if self.cells[x][y] == NONE :
            return False
        
        # さらに隣を調べる
        x += dir_x
        y += dir_y

        # 隣に石があるならばループし続ける
        while x >= 0 and x < 8 and y >= 0 and y < 8 :
            # 空白ならば挟めないのでFalse
            if self.cells[x][y] == NONE :
                return False
            # 自分の石があればTrue
            if self.cells[x][y] == color :
                return True
            
            x += dir_x
            y += dir_y

        # 相手の石しかないならFalse
        return False

    # 石を置くメソッド
    def put(self, x, y):

        if self.check(x, y) :
            self.cells[x][y] = self.player
            
            if self.player == BLACK :
                self.player = WHITE
            else :
                self.player = BLACK

        else :
            print(self.player)
            print('指定された場所に石は置けません。')

board = Reversi()
board.call()

while True :
    y, x = [int(i) for i in input().split()]
    board.put(x, y)
    board.call()
