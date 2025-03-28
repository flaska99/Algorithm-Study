from __future__ import annotations
from typing import Any, Type

class Node :
    def __init__(self, key: Any, value: Any, left : Node = None, right: Node = None):

        self.key = key
        self.value = value
        self.left = left # 왼쪽 포인터
        self.right = right # 오른쪽 포인터
    
class BinarySearchTree :

    def __init__(self):
        self.root = None
    
    def search(self, key : Any) -> Any :
        p = self.root

        while True :
            if p is None: #진행 불가능
                return None # 검색 실패
            
            if key == p.key:
                return p.value
            elif key < p.key:
                p = p.left
            else:
                p = p.right
            
    def add(self, key : Any, value : Any) -> bool:
        # 키와 벨류 값으로 하는 노드를 삽입
        def add_node(node : Node, key : Any, value : Any) -> None : 
            # node를 루트로 하는 서브트리에 키값과 벨류값을 삽입
            # 값이 존재한다면 재귀를 통해 해당 노드를 타고 들어감감
            if key == node.key:
                return False
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
            
            else:
                if node.right is None :
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)
            return True
        
        if self.root is None :
            self.root = Node(key, value, None, None)
            return True
        else :
            return add_node(self.root, key, value)
        
        
    def remove(self, key: Any) -> bool :
        ## 키값이 key인 노드 삭제
        p = self.root # 스캔 노드
        parent = None # 스캔 중인 노드의 부모 노드
        is_left_child = True # parent의 왼쪽 자식 노드 인지 확인

        while True :
            if p is None : # 더이상 진행 안됨
                return False # 키 존재 x
            
            if key == p.key: # key와 노드 p의 키가 같으면
                break # 루프 탈출 (검색 성공 )

            else:
                parent = p # 가지를 내려가기전에 부모를 설정

                if key < p.key: # key쪽이 작으면
                    is_left_child = True # 이제부터 왼쪽 자식으로 내려감
                    p = p.left # 왼쪽 서브트리 스캔
                
                else:
                    is_left_child = False # 여기서는 오른쪽 자식으로 내려감 
                    p = p.right # 오른쪽 서브트리 스캔

        if p.left is None : ## p에게 왼쪽 자식이 없다면 
            if p is self.root: ## p가 루트일 경우 그냥 오른쪽자식을 루트로 지정
                self.root = p.right 
            elif is_left_child: ## p가 왼쪽 서브노드 였을경우 그 노드의 오른쪽 서브노드를 부모와 이음
                parent.left = p.right 
            else: ## 위 조건과 반대일 경우 (오른쪽 서브 노드 였을 경우)
                parent.right = p.right
        
        elif p.right is None: ## p에게 오른쪽 자식이 없다면 위 조건과 반대로
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left
            else:
                parent.right = p.right

        else: ## p에게 자식이 다 있다면
            parent = p
            left = p.left # 서브트리안에서 가장 큰 노드
            is_left_child = True

            while left.right is not None: #서브 트리 중 가장 큰 노드 검색
                parent = left
                left = left.right 
                is_left_child = False
                
            p.key = left.key # left(가장 큰 노드)의 키를 p로 이동
            p.value = left.value #left(가장 큰노드)의 value를 p로 이동

            ## 가장 큰 노드 검색 특성상 제일 오른쪽 자식의 끝노드로 가기 때문에
            ## 해당 자식의 오른쪽 자식이 있을 수 없음
            ## 따라서 데이터를 삭제할때 부모의 왼쪽 혹은 오른쪽에 
            ## 제일 큰 자식의 왼쪽노드를 붙여 주는거임

            if is_left_child:
                parent.left = left.left #left데이터 삭제 
            
            else:
                parent.right = left.left # left데이터 삭제

            return True
        

    def dump(self) -> None:
        #모든 키를 오름차순으로 출력함
        
        def print_subtree(node : Node):
            ## node를 루트로 하는 서브트리의 노드들의 키를 오름차순으로 출력
            if node is not None:
                print_subtree(node.left)
                print(f'{node.key} {node.value}') ## 재귀의 중간의 껴있음 -> 중위순회
                print_subtree(node.right)

        print_subtree(self.root)

    def min_key(self) -> Any:
        ## 가장 작은 키는 왼쪽 자식 끝에 있음
        if self.root is None:
            return None
        
        p = self.root
        while p.left is not None:
            p = p.left
        
        return p.key
    
    def max_key(self) -> Any:
        ## 가장 큰 키는 오른쪽 자식 끝에 있음
        if self.root is None:
            return None
        p = self.root
        while p.right is not None:
            p = p.right

        return p.key



        
