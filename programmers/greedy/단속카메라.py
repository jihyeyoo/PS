def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1]) # 진출 지점 기준으로 정렬
    camera = -30001 # 차량의 최소 진입 지점

    for start in routes:
        if camera < start[0]: # 아직 카메라를 만나지 못함
            answer += 1 # 카메라 추가 설치
            camera = start[1]
    return answer
