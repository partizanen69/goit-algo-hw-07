# Напишіть алгоритм (функцію), який знаходить суму всіх значень у 
# двійковому дереві пошуку або в AVL-дереві. Візьміть будь-яку 
# реалізацію дерева з конспекту чи з іншого джерела.
# Код виконується, і функція знаходить суму всіх значень у дереві.

from binary_search_tree import Node, bst_insert

def sum_of_values(root: Node | None) -> int:
  if not root:
    return 0
  return root.val + sum_of_values(root.left) + sum_of_values(root.right)

if __name__ == "__main__":
  # Test
  root = Node(5)
  root = bst_insert(root, 3)
  root = bst_insert(root, 2)
  root = bst_insert(root, 4)
  root = bst_insert(root, 8)
  root = bst_insert(root, 7)
  root = bst_insert(root, 6)

  # Test finding sum of values
  print(f"Sum of values in the tree: {sum_of_values(root)}")
