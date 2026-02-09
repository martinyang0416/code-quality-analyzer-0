def rankTeams(votes):
    if not votes:
        return ""
    n = len(votes[0])
    teams = list(votes[0])
    count = {team: [0] * n for team in teams}
    for vote in votes:
        for pos, team in enumerate(vote):
            count[team][pos] += 1
    sorted_teams = sorted(teams, key=lambda x: (tuple(-count[x][i] for i in range(n)), x))
    return ''.join(sorted_teams)