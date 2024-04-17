def count_complexity_classes(M, N, relations):
  """Counts the minimum and maximum number of distinct complexity classes.

  Args:
    M: The number of subset relations.
    N: The number of proper subset relations.
    relations: A list of tuples representing the relations between complexity classes.

  Returns:
    A tuple of the minimum and maximum number of distinct complexity classes.
  """

  # Create a set of all complexity classes mentioned in the relations.
  classes = set()
  for relation in relations:
    classes.add(relation[0])
    classes.add(relation[1])

  # Create a graph where the nodes are complexity classes and the edges represent
  # the subset relations.
  graph = {}
  for relation in relations:
    if relation[0] not in graph:
      graph[relation[0]] = set()
    graph[relation[0]].add(relation[1])

  # Find the connected components of the graph.
  components = []
  visited = set()
  for cls in classes:
    if cls not in visited:
      component = set()
      dfs(cls, graph, component, visited)
      components.append(component)

  # The minimum number of distinct complexity classes is the number of connected
  # components.
  min_classes = len(components)

  # The maximum number of distinct complexity classes is the total number of
  # complexity classes.
  max_classes = len(classes)

  return min_classes, max_classes


def dfs(cls, graph, component, visited):
  """Performs a depth-first search on the graph to find connected components."""

  visited.add(cls)
  component.add(cls)
  for neighbor in graph[cls]:
    if neighbor not in visited:
      dfs(neighbor, graph, component, visited)


if __name__ == "__main__":
  # Read the input.
  M, N = map(int, input().split())
  relations = [tuple(input().split()) for _ in range(M + N)]

  # Count the minimum and maximum number of distinct complexity classes.
  min_classes, max_classes = count_complexity_classes(M, N, relations)

  # Print the output.
  print(min_classes, max_classes)