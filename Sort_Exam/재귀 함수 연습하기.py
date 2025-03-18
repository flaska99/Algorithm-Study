def fibo(n) :
    if n <= 0 : return []
    elif n == 1 : return [1]
    elif n == 2 : return [1, 1]

    else :
        arr = fibo(n - 1)
        arr.append(arr[-1] + arr[-2])
    return arr    


#바로 위에 함수 for 문으로 구현시시
def fibo_loop(n) :
    if n <= 0 : return []
    elif n == 1 : return [1]
    elif n == 2 : return [1, 1]

    arr = [1,1]

    for i in range(2, n) :
        arr.append(arr[i - 2] + arr[i - 1])
    
    return arr

num = int(input())

list = fibo(num)
print(list)

list_2 = fibo_loop(num)
print(list_2)


