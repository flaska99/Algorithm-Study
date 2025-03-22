# 이분 탐색은 정렬이 되어있다는 가정하에 가능함
# 현재 이분탐색은 오름차순으로 정렬 후에 할꺼임
# 그래서 필요한 함수는 ?

# 분할을 해야한다 (두개로)
# 찾을 수 = num, 찝은 수 인덱스 = pivot
# 조건 :
# 1. num < arr[pivot] :  arr =[:pivot],
# 2. num > arr[pivot] : arr = [pivot:],
# 3. num == arr[pivot] : return pivot


def devide(arr, num, idx) :
    mid = len(arr) // 2
    idx += mid # 가운데 값을 리턴함으로 인덱스는 mid로 설정
    new_arr = []

    if num == arr[mid] :
        return idx
    
    elif len(arr) == 1:
        return '찾을 수 없음'
    
    if num < arr[mid] : 
        new_arr = arr[:mid]
        idx -= mid # 만약 mid보다 작은 곳에 있다면 인덱스를 뺴줌
    else : 
        new_arr = arr[mid:]

    return devide(new_arr, num, idx) #재귀로 인덱스값을 계속 중첩

num_list = [1,2,3,4,5,6,7,8,9,24,34,534,2]
t = 42
print(f'우리가 찾을 num의 인덱스는 {devide(num_list, t, 0)} 입니다.')