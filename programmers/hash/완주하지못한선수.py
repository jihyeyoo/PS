from collections import defaultdict

def solution(participant, completion):
    answer = ''
    
    arr = defaultdict(int)
    
    # 1
    for i in completion:
        arr[i]+=1
        
    # 2
    for i in participant:
        arr[i] -=1
        if arr[i] < 0:
            answer = i
    
    return answer
