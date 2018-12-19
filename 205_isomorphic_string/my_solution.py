class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        _map = {}
        s_pattern = ''
        t_pattern = ''

        for index, w in enumerate(s):
            if w in _map:
                s_pattern += _map[w]
            else:
                _map[w] = str(index)
                s_pattern += str(index)

        _map = {}
        for index, w in enumerate(t):
            if w in _map:
                t_pattern += _map[w]
            else:
                _map[w] = str(index)
                t_pattern += str(index)
        if s_pattern == t_pattern:
            return True
        else:
            return False
