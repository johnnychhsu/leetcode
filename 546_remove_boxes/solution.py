class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        memo={}
        lookup=collections.defaultdict(set)
        last={}
        st=ed=0
        while st<len(boxes):
            while ed<len(boxes) and boxes[ed]==boxes[st]:
                ed+=1
            lookup[boxes[st]].add((st,ed-1))
            for k in range(st,ed):
                last[k]=ed-1
            st=ed
        def helper(i,j,k):
            if j>last[i]:
                i,k = last[i],k+last[i]-i
            else:
                return (j-i+1+k)**2
            if i>j:
                return 0
            if (i,j,k) in memo:
                return memo[i,j,k]
            ans=(k+1)**2+helper(i+1,j,0)
            num=boxes[i]
            for l,r in lookup[num]:
                if l>i and r<=j:
                    ans=max(ans,helper(i+1,l-1,0)+helper(r,j,k+1+r-l))
            memo[i,j,k]=ans
            return ans
        return helper(0,len(boxes)-1,0)     
