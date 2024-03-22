# Difficulty: 2.0
# Justification: 
# Result: wrong answer
# Tests passed: 0/7
# Error: none
# Response: 
def calculate_score(submissions):
  """
  Calculates the number of problems solved and total time score with penalties.

  Args:
      submissions: A list of tuples where each tuple represents a submission
                    (minutes, problem, result).

  Returns:
      A tuple containing the number of problems solved and the total time score.
  """
  solved_problems = set()  # Store solved problems to avoid duplicates
  time_score = 0
  penalty = 20

  for minutes, problem, result in submissions:
    if result == "right" and problem not in solved_problems:
      solved_problems.add(problem)
      time_score += minutes
    elif result == "wrong" and problem not in solved_problems:
      time_score += penalty

  return len(solved_problems), time_score

def main():
  """
  Reads input, calculates score, and prints the results.
  """
  submissions = []
  while True:
    line = input().strip()
    if line == "-1":
      break
    minutes, problem, result = line.split()
    submissions.append((int(minutes), problem, result))

  num_solved, total_time = calculate_score(submissions)
  print(num_solved, total_time)

if __name__ == "__main__":
  main()
