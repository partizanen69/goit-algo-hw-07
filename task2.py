# Напишіть алгоритм (функцію), який знаходить 
# найменше значення у двійковому дереві пошуку 
# або в AVL-дереві. Візьміть будь-яку реалізацію дерева з конспекту чи з іншого джерела.
# Код виконується, і функція знаходить найменше значення в дереві.

from binary_search_tree import Node, bst_insert

def find_min_value(root: Node | None) -> int | None:
  if not root:
    return None
  current = root
  while current.left:
    current = current.left
  return current.val

if __name__ == "__main__":
  # Test
  root = Node(5)
  root = bst_insert(root, 3)
  root = bst_insert(root, 2)
  root = bst_insert(root, 4)
  root = bst_insert(root, 8)
  root = bst_insert(root, 7)
  root = bst_insert(root, 6)

  # Test finding min value
  print(f"Minimum value in the tree: {find_min_value(root)}")
