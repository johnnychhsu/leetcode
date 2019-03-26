class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        def makeNext(index):
            ans = [None] * len(A)
            stack = []
            for i in index:
                while stack and i > stack[-1]:
                    ans[stack.pop()] = i
                stack.append(i)
            return ans

        index = sorted(range(len(A)), key=lambda x: A[x])
        oddNext = makeNext(index)
        index.sort(key=lambda x: -A[x])
        evenNext = makeNext(index)

        odd = [False] * len(A)
        even = [False] * len(A)
        odd[-1] = True
        even[-1] = True

        for i in range(len(A) - 2, -1, -1):
            if oddNext[i]:
                odd[i] = even[oddNext[i]]
            if evenNext[i]:
                even[i] = odd[evenNext[i]]
        return sum(odd)