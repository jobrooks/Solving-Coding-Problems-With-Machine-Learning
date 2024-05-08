from math import sqrt

def count_lacing_patterns(N, d, s, t, f_min, f_max, L):
  """Counts the number of lacing patterns that meet the given requirements.

  Args:
    N: The number of eyelets on a side.
    d: The distance between eyelets (in millimeters).
    s: The separation between the columns of eyelets (in millimeters).
    t: The thickness of an eyelet (in millimeters).
    f_min: The minimum free end length (in millimeters).
    f_max: The maximum free end length (in millimeters).
    L: The length of the shoelace (in millimeters).

  Returns:
    The number of lacing patterns that meet the given requirements.
  """

  # Check if the given shoelace length is valid.
  if L < 2 * (N + 1) * d + 2 * N * t + f_min:
    return 0

  # Calculate the total length of the shoelace that is used for lacing.
  lace_length = L - 2 * f_min - 2 * N * t

  # Calculate the number of eyelets that the shoelace can pass through.
  num_eyelets = int((lace_length - 2 * d) / (2 * d + s))

  # If the number of eyelets is odd, then the shoelace cannot be laced symmetrically.
  if num_eyelets % 2 == 1:
    return 0

  # Calculate the length of the shoelace that is used between each eyelet.
  lace_length_between_eyelets = (lace_length - 2 * d) / num_eyelets

  # Calculate the free end length of the shoelace.
  f = (lace_length - lace_length_between_eyelets * num_eyelets) / 2

  # Check if the free end length of the shoelace falls within the given range.
  if f_min <= f <= f_max:
    return 1

  # Otherwise, the shoelace cannot be laced with the given requirements.
  return 0


def main():
  """Gets the input data and prints the number of lacing patterns for each shoelace length."""

  # Get the input data.
  N, d, s, t, f_min, f_max = map(int, input().split())
  L_values = [int(input()) for _ in range(100)]

  # Count the number of lacing patterns for each shoelace length.
  num_lacing_patterns = [count_lacing_patterns(N, d, s, t, f_min, f_max, L) for L in L_values]

  # Print the number of lacing patterns for each shoelace length.
  print(*num_lacing_patterns)


if __name__ == "__main__":
  main()