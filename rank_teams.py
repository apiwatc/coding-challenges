"""
In a special ranking system, each voter gives a rank from highest to lowest to all teams participated in the competition.

The ordering of teams is decided by who received the most position-one votes. If two or more teams tie in the first position, 
we consider the second position to resolve the conflict, if they tie again, we continue this process until the ties are resolved. 
If two or more teams are still tied after considering all positions, we rank them alphabetically based on their team letter.

Given an array of strings votes which is the votes of all voters in the ranking systems. Sort all teams according to the ranking system described above.

Return a string of all teams sorted by the ranking system.

Example 1:
Input: votes = ["ABC","ACB","ABC","ACB","ACB"]
Output: "ACB"
Explanation: Team A was ranked first place by 5 voters. No other team was voted as first place so team A is the first team.
Team B was ranked second by 2 voters and was ranked third by 3 voters.
Team C was ranked second by 3 voters and was ranked third by 2 voters.
As most of the voters ranked C second, team C is the second team and team B is the third.
"""


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
