class stack:
#push | 매개변수 : self, value
#pop | 매개변수 : self
    def __init__(self, max_size):
        self.items = []
        self.max_size = max_size
    
    def push(self, value) :
        if self.is_full():
            print("스택이 가득 찼습니다.")
            return
        
        self.items.append(value)
    
    def pop(self) :
        if not self.is_empty() :
            print("스택이 비어있습니다.")
            return 
        
        length = len(self.items) - 1
        result = self.items[length]
        self.items = self.items[:length]

        return result

    def is_full(self):
        return len(self.items) >= self.max_size
    
    def is_empty(self):
        return self.items #파이썬은 빈리스트를 false 반환
    
class queue :
    def __init__(self, max_size):
        self.items = []
        self.max_size = max_size
    
    def push(self, value) :
        if self.is_full() :
            print("큐가 가득 찼습니다.")
            return
        
        self.items.append(value)
    
    def pop(self) :
        if not self.is_empty() :
            print("큐가 비어있습니다.")
            return 
        
        result = self.items[0] 
        self.items = self.items[1:]

        return result
        
    def is_full(self) :
        return len(self.items) >= self.max_size 
    
    def is_empty(self) :
        return self.items

stack_exam = stack(3)
queue_exam = queue(3)

##STACK

#push 확인 
for i in range(3):
    stack_exam.push(i+1)
#입력 : 1, 2, 3 

#스택값 확인
print(stack_exam.items)
#출력 : [1, 2, 3]

# 오버플로우 걸림 확인
stack_exam.push(5) 
#입력 : 5
# 출력 : 스택이 가득 찼습니다 !

#pop 확인
for j in range(3):
    print(stack_exam.pop())
#출력 : 3, 2, 1

#is_empty 확인
stack_exam.pop()
#출력 : 스택이 비어있습니다.    

## QUEUE
#push 확인 
for i in range(3):
    queue_exam.push(i+1)
#입력 : 1, 2, 3 

#큐 확인
print(queue_exam.items)
#출력 : [1, 2, 3]

# 오버플로우 걸림 확인
queue_exam.push(5) 
#입력 : 5
# 출력 : 큐가 가득 찼습니다.

#pop 확인
for j in range(3):
    print(queue_exam.pop())
#출력 : 1,2,3

#is_empty 확인
queue_exam.pop()
#출력 : 큐가 비어있습니다.    
