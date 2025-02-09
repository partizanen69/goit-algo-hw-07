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

def bst_insert(root: Node | None, key: int) -> Node:
  if root is None:
    return Node(key)
  else:
    if key < root.val:
      root.left = bst_insert(root.left, key)
    else:
      root.right = bst_insert(root.right, key)
  return root

def bst_search(root: Node | None, key: int) -> Node | None:
  if root is None or root.val == key:
    return root
  if key < root.val:
    return bst_search(root.left, key)
  return bst_search(root.right, key)

def bst_min_value_node(node: Node) -> Node:
  current = node
  while current.left:
    current = current.left
  return current

def bst_delete(root: Node | None, key: int) -> Node | None:
  if not root:
    return root

  if key < root.val:
    root.left = bst_delete(root.left, key)
  elif key > root.val:
    root.right = bst_delete(root.right, key)
  else:
    if not root.left:
      temp = root.right
      root = None
      return temp
    elif not root.right:
      temp = root.left
      root = None
      return temp
    root.val = bst_min_value_node(root.right).val
    root.right = bst_delete(root.right, root.val)
  return root
