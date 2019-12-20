def maxSumDivThree(self, A):
        seen = [0, 0, 0]
        for a in A:
            for i in seen[:]:
                seen[(i + a) % 3] = max(seen[(i + a) % 3], i + a)
        return seen[0]
