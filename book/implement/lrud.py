n = 5
x = 1
y = 1

move = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

move_type = ['L', 'R', 'U', 'D']

for m in move :
  for i in range(len(move_type)) :
    if m == move_type[i] :
      nx = x + dx[i]
      ny = y + dy[i]
  if nx < 1 or ny < 1 or nx > n or ny > n :
    continue
  x, y = nx, ny

print(x,y)

