from collections import deque
from copy import deepcopy

# S = [1, 2, 3, 0, 4, 5, 6, 7, 8]
# G = [1, 2, 3, 4, 0, 5, 6, 7, 8]


# 0探索
def search_zero(l):
    for i in l:
        if i == 0:
            return l.index(i)


# 9個の要素が全て等しければTrue, 1つでも違えばFalseを返す
def check_state(state, state_dash):
    return all([state[i] == state_dash[i] for i in range(9)])


def bfs(s, g):
    # 探索済みかどうか状態をログでとる
    log = []
    # 10番目の要素に移動回数を付与する(比較はそれより前の9要素)
    s.append(1)
    S_dash = deepcopy(s)
    # 上下左右に行く時の配列移動
    up_down_left_right = [-3, 3, -1, 1]
    que = deque()
    log.append(S_dash)
    que.append(S_dash)

    while not (len(que) == 0):
        ss = que.popleft()
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
            # 過去に探索したことがあるかログを探索する。なければログとキューに追加する。
            if not any([check_state(S_dash_dash, l) for l in log]):
                S_dash_dash[9] += 1
                que.append(S_dash_dash)
                log.append(S_dash_dash)
            # ゴールと状態が等しければ探索までの長さを返して終了
            if check_state(S_dash_dash, g):
                return S_dash_dash[9]
    return -1


if __name__ == "__main__":
    S = list(map(int, input().split()))
    G = list(map(int, input().split()))
    print(bfs(S, G))
