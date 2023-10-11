from typing import TypedDict, Unpack


class Node(TypedDict):
    key: int
    value: str


class TreeNode:

    def __init__(self, node: Node):
        self.node = node
        self.right, self.left = None, None


def insert(node: Node) -> None:
    global root
    root = insert_recursive(root, node)


def insert_recursive(root: (TreeNode | None), node: Node):
    if root is None:
        return TreeNode(node)
    else:
        if root.node['key'] == node['key']:
            return None
        elif root.node['key'] > node['key']:
            root.left = insert_recursive(root.left, node)
        else:
            root.right = insert_recursive(root.right, node)

    return root


def print_tree(**kwargs: Unpack[Node]) -> None:
    print(kwargs)


def inroder(root: (TreeNode | None)) -> None:
    if root is None:
        return
    inroder(root.left)
    print_tree(**root.node)
    inroder(root.right)


def insert_tree(arr: list[Node]) -> None:
    for node in arr:
        insert(node)


root = TreeNode({'key': 4, 'value': 'a'})
array_node: list[Node] = [
    {'key': 10, 'value': 'python'},
    {'key': 5, 'value': 'teste'},
    {'key': 50, 'value': 'java'},
    {'key': 1, 'value': 'guilherme'}
]
insert_tree(array_node)
inroder(root)
