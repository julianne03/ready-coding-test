# 오름차순 정렬하여 이어서 출력한 뒤, 그 뒤에 모든 숫자 더한 값 출력

# ex. K1KA5CB7 => ABCKK13
input_s = input()

string_list = []
num_sum = 0

for s in input_s :
  if s.isalpha() :
    string_list.append(s)
  else :
    num_sum += int(s)

string_list.sort()

if num_sum != 0 :
  string_list.append(str(num_sum))

print(''.join(string_list))