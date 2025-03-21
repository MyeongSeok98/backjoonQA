import sys

if __name__ == '__main__':
    N, C = map(int, input().split())
    
    router = list(int(input()) for _ in range(N))
    router.sort()
    ## 최소거리는 1부터
    start = 1
    ## 최대거리는 맨 마지막 라우터 - 맨 처음 라우터
    end = router[N-1] - router[0]


    while start <= end:
        # 중간거리 구하기
        mid = (start + end) // 2
        # print(f"mid가 {mid} 일 때")
        # 첫 라우터는 처음에 넣으니 cnt 1부터 시작
        cnt = 1
        # 첫라우터 설치
        current_cordinate = router[0]

        for i in range(1, len(router)):
            #다음 라우터가 전라우터 위치 + 중간위치보다 크면
            if router[i] >= current_cordinate + mid:
                cnt+=1
                # 현재 라우터 위치로 변수변경
                current_cordinate = router[i]
                # print(f"current_cordinate : {current_cordinate}")
        
        # 설치한 공유기 수 cnt가 c이상이면
        # mid 값을 좀더 크게 설정해야하므로 
        if cnt >= C:
            start = mid+1
        # 설치한 공유기 수 cnt가 c보다 작으면
        # mid가 너무 크므로 end = mid -1
        else:
            end = mid - 1
    print(end)


    