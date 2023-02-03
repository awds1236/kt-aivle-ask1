def solution(lottos, win_nums):
    answer = []
    num_count = 0
    zero_count = 0
    minimum = 0
    maximum = 0
    
    for i in lottos:
        for j in win_nums:
            if i == j:
                num_count += 1
        if i == 0:
            zero_count += 1
    
    minimum = num_count
    maximum = num_count + zero_count
    
    if maximum <= 1:
        answer.append(6)
    else :
        answer.append(7-maximum)
    
    if minimum <= 1:
        answer.append(6)
    else :
        answer.append(7-minimum)
        
    return answer

lottos = [0, 0, 0, 0, 0, 0]
win_nums = [38, 19, 20, 40, 15, 25]
answer = solution(lottos, win_nums)
print(answer)