sum_num = 0
new_num = 0
number = 0
count = 0
num = int(input('정수를 입력하시오 : '))
number = num
while True:
    sum_num = (number // 10) + (number % 10)
    new_num = ((number % 10)*10) + (sum_num % 10)
    number = new_num
    count += 1
    if number == num :
        break

print(count)