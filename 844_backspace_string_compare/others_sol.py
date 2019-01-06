class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s = len(S) - 1
        t = len(T) - 1
        s_counter = 0
        t_counter = 0
        while True:
            while s >= 0 and (s_counter or S[s] == '#'):
                s_counter += 1 if S[s] == '#' else -1
                s -= 1
            while t >= 0 and (t_counter or T[t] == '#'):
                t_counter += 1 if T[t] == '#' else -1
                t -= 1
            if not (t >= 0 and s >= 0 and S[s] == T[t]):
                return t == s == -1
            s -= 1
            t -= 1
