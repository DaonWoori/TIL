# 파이썬을 활용한 완전 이진트리 구현
def get_parent_index(complete_binary_tree, index):
    """배열로 구현한 완전 이진 트리에서 index번째 노드의 부모 노드의 인덱스를 리턴하는 함수"""
    if index // 2 <= 0:
        return None
    return index // 2

def get_left_child_index(complete_binary_tree, index):
    """배열로 구현한 완전 이진 트리에서 index번째 노드의 왼쪽 자식 노드의 인덱스를 리턴하는 함수"""
    tree_len = len(complete_binary_tree)

    if index * 2 >= tree_len:
        return None
    return index * 2

def get_right_child_index(complete_binary_tree, index):
    """배열로 구현한 완전 이진 트리에서 index번째 노드의 오른쪽 자식 노드의 인덱스를 리턴하는 함수"""
    tree_len = len(complete_binary_tree)

    if index * 2 >= tree_len - 1:
        return None
    return index * 2 + 1

# 실행 코드
root_node_index = 1

tree = [None, 1, 5, 12, 11, 9, 10, 14, 2, 10]

# root 노드의 왼쪽과 오른쪽 자식 노드의 인덱스를 받아온다
left_child_index = get_left_child_index(tree, root_node_index)
right_child_index = get_right_child_index(tree, root_node_index)
print(tree[left_child_index])
print(tree[right_child_index])

# 9번째 노드의 부모 노드의 인덱스를 받아온다
parent_index = get_parent_index(tree, 9)
print(tree[parent_index])

# 부모나 자식 노드들이 없는 경우들
parent_index = get_parent_index(tree, root_node_index)
print(parent_index)

left_child_index = get_left_child_index(tree, 6)
print(left_child_index)

right_child_index = get_right_child_index(tree, 8)
print(right_child_index)
