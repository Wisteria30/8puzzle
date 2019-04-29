from collections import deque
from copy import deepcopy
import time

# S = [1, 2, 3, 0, 4, 5, 6, 7, 8]
# G = [1, 2, 3, 4, 0, 5, 6, 7, 8]


# 0探索
def search_zero(l):
    for i in l:
        if i == 0:
            return l.index(i)


def bfs(s, g):
    # 探索済みかどうか状態をログでとる
    log = {}
    S_dash = deepcopy(s)
    # 上下左右に行く時の配列移動
    up_down_left_right = [-3, 3, -1, 1]
    que = deque()
    g_tuple = tuple(g)
    log[tuple(S_dash)] = 1
    que.append(S_dash)

    while not (len(que) == 0):
        ss = que.popleft()
        ss_tuple = tuple(ss)
        zero = search_zero(ss)
        for i in range(4):
            # 左端だったら左にはいけない
            if zero % 3 == 0 and i == 2:
                continue
            # 右端だったら右にはいけない
            if zero % 3 == 2 and i == 3:
                continue
            point = zero + up_down_left_right[i]
            # 上限・下限は超えない
            if point < 0 or point > 8:
                continue
            # シャローコピーをせずに0からスワップ
            S_dash_dash = deepcopy(ss)
            swap = S_dash_dash[point]
            S_dash_dash[point] = 0
            S_dash_dash[zero] = swap
            S_dd_tuple = tuple(S_dash_dash)
            # 過去に探索したことがあるかログを探索する。なければログとキューに追加する。
            if log.get(S_dd_tuple) is None:
                log[S_dd_tuple] = log[ss_tuple] + 1
                que.append(S_dash_dash)
            # ゴールに訪問していれば終了
            if log.get(g_tuple) is not None:
                return log[g_tuple]

    return -1


if __name__ == "__main__":
    start = time.time()
    S = list(map(int, input().split()))
    G = list(map(int, input().split()))
    print(bfs(S, G))
    elapsed_time = time.time() - start
    print("elapsed_time:{0}".format(elapsed_time) + "[sec]")
