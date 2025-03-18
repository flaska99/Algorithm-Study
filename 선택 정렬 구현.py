#배열의 첫 인덱스부터 끝 인덱스까지 중
#가장 작은 배열을 찾아서 가장 작은 배열이 찾아지면 
#첫 인덱스와 교환
#이후 인덱스를 늘려가며 계속해서 작은값을 찾으면 교환을 실행한다.
#이때 중요한 점은 한 스텝당 교환은 한번만 일어난다.
#그리고 정렬이 완료된 인덱스는 더이상 검사하지않는다

def selection_sort(arr) :
    n = len(arr)
    for i in range(n-1) :
        min_idx = i 
        for j in range(i+1, n) :
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]    



arr = [4,2,5,3,1]
selection_sort(arr)
print(arr)