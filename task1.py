# Напишіть алгоритм (функцію), який знаходить найбільше значення у двійковому дереві 
# пошуку або в AVL-дереві. Візьміть будь-яку реалізацію дерева з конспекту чи з іншого джерела.
# Код виконується, і функція знаходить найбільше значення в дереві.

class Node:
  def __init__(self, key: int) -> None:
    self.left = None
    self.right = None
    self.val = key

  def __str__(self, level: int = 0, prefix: str = "Root: ") -> str:
    ret = "\\t" * level + prefix + str(self.val) + "\\n"
    if self.left:
      ret += self.left.__str__(level + 1, "L--- ")
    if self.right:
      ret += self.right.__str__(level + 1, "R--- ")
    return ret

def insert(root: Node | None, key: int) -> Node:
  if root is None:
    return Node(key)
  else:
    if key < root.val:
      root.left = insert(root.left, key)
    else:
      root.right = insert(root.right, key)
  return root

def search(root: Node | None, key: int) -> Node | None:
  if root is None or root.val == key:
    return root
  if key < root.val:
    return search(root.left, key)
  return search(root.right, key)

def min_value_node(node: Node) -> Node:
  current = node
  while current.left:
    current = current.left
  return current

def delete(root: Node | None, key: int) -> Node | None:
  if not root:
    return root

  if key < root.val:
    root.left = delete(root.left, key)
  elif key > root.val:
    root.right = delete(root.right, key)
  else:
    if not root.left:
      temp = root.right
      root = None
      return temp
    elif not root.right:
      temp = root.left
      root = None
      return temp
    root.val = min_value_node(root.right).val
    root.right = delete(root.right, root.val)
  return root

def find_max_value(root: Node | None) -> int | None:
  if not root:
    return None
  current = root
  while current.right:
    current = current.right
  return current.val

def find_min_value(root: Node | None) -> int | None:
  if not root:
    return None
  current = root
  while current.left:
    current = current.left
  return current.val

# Test
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 8)
root = insert(root, 7)
root = insert(root, 6)


# Test finding max value
print(root)
print(f"Maximum value in the tree: {find_max_value(root)}")
print(f"Minimum value in the tree: {find_min_value(root)}")
