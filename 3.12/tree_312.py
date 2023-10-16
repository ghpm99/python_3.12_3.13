from typing import TypedDict, Unpack


# Nó da arvore extende um typedDict, sendo assim é um dict
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


# Recebe um nó da arvore para tratar o conteudo
def print_tree(**kwargs: Unpack[Node]) -> None:
    print(kwargs)


# Chama função de impressao de nó de forma ordenada
def inroder(root: (TreeNode | None)) -> None:
    if root is None:
        return
    inroder(root.left)
    print_tree(**root.node)
    inroder(root.right)


def insert_tree(arr: list[Node]) -> None:
    for node in arr:
        insert(node)


root = TreeNode({'key': 5, 'value': 'root'})
array_node: list[Node] = [
    {'key': 10, 'value': 'python'},
    {'key': 4, 'value': 'typed'},
    {'key': 3, 'value': 'java'},
    {'key': 1, 'value': 'javascript'},
    {'key': 9, 'value': 'node'},
    {'key': 2, 'value': 'thread'},
    {'key': 6, 'value': 'binary'},
    {'key': 8, 'value': 'recursive'},
    {'key': 7, 'value': 'hash'},
    {'key': 0, 'value': 'bash'},
]
insert_tree(array_node)
inroder(root)
