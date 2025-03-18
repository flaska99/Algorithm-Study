# 삽입 정렬이란 ?
# 숫자들을 하나씩 비교하며 적절한 위치에 삽입하는 정렬
# 값을 하나 뽑고 그 값보다 작은 인덱스와 계속해서 비교함
# 그 숫자보다 큰 값이 나온다면 그 앞에 삽입
def insertion_sort(arr) :
    n = len(arr)

    for i in range(1, n) :
        key = arr[i]
        j = i - 1

        while j >=0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key



arr = [4,2,5,3,1]
insertion_sort(arr)
print(arr)