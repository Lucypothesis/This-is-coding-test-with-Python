N = int(input())
list = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L', 'R', 'U', 'D']

x, y = 1, 1
for i in list:
    for j in range(len(move_types)):
        if i == move_types[j]:
            nx = x + dx[j]
            ny = y + dy[j]
            if 1 <= nx <= N and 1 <= ny <= N:
                x, y = nx, ny
print(x,y)