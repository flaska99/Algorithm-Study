def quicksort(arr, low, high):
    # 재귀 종료 조건: 정렬할 구간의 길이가 0 또는 1이면 이미 정렬된 상태
    if low >= high:
        return

    # 중앙값을 피벗으로 선택: 현재 부분 배열의 중간 인덱스의 값을 피벗으로 사용
    pivot = arr[(low + high) // 2]

    # pl은 왼쪽에서 시작, pr은 오른쪽에서 시작
    pl = low
    pr = high

    # pl과 pr이 서로 교차할 때까지 반복하며 요소들을 피벗을 기준으로 분할
    while pl <= pr:
        # 왼쪽에서부터 시작해서 피벗보다 작은 원소들은 그대로 두기 위해,
        # arr[pl]이 피벗보다 작으면 올바른 위치에 있으므로 pl을 오른쪽으로 이동
        while arr[pl] < pivot:
            pl += 1

        # 오른쪽에서부터 시작해서 피벗보다 큰 원소들은 그대로 두기 위해,
        # arr[pr]이 피벗보다 크면 올바른 위치에 있으므로 pr을 왼쪽으로 이동
        while arr[pr] > pivot:
            pr -= 1

        # 만약 pl과 pr이 아직 교차하지 않았다면, 
        # 두 포인터가 가리키는 원소는 서로 잘못된 위치에 있으므로 교환
        if pl <= pr:
            arr[pl], arr[pr] = arr[pr], arr[pl]
            # 교환한 후, pl은 오른쪽으로, pr은 왼쪽으로 이동시킴
            pl += 1
            pr -= 1
    
    # 여기까지 오면 배열은 두 부분으로 분할됨:
    #   - low ~ pr: 피벗보다 작거나 같은 값들
    #   - pl ~ high: 피벗보다 큰 값들
    # 재귀 호출: 왼쪽 부분과 오른쪽 부분에 대해 각각 정렬 수행
    quicksort(arr, low, pr)
    quicksort(arr, pl, high)
   

# 예제 배열
arr = [3, 6, 2, 9, 5, 1, 7, 8, 4]

# 배열 전체에 대해 퀵소트 실행 (인덱스 0부터 len(arr)-1)
quicksort(arr, 0, len(arr) - 1)

print("Sorted array:", arr)




