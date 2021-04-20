# 8 x 8
# L자 방법 : 가로로 x 2 + 세로로 x 1
# 2번째 방법 : 세로로 x 2 + 가로로 x 1

# 입력 : a1 -> 출력 : 2

direction = input()

row = int(direction[1])
column = ord(direction[0]) - ord('a') + 1

move = [[-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1], [-2, 1], [-2, -1]]

answer = 0

for i in range(len(move)) :
  new_row = row + move[i][0]
  new_column = column + move[i][1]

  if new_row >= 1 and new_row <= 8 and new_column >= 1 and new_column <= 8 :
    answer += 1

print(answer)
