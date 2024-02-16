# 먹을 물고기를 결정하는 것이 핵심
# 4. 상어에게 가장 가까운 위치에 있는 물고기를 우선순위로 먹어야 한다. -> 최단경로 알고리즘인듯
# 5. 여러마리가 가까이에 있다면, 가장 위쪽에 있는 물고기 (ft.행), 그 다음 순서로 가장 왼쪽에 있는 물고기(ft.열)를 우선순위로 먹어야 한다.
# -> 4, 5번때문에 minheap에 (이동거리, 행좌표, 열좌표)를 push하는 것
# 6. 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때마다 크기가 1 증가한다.

from sys import stdin
from heapq import heappush, heappop
input = stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
q = []

def init():
    for i in range(n):
        for j in range(m):
            if a[i][j] == 9:
                sx, sy = i, j

#x, y는 아기상어의 위치
def dijkstra(x, y):
    q = []
    heappush(q, (0, (x, y))) #이코테도 그렇고 (최단거리, 노드) 순으로 heappush한다
    
    while q:
        dist, now = heappop(q)
        
