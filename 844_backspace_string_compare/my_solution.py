class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s_res = []
        t_res = []
        for w in S:
            if w == '#':
                if s_res:
                    s_res.pop()
            else:
                s_res.append(w)
        for t in T:
            if t == '#':
                if t_res:
                    t_res.pop()
            else:
                t_res.append(t)
        if ''.join(s_res) == ''.join(t_res):
            return True
        else:
            return False
            
                
