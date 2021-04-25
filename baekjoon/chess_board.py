li = ['.F.F...F', 'F...F.F.', '...F.F.F', 
  'F.F...F.', '.F...F..', 'F...F.F.', '.F.F.F.F',
  '..FF..F.'
]

white_count = 0
row_count = 0
for l in li :
  for i in range(8) :
    # 짝수 번 째 row 일 때
    if row_count % 2 == 0 :
      if i % 2 == 0 and l[i] == 'F' :
        white_count += 1
    # 홀수 번째 row 일 때
    else :
      if i % 2 != 0 and l[i] == 'F' :
        white_count += 1
  row_count += 1

print(white_count)