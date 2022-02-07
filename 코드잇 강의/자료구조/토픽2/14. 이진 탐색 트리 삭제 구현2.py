""" 이번 과제에서는 이진 탐색 트리 삭제 연산 중 두 번째 경우:
    하나의 자식만 있는 노드를 삭제하는 경우를 코드로 구현해 볼게요.
    이 경우는 영상에서 본 것과 같이
    “삭제하는 노드의 위치를 자식 노드가 대신 차지한다”를 해주기만 하면 되는데요."""

class Node:
    """이진 탐색 트리 노드 클래스"""

    def __init__(self, data):
        self.data = data
        self.parent = None
        self.right_child = None
        self.left_child = None


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

    def delete(self, data):
        """이진 탐색 트리 삭제 메소드"""
        node_to_delete = self.search(data)  # 삭제할 노드를 가지고 온다
        parent_node = node_to_delete.parent  # 삭제할 노드의 부모 노드

        # 경우 1: 지우려는 노드가 leaf 노드일 때
        if node_to_delete.left_child is None and node_to_delete.right_child is None:
            if self.root is node_to_delete:
                self.root = None
            else:  # 일반적인 경우
                if node_to_delete is parent_node.left_child:
                    parent_node.left_child = None
                else:
                    parent_node.right_child = None

        # 경우 2: 지우려는 노드가 자식이 하나인 노드일 때:
        elif node_to_delete.left_child is None:  # 지우려는 노드가 오른쪽 자식만 있을 때:
            # 지우려는 노드가 root 노드일 때
            if node_to_delete is self.root:
                self.root = node_to_delete.right_child
                self.root.parent = None
            # 지우려는 노드가 부모의 왼쪽 자식일 때
            elif node_to_delete is parent_node.left_child:
                parent_node.left_child = node_to_delete.right_child
                node_to_delete.right_child.parent = parent_node
            # 지우려는 노드가 부모의 오른쪽 자식일 때
            else:
                parent_node.right_child = node_to_delete.right_child
                node_to_delete.right_child.parent = parent_node

        elif node_to_delete.right_child is None:  # 지우려는 노드가 왼쪽 자식만 있을 때:
            # 지우려는 노드가 root 노드일 때
            if node_to_delete is self.root:
                self.root = node_to_delete.left_child
                self.root.parent = None
            # 지우려는 노드가 부모의 왼쪽 자식일 때
            elif node_to_delete is parent_node.left_child:
                parent_node.left_child = node_to_delete.left_child
                node_to_delete.left_child.parent = parent_node
            # 지우려는 노드가 부모의 오른쪽 자식일 때
            else:
                parent_node.right_child = node_to_delete.left_child
                node_to_delete.left_child.parent = parent_node

            # 경우 3: 지우려는 노드가 2개의 자식이 있을 때

        else:
            # 1. 지우려는 노드의 succssor를 받아옵니다.(find_min 메소드 활용)
            """ successor는 특정 노드보다 큰 노드중 가장 작은 노드입니다.
                과제에서 작성한 find_min메소드를 쓰면 successor를 쉽게
                찾아낼 수 있는데요. node_to_delete의 오른쪽 부분 트리에 있는
                모든 노드는 node_to_delete보다 큽니다. 이 중에서 가장 작은 노드를
                고르면 되겠죠? 따라서 find_min 메소드의 파라미터로 node_to_delete의
                오른쪽 자식을 넘겨주면 됩니다."""
            successor = self.find_min(node_to_delete.right_child)

            # 2. 삭제하려는 노드 데이터에 successor의 데이터를 저장합니다.
            node_to_delete.data = successor.data
            """ 이때 아래에 써있는거 처럼 successor는 두개가 된다.
                위에 한개, 맨아래 한개"""


            # 3. successor 노드 트리에서 삭제
            if successor is successor.parent.left_child:  # successor 노드가 오른쪽 자식일 때
                # successor가 오른쪽 자식만 가지고 있기 때문에 이런 코드가 나옴.
                # 왼쪽 자식은 있을 수 가 없음.
                successor.parent.left_child = successor.right_child
            else:  # successor 노드가 왼쪽 자식일 때
                successor.parent.right_child = successor.right_child
                """ 위에꺼 코드 해석은: 일단 successor의 왼쪽 자식은 있을수가 없어
                    successor는 특정노드보다 큰 노드중 가장 작은 노드이기 때문이야.
                    그래서 successor가 현재 2개잖아?(아래에 써놓은거 처럼) 
                    맨 아래있는 successsor를 없애주기 위해 쓴 코드야."""

            if successor.right_child is not None:  # successor 노드가 오른쪽 자식이 있을 떄
            """  이 코드의 해석은: 삭제하려는 successor가 14면 14는 현재 이 트리안에 2개야
                 그럼 맨 아래있는 successor를 지워줘야 하잖아 근데 이때 지워야할 successor의
                 오른쪽 자식이 있는 상태에서 successor를 지워버리면 안되니까
                 그 오른쪽 자식의 부모를 지워야할 successor의 부모로 만들어 주는거지 ok?"""
                successor.right_child.parent = successor.parent

    @staticmethod
    def find_min(node):
        """(부분)이진 탐색 트리의 가장 작은 노드 리턴"""
        # 코드를 쓰세요
        temp = node  # 탐색 변수. 파라미터 node로 초기화

        # temp가 node를 뿌리로 갖는 부분 트리에서 가장 작은 노드일 때까지 왼쪽 자식 노드로 간다
        while temp.left_child is not None:
            temp = temp.left_child

        return temp

    def search(self, data):
        """이진 탐색 트리 탐색 메소드, 찾는 데이터를 갖는 노드가 없으면 None을 리턴한다"""
        temp = self.root  # 탐색 변수. root 노드로 초기화

        # 원하는 데이터를 갖는 노드를 찾을 때까지 돈다
        while temp is not None:
            # 원하는 데이터를 갖는 노드를 찾으면 리턴
            if data == temp.data:
                return temp
            # 원하는 데이터가 노드의 데이터보다 크면 오른쪽 자식 노드로 간다
            if data > temp.data:
                temp = temp.right_child
            # 원하는 데이터가 노드의 데이터보다 작으면 왼쪽 자식 노드로 간다
            else:
                temp = temp.left_child

        return None  # 원하는 데이터가 트리에 없으면 None 리턴

    def insert(self, data):
        """이진 탐색 트리 삽입 메소드"""
        new_node = Node(data)  # 삽입할 데이터를 갖는 노드 생성

        # 트리가 비었으면 새로운 노드를 root 노드로 만든다
        if self.root is None:
            self.root = new_node
            return

        # 코드를 쓰세요
        temp = self.root  # 저장하려는 위치를 찾기 위해 사용할 변수. root 노드로 초기화한다

        # 원하는 위치를 찾아간다
        while temp is not None:
            if data > temp.data:  # 삽입하려는 데이터가 현재 노드 데이터보다 크다면
                # 오른쪽 자식이 없으면 새로운 노드를 현재 노드 오른쪽 자식으로 만듦
                if temp.right_child is None:
                    new_node.parent = temp
                    temp.right_child = new_node
                    return
                # 오른쪽 자식이 있으면 오른쪽 자식으로 간다
                else:
                    temp = temp.right_child
            else:  # 삽입하려는 데이터가 현재 노드 데이터보다 작다면
                # 왼쪽 자식이 없으면 새로운 노드를 현재 노드 왼쪽 자식으로 만듦
                if temp.left_child is None:
                    new_node.parent = temp
                    temp.left_child = new_node
                    return
                # 왼쪽 자식이 있다면 왼쪽 자식으로 간다
                else:
                    temp = temp.left_child

    def print_sorted_tree(self):
        """이진 탐색 트리 내의 데이터를 정렬된 순서로 출력해주는 메소드"""
        print_inorder(self.root)  # root 노드를 in-order로 출력한다


# 빈 이진 탐색 트리 생성
bst = BinarySearchTree()

# 데이터 삽입
bst.insert(7)
bst.insert(11)
bst.insert(9)
bst.insert(17)
bst.insert(8)
bst.insert(5)
bst.insert(19)
bst.insert(3)
bst.insert(2)
bst.insert(4)
bst.insert(14)

# 자식이 하나만 있는 노드 삭제
bst.delete(5)
bst.delete(9)

bst.print_sorted_tree()