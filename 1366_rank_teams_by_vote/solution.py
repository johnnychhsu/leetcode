class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        keys = {c: [0] * len(votes[0]) + [c] for c in votes[0]}
        for vote in votes:
            for i, c in enumerate(vote):
                keys[c][i] -= 1
        return ''.join(sorted(keys, key=keys.get))
