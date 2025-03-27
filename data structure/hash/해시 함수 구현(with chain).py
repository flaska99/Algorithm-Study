from __future__ import annotations
from typing import Any, Type
import hashlib

class Node :

    def __init__(self, key: Any, value: Any, next: Node) -> None :
        self.key = key # 키값
        self.value = value # 벨류값
        self.next = next #뒤 노드 참조

class ChainedHash :

    def __init__(self, capacity: int)-> int:
        self.capacity = capacity # 해시 테이블의 크기
        self.table = [None] * self.capacity # 해시 테이블 선언
    
    def hash_value(self, key: Any) -> int:
        if isinstance(key, int): #해당 키값이 인스턴스내에 존재한다면 해싱시작
            return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)
    # 해시 키가 int형이 아닌경우 표준라이브러리로 형변환을 진행해야한다.

    def search(self, key: Any) -> Any :
        hash = self.hash_value(key) # 검색하는 키의 해시값을 얻어옴
        p = self.table[hash] # 노드를 주목시킴

        while p is not None:
            if p.key == key:
                return p.value #검색 성공 후 벨류값 반환
            
            p = p.next #뒤쪽 노드 주목
        
        return None # 검색을 실패했을 경우
    
    def add(self, key: Any, value: Any) -> bool :
        hash = self.hash_value(key) #추가하는 key의 hash값을 얻어옴
        p = self.table[hash] # 해당 해시에 노드를 주목시킴

        while p is not None:
            if p.key == key:
                return False # 추가 실패
            
            p = p.next # 뒤쪽 노드 참조
        
        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp
        return True # 추가 완료
    
    def remove(self, key:Any) -> bool:

        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None

        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
            
                else:
                    pp.next = p.next
                return True
            pp = p
            p = p.next
        return False    
    

    def dump(self) -> None:

        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f' -> {p.key} ({p.value})', end='')
                p = p.next
                print()
