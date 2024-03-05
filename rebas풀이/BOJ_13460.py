def init():
    _rx, _ry, _bx, _by = [0]*4 #왜 이렇게 하는거징
    for i in range(n):
        for j in range(m):
            if a[i][j] == 'R':
                _rx, _ry = i, j
            elif a[i][j] == 'B':
                _bx, _by = i, j
    q.append((_rx, _ry, _bx, _by, 0))
    check[_rx][_ry][_bx][_by] = True

def move(_x, _y, _dx, _dy, _c):
    while a[_x+_dx][_y+_dy] != '#' and a[_x][_y] != 'O':
        _x += _dx
        _y += _dy
        _c += 1
    return _x, _y, _c