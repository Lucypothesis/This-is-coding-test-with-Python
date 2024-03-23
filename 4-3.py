input = input()
x = int(input[1])
list = 'abcdefgh'
y = list.index(input[0]) + 1

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]
count = 0

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1
print(count)