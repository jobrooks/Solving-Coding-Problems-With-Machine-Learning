# Difficulty: 1.5
# Justification: 
# Result: wrong answer
# Tests passed: 0/14
# Error: none
# Response: 
def find_cia_blimps(codes):
  """
  Identifies CIA blimps based on the presence of "FBI" in their registration codes.

  Args:
      codes: A list of blimp registration codes (strings).

  Returns:
      A list of indices (integers) corresponding to CIA blimp registrations (sorted).
  """

  cia_blimps = []
  for i, code in enumerate(codes):
    if "FBI" in code:
      cia_blimps.append(i)

  return sorted(cia_blimps)  # Sort indices of CIA blimp registrations

# Read blimp registration codes
codes = []
for _ in range(5):
  code = input()
  codes.append(code)

# Find CIA blimps and print results
cia_blimp_indices = find_cia_blimps(codes)
if not cia_blimp_indices:
  print("HE GOT AWAY!")
else:
  print(" ".join(map(str, cia_blimp_indices)))
