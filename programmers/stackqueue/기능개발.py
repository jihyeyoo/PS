def solution(progresses, speeds):
    answer = list()
    
    while progresses:
        count = 0 
        progresses = [ i + j for i, j in zip(progresses, speeds) ]

        for i in progresses:
            if i < 100:
                break
            else:
                count += 1
        if count > 0:
            answer.append(count)
            for _ in range(count):
                speeds.pop(0), progresses.pop(0)

    return answer
