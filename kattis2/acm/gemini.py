def main():
  """Calculates the number of problems solved and the total time measure (including penalties) for a team."""

  # Read the input.
  log = []
  while True:
    line = input()
    if line == "-1":
      break
    m, p, r = line.split()
    log.append((int(m), p, r))

  # Initialize the variables to keep track of the number of problems solved and the total time measure.
  num_problems_solved = 0
  total_time = 0

  # Process the log.
  problems_solved = set()
  for m, p, r in log:
    # If the problem has not been solved yet, and the submission is correct, increment the number of problems solved.
    if p not in problems_solved and r == "right":
      num_problems_solved += 1
      problems_solved.add(p)

    # Add the time taken to solve the problem to the total time.
    if r == "right":
      total_time += m
    elif p in problems_solved:
      # If the problem has been solved before, add a 20-minute penalty for each wrong submission.
      total_time += 20

  # Print the output.
  print(num_problems_solved, total_time)


if __name__ == "__main__":
  main()