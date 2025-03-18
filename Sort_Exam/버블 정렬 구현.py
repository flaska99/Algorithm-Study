# 버블 정렬이란 ? 
# 코드가 반복하며 배열의 원소가 뒷쪽으로 밀려나는 모습이
# 마치 거품이 떠오르는 모습과 같다고 해서 붙여진 이름이다.
# 간단해서 사용함.
# 시작복잡도는 O(N^2) 이다.

def bubble_sort(arr) :
    n = len(arr)

    for i in range(n-1, 0, -1) : # 4 3 2 1 
        print(i)
        for j in range(i):  # 루프 횟수 5 4 3 2 1
            print(j)
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
        
arr = [4,2,5,3,1]

bubble_sort(arr)
print(arr)