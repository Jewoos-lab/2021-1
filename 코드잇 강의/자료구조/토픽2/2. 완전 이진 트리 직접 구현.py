"""완전 이진 트리는 그것이 가지는 특수한 2가지 성질:

마지막 레벨 직전의 레벨까지는 노드들로 가득 차 있음
마지막 레벨은 왼쪽에서 오른쪽 방향으로 노드들로 가득 차
있어야 함(오른쪽은 비어있어도 되지만 왼쪽은 비어있으면 안 됨)"""

def get_parent_index(complete_binary_tree, index):
    """배열로 구현한 완전 이진 트리에서 index번째 노드의 부모 노드의 인덱스를 리턴"""
    # 부모 노드의 인덱스는 자식노드의 인덱스에서 2를 나눈 후의 정수값(7//2면 3)
    parent_index = index // 2

    # 부모 노드가 있으면 인덱스를 리턴한다.
    # complete_binary_tree리스트의 0번째 인덱스에는 None이 저장돼있기 때문에 인덱스는
    # 0보다 커야하고, 인덱스는 리스트의 길이보다는 작아야 한다.
    if 0 < parent_index < len(complete_binary_tree):
        return parent_index
    return None

def get_left_child_index(complete_binary_tree, index):
    """index번째 노드의 왼쪽 자식 노드의 인덱스 리턴"""
    # 왼쪽 자식 노드의 인덱스는 부모 노드의 인덱스에 2를 곱하면 됨
    left_child_index = index * 2

    # 왼쪽 자식노드가 있으면 인덱스를 리턴한다.
    # complete_binary_tree리스트의 0번째 인덱스에는 None이 저장돼있기 때문에 인덱스는
    # 0보다 커야하고, 인덱스는 리스트의 길이보다는 작아야 한다.
    if 0 < left_child_index < len(complete_binary_tree):
        return left_child_index
    return None

def get_right_child_index(complete_binary_tree, index):
    """index번째 노드의 오른쪽 자식 노드의 인덱스 리턴"""
    # 오른쪽 자식 노드의 인덱스는 부모 노드의 인덱스에 2곱하고 더하기 1
    right_child_index = index * 2 + 1

    # 오른쪽 자식 노드가 있으면 인덱스를 리턴한다.
    # complete_binary_tree리스트의 0번째 인덱스에는 None이 저장돼있기 때문에 인덱스는
    # 0보다 커야하고, 인덱스는 리스트의 길이보다는 작아야 한다.
    if 0 < right_child_index < len(complete_binary_tree):
        return right_child_index
    return None

# 실행 코드
root_node_index = 1 # root 노드

tree = [None, 1, 5, 12, 11, 9, 10, 14, 2, 10]  # 과제 이미지에 있는 완전 이진 트리

# root 노드의 왼쪽과 오른쪽 자식 노드의 인덱스를 받아온다
left_child_index = get_left_child_index(tree, root_node_index)
right_child_index = get_right_child_index(tree,root_node_index)

print(tree[left_child_index])
print(tree[right_child_index])

# 9번째 노드의 부모 노드의 인덱스를 받아온다
parent_index = get_parent_index(tree, 9)

print(tree[parent_index])

# 부모나 자식 노드들이 없는 경우들
parent_index = get_parent_index(tree, 1)  # root 노드의 부모 노드의 인덱스를 받아온다
print(parent_index)

left_child_index = get_left_child_index(tree, 6)  # 6번째 노드의 왼쪽 자식 노드의 인덱스를 받아온다
print(left_child_index)

right_child_index = get_right_child_index(tree, 8)  # 8번째 노드의 오른쪽 자식 노드의 인덱스를 받아온다
print(right_child_index)


