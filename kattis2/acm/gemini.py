# 2.1 Error 1/7
def parse_log(log):
    """Parses a contest submission log and returns a list of tuples.
    Each tuple contains the time, problem, and result of a submission.

    Args:
        log: A string containing the contest submission log.

    Returns:
        A list of tuples representing the contest submission log.
    """

    submissions = []
    for line in log.split("\n"):
        if line == "-1":
            break
        time, problem, result = line.split()
        submissions.append((int(time), problem, result))
    return submissions


def calculate_score(submissions):
    """Calculates the primary and secondary scores for a team.

    The primary score is the number of problems that were solved.
    The secondary score is the sum of those submission times that resulted
    in right answers, plus a 20-minute penalty for each wrong submission of
    a problem that is ultimately solved.

    Args:
        submissions: A list of tuples representing the contest submission log.

    Returns:
        A tuple containing the primary and secondary scores.
    """

    primary_score = 0
    secondary_score = 0
    solved_problems = set()
    penalty_minutes = {}

    for time, problem, result in submissions:
        if problem not in penalty_minutes:
            penalty_minutes[problem] = 0
        if result == "right":
            if problem not in solved_problems:
                primary_score += 1
                solved_problems.add(problem)
            secondary_score += time
        else:
            if problem in solved_problems:
                penalty_minutes[problem] += 20

    secondary_score += sum(penalty_minutes.values())

    return primary_score, secondary_score


if __name__ == "__main__":
    log = input()
    submissions = parse_log(log)
    primary_score, secondary_score = calculate_score(submissions)
    print(primary_score, secondary_score)