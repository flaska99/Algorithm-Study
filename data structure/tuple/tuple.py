tuple_1 = 1, # 튜플은 항상 쉼표가 들어가야함
tuple_2 = 1 # 해당 자료형은 튜플이 아닌 int로 인식

tuple_1 += 1,2,3 # (1, 1, 2, 3)
# TypeError: unsupported operand type(s) for +=: 'int' and 'tuple'
#tuple_2 += 1,2,3 # 위와 같이 타입에러가 남

tuple_1 = {1,2,3,4,5,5} # 집합도 들어간다
#output: {1, 2, 3, 4, 5}

# 여기서 집합이란 

# set() 함수로 만들수도 있고 중괄호로 만들수도있음
tuple_1 = 1,2,3,4,5,6,6,6
#output : (1, 2, 3, 4, 5, 6, 6, 6)
tuple_1 = set(tuple_1)
#output : {1, 2, 3, 4, 5, 6}

#리스트나 튜플 같은 경우는 인덱스로 접근이 가능
print(tuple_1[0]) # output : 1

# 하지만 set을 이용하여 집합으로 만들었다면 불가능하다.
# 왜 ? set은 순서가 없는 자료형이라서 인덱스로 접근이 불가능
