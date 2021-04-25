# N x M
# 한 칸은 육지 or 바다
def turn_left(direction) :
  direction -= 1
  if direction == -1 :
    direction = 3
  return direction
  
row_num, col_num = map(int, input().split())

went_list = [[0] * col_num for _ in range(row_num)]

cx, cy, direction = map(int, input().split())
went_list[cx][cy] = 1

map_list = []

for i in range(row_num) :
  map_list.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 1
turn_time = 0
while True :
  # 왼쪽으로 돌고
  direction = turn_left(direction)
  # 차례대로 왼쪽부터 돌면서 1인지 0인지 확인
  for i in range(4) :
    new_row = cx + dx[i]
    new_col = cy + dy[i]
    if map_list[new_row][new_col] == 0 and went_list[new_row][new_col] == 0 :
      count += 1
      turn_time = 0
      went_list[new_row][new_col] = 1
      cx = new_row
      cy = new_col
      continue
    else :
      # 0이면 그 인덱스 +1 or -1 / 1이면 continue
      turn_time += 1
  # 1의 개수가 4이면 (다 돌았는데 다 1이면) 뒤로 가기
  if turn_time == 4 :
    new_row = cx - dx[i]
    new_col = cy - dy[i]
    if map_list[new_row][new_col] == 0 :
      cx = new_row
      cy = new_col
  else :
    # 뒤로 갔는데도 다 1이면 멈춰!
    break
  turn_time = 0

print(count)