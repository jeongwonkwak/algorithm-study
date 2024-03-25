from collections import deque
from copy import deepcopy
from itertools import combinations
from sys import stdin
from typing import List


def bfs(graph: List[int]) -> None:
    q = deque([(j, i) for i in range(N) for j in range(M) if graph[i][j] == 2])
    while q:
        x, y = q.popleft()
        for nx, ny in zip([x + 1, x - 1, x, x], [y, y, y + 1, y - 1]):
            if 0 <= nx < M and 0 <= ny < N and not graph[ny][nx]:
                graph[ny][nx] = 2
                q.append((nx, ny))
