""" 힙은 항상 완전 이진 트리이기 때문에 배열, 리스트로 구현했지만
    이진 탐색 트리는 이진 트리지만 완전 이진 트리라는 보장이 없다.
    따라서 노드클래스를 정의한후 여러 노드 인스턴스를 생성해서
    그 인스턴스를 연결시켜 구현한다."""

""" 이진 탐색 노드의 특성은 왼쪽은 부모노드 보다 반드시 작게
    오른쪽은 부모노드 보다 반드시 크게"""

class Node:
    # 이진트리 구현에서의 노드클래스와 어디가 다른지 비교해서 보기
    """이진 탐색 트리 노드"""
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left_child = None
        self.right_child = None

def print_inorder(node):
    """주어진 노드를 in-order로 출력해주는 함수"""
    if node is not None:
        print_inorder(node.left_child)
        print(node.data)
        print_inorder(node.right_child)

class BinarySearchTree:
    """이진 탐색 트리 클래스"""
    def __init__(self):
        self.root = None

    def print_sorted_tree(self):
        """이진 탐색 트리 내의 데이터를 정렬된 순서로 출력해주는 메소드"""
        print_inorder(self.root)  # root노드를 in-order로 출력한다.

# 비어 있는 이진 탐색 트리 생성
bst = BinarySearchTree()

