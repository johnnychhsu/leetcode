class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(typed) < len(name):
            return False
        cur = 0
        prev = -1
        i = 0
        while cur < len(name) and i < len(typed):
            if name[cur] == typed[i]:
                cur += 1
                prev += 1
                i += 1
            elif typed[i] == name[prev]:
                i += 1
            else:
                return False
        if cur < len(name):
            return False
        return True
