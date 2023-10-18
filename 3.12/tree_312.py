from typing import NotRequired, TypedDict, Unpack


# Nó da arvore extende um typedDict, sendo assim é um dict
# pode receber tipos diferentes em cada variavel, nao precisa ser homogenea em sua declaração
class Node(TypedDict):
    key: int
    value: str
    version: NotRequired[float]


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


# args é do tipo homogenea int, já kwargs recebe todas declarações de chave e tipo de Node, no caso int/str e um float opcional
def print_loop(*args: int, **kwargs: Unpack[Node]) -> None:
    print(args, kwargs)
    for i in range(*args):
        print(i, kwargs)


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
    {'key': 10, 'value': 'python', 'version': 1.0},
    {'key': 4, 'value': 'typed'},
    {'key': 3, 'value': 'java', 'version': 1.0},
    {'key': 1, 'value': 'javascript', 'version': 1.0},
    {'key': 9, 'value': 'node', 'version': 1.0},
    {'key': 2, 'value': 'thread'},
    {'key': 6, 'value': 'binary'},
    {'key': 8, 'value': 'recursive'},
    {'key': 7, 'value': 'hash'},
    {'key': 0, 'value': 'bash', 'version': 1.0},
]
insert_tree(array_node)
inroder(root)

print_tree(key=15, value='print externo')

print_loop(2, key=20, value='print em loop')
