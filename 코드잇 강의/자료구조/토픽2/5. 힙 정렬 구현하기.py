def swap(tree, index_1, index_2):
    """완전 이진 트리의 노드 index_1과 노드 index_2의 위치를 바꿔준다"""
    temp = tree[index_1]
    tree[index_1] = tree[index_2]
    tree[index_2] = temp


def heapify(tree, index, tree_size):
    """heapify 함수"""

    # 왼쪽 자식 노드의 인덱스와 오른쪽 자식 노드의 인덱스를 계산
    left_child_index = 2 * index
    right_child_index = 2 * index + 1

    largest = index  # 일단 부모 노드의 값이 가장 크다고 설정

    # 왼쪽 자식 노드의 값과 비교
    if 0 < left_child_index < tree_size and tree[largest] < tree[left_child_index]:
        largest = left_child_index

    # 오른쪽 자식 노드의 값과 비교
    if 0 < right_child_index < tree_size and tree[largest] < tree[right_child_index]:
        largest = right_child_index

    if largest != index:  # 부모 노드의 값이 자식 노드의 값보다 작으면
        swap(tree, index, largest)  # 부모 노드와 최댓값을 가진 자식 노드의 위치를 바꿔준다
        heapify(tree, largest, tree_size)  # 자리가 바뀌어 자식 노드가 된 기존의 부모 노드를대상으로 또 heapify 함수를 호출한다


def heapsort(tree):
    """힙 정렬 함수"""
    tree_size = len(tree)

    # 코드를 쓰세요
    # 마지막 노드부터 root 노드까지 heapify를 해준다
    # 이 코드가 실행되고 나면 리스트 tree는 힙이 됩니다.
    for index in range(tree_size - 1, 0, -1):
        heapify(tree, index, tree_size)

    # 힙 정렬
    # 1. root노드와 마지막 노드의 위치를 바꿉니다. 마지막 위치로 간 기존의 root노드는 이제 힙에서 없다고 가정
    # 2. 새로운 root 노드가 힙 속성을 지킬 수 있게 heapify합니다.
    # 3. 힙에 남아있는 노드가 없도록 단계 1~2를 반복합니다.
    for i in range(tree_size - 1, 0, -1):
        swap(tree, 1, i)
        heapify(tree, 1, i)  # root 노드에 heapify를 호출한다


# 실행 코드
data_to_sort = [None, 6, 1, 4, 7, 10, 3, 8, 5, 1, 5, 7, 4, 2, 1]
heapsort(data_to_sort)
print(data_to_sort)