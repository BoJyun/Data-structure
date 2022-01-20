# 迷宮
maze = [[0, 0, 1, 0],
        [0, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1]]

next = [[0, 1],
        [1, 0],
        [0, -1],
        [-1, 0]]


class note():
    def __init__(self, n, m):
        self.x = [0]*n*m
        self.y = [0]*n*m
        self.f = [0]*n*m
        self.s = [0]*n*m


n = len(maze)
m = len(maze[0])

book = []
for i in range(n):
    book.append([0]*m)

start_x = 0
start_y = 0
end_x = 3
end_y = 2

head = 0
tail = 0

que = note(n, m)
que.x[tail] = start_x
que.y[tail] = start_y
que.f[tail] = 0
que.s[tail] = 0
flag = 0

tail += 1
book[start_x][start_y] = 1

while head < tail:
    for i in range(4):
        print(que.x[head], que.y[head])
        tx = que.x[head]+next[i][0]
        ty = que.y[head]+next[i][1]

        if tx >= n or tx < 0 or ty >= m or ty < 0:
            continue

        if book[tx][ty] == 0 and maze[tx][ty] == 0:
            book[tx][ty] = 1
            que.x[tail] = tx
            que.y[tail] = ty
            que.f[tail] = head
            que.s[tail] = que.s[head]+1
            tail += 1

        if tx == end_x and ty == end_y:
            flag = 1
            break
    if flag == 1:
        break
    head += 1


print(que.s[tail-1])
print(que.x)
print(que.y)

#BFS and Quene


class Quene():
    def __init__(self):
        self.arr = []

    def pop(self):
        return self.arr.pop()

    def add(self, n):
        self.arr.append(n)
