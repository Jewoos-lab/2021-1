class Node:
    """링크드 리스트의 노드 클래스"""
    def __init__(self,data):
        self.data = data  # 노드가 저장하는 데이터
        self.next = None  # 다음 노드에 대한 레퍼런스

class LinkedList:
    """더블리 링크드 리스트 클래스"""
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)

        #링크드 리스트가 비었을 때(head노드가 없는경우)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:  # 링크드 리스트에 데이터가 이미 있는 경우
            # 2, 3, 5, 7이 있는 링크드 리스트에 11을 추가하려할때
            # 11을 받는 new_node를 만들고 tail노드의 다음 노드로 만든다.
            self.tail.next = new_node
            new_node.prev = self.tail  # 그후 tail노드를 새롭게 만든 new_node의 전 노드로 만들어 준다.
            self.tail = new_node  # 그후 tail을 새로 만든 노드로 바꿔준다.

    def insert_after(self, previous_node, data):
        """주어진 노드 다음에 데이터를 추가시켜주는 메소드"""
        new_node = Node(data)  # 새로운 노드 생성

        # tail 노드 다음에 노드를 삽입할 때
        if previous_node is self.tail:
            self.tail.next = new_node  # 새로운 노드를 tail 노드의 다음 노드로 지정한다
            new_node.prev = self.tail  # tail 노드를 새로운 노드의 전 노드로 지정한다
            self.tail = new_node  # 새로운 노드를 tail 노드로 지정한다

        # 두 노드 사이에 삽입할 때
        else:
            # 새롭게 생성한 노드를 이미 있는 링크드 리스트에 연결시키고
            new_node.prev = previous_node
            new_node.next = previous_node.next

            # 이미 있는 노드들의 앞과 다음 레퍼런스를 새롭게 생성한 노드로 지정한다
            previous_node.next.prev = new_node
            previous_node.next = new_node

    def find_node_at(self, index):
        """링크드 리스트 접근 연산 메소드. 파라미터 인덱스는 항상 있다고 가정"""
        iterator = self.head

        """링크드 리스트는 레퍼런스를 통해 순서를 저장하기 때문에
        한번에 원하는 위치의 데이터에 접근할수 없다.
        x번 인덱스를 접근하려면 처음부터 x번 접근해야 한다.
        따라서 코드는 이렇게 된다."""
        for _ in range(index):
            iterator = iterator.next

        return iterator

    def find_node_with_data(self, data):
        """링크드 리스트에서 주어진 데이터를 갖고있는 노드를 리턴한다. 단, 해당 노드가 없으면 None을 리턴한다"""
        iterator = self.head  # 링크드 리스트를 돌기 위해 필요한 노드 변수

        while iterator is not None:
            if iterator.data == data:
                return iterator

            iterator = iterator.next

        return None

    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        #링크드 리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        #링크드 리스트 끝까지 돈다.
        while iterator is not None:
            res_str += f" {iterator.data} |"
            iterator = iterator.next

        return res_str

# 새로운 링크드 리스트 생성
my_list = LinkedList()

# 새로운 노드 5개 추가
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)
my_list.append(11)

print(my_list)

# tail 노드 뒤에 노드 삽입
tail_node = my_list.tail  # 4 번째(마지막)노드를 찾는다
my_list.insert_after(tail_node, 5)  # 4 번째(마지막)노드 뒤에 노드 추가
print(my_list)
print(my_list.tail.data)  # 새로운 tail 노드 데이터 출력

# 링크드 리스트 중간에 데이터 삽입
node_at_index_3 = my_list.find_node_at(3)  # 노드 접근
my_list.insert_after(node_at_index_3, 3)
print(my_list)

# 링크드 리스트 중간에 데이터 삽입
node_at_index_2 = my_list.find_node_at(2)  # 노드 접근
my_list.insert_after(node_at_index_2, 2)
print(my_list)

# 맨뒤 노드에 새롭게 추가할때
"""새로운 노드를 tail 노드의 다음 노드로 지정한다
tail 노드를 새로운 노드의 전 노드로 지정한다
새로운 노드를 tail 노드로 지정한다"""

# 중간에 추가할때
"""새롭게 만든 노드를 링크드 리스트에 연결시킬때
new_node를 previous_node의 다음 노드로 지정한다
new_node를 previous_node의 다음 노드의 전 노드로 지정한다
이미 있던 노드들에 새롭게 만든 노드를 연결시킬때
previous_node의 다음 노드의 전 노드를 new_node로 지정한다
previous_node의 다음 노드를 new_node로 지정한다"""