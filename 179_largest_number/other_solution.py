from functools import cmp_to_key
def largestNumber(self, a):
    a = list(map(str, a))              
    a.sort(key=cmp_to_key(lambda x, y: int(x+y) - int(y+x)), reverse=True)                
    return ''.join(a if a[0] != '0' else '0')
