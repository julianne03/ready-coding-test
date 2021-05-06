import sys
num = int(sys.stdin.readline())
a = []

for i in range(num) :
  input_text = sys.stdin.readline().split()
  if input_text[0] == 'push':
    a.append(input_text[1])
  elif input_text[0] == 'pop' :
    if len(a) != 0 :
      print(a.pop())
    else :
      print(-1)
  elif input_text[0] == 'size' :
    print(len(a))
  elif input_text[0] == 'empty' :
    if len(a) == 0 :
      print(1)
    else :
      print(0)
  if input_text[0] == 'top' :
    if len(a) != 0 :
      print(a[-1])
    else :
      print(-1)
  