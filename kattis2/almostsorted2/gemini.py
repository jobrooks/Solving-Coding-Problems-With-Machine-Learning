def is_almost_sorted(array):
  """
  Checks if the given array is almost sorted.

  Args:
    array (list): The array to check.

  Returns:
    bool: True if the array is almost sorted, False otherwise.
  """
  
  n = len(array)
  if n <= 2:
    return True

  # Find the first and last elements out of order.
  i = 0
  while i < n - 1 and array[i] <= array[i + 1]:
    i += 1

  j = n - 1
  while j > 0 and array[j] >= array[j - 1]:
    j -= 1
  
  if j - i <= 1:
    return True

  # Check if the subarray between i and j can be reversed to obtain an ascending sorted array.
  subarray = array[i:j+1]
  subarray.sort()
  
  for k in range(i, j+1):
    if array[k] != subarray[k - i]:
      return False

  return True


def main():
  """
  Gets input from the user and prints the result.
  """

  n = int(input())
  array = list(map(int, input().split()))

  if is_almost_sorted(array):
    print("Yes")
  else:
    print("No")


if __name__ == "__main__":
  main()