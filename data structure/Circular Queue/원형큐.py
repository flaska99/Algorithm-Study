class CircularQueue:

    # 해당 배열의 크기를 인자로 받아 초기화
    def __init__(self, k):
        self.q = [None] * k
        self.len = k
        self.front = 0
        self.rear = 0

    # 삽입 메소드
    def enQueue(self, value):
        if self.q[self.rear] is None:
            self.q[self.rear] = value   # rear 포인터에 입력받은 인자를 넣는다.
            self.rear = (self.rear + 1) % self.len  # 전체길이로 나머지연산을 하여 포인터가 전체거리를 넘지 못하게 이동시킨다.
            return True
        else:
            return False

    # 추출 메소드
    def deQueue(self):
        if self.q[self.front] is not None:
            result = self.q[self.front]     # result 변수에 배열의 첫번째 요소를 담는다.
            self.q[self.front] = None   # 배열의 첫번쨰요소를 삭제
            self.front = (self.front + 1) % self.len
            return result     # result 변수 리턴
        else:
            return False

    # 배열의 첫번째 요소 출력
    def pr_front(self):
        return False if self.q[self.front] is None else self.q[self.front]

    # 배열의 마지막 요소 출력
    def pr_rear(self):
        return False if self.q[self.rear] is None else self.q[self.rear]

    # 배열이 비어있는지 확인
    def is_empty(self):
        return self.q[self.front] == None and self.q[self.rear] == None

    # 배열이 꽉 차있는지 확인
    def is_full(self):
        return None not in self.q