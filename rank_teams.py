def rankTeams(votes):
    # count = {'W': [0, 0, 0, 0], 'X': [0, 0, 0, 0], 'Y': [0, 0, 0, 0], 'Z': [0, 0, 0, 0]}
    count = {x: [0]*len(votes[0]) for x in votes[0]}

    for vote in votes:
        for rank, team in enumerate(vote):
            count[team][rank] -= 1

    ans = sorted(votes[0], key=lambda v: count[v]+[v])

    return ''.join(ans)


votes = ["ABC", "ACB", "ABC", "ACB", "ACB"]
print(rankTeams(votes))
