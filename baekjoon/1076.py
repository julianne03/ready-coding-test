input_ls = []
value_ls = []
color_table = ['black', 'brown', 'red', 
'orange', 'yellow', 'green', 'blue', 'violet',
'grey', 'white']

for i in range(3) :
  value = input()
  input_ls.append(value)

for l in input_ls :
  value_ls.append(color_table.index(l))

answer = int(str(value_ls[0]) + str(value_ls[1])) * (10 ** value_ls[2])

print(answer)