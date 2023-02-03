data = input('숫자로 이루어진 문자열을 입력하세요. ')
       
data = int(data)
data = str(data)

result = 1

for a in range(0, len(data)) :
    if int(data[a]) == 0 :
        result = result + int(data[a])
    else :
        result = result * int(data[a])

print(result)