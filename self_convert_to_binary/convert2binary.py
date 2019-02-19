def convert2Binary(n):
    ans = []
    while n > 0:
        if n % 2 == 0:
            ans.append(str(0))
        else:
            ans.append(str(1))
        n >>= 1
    ans.reverse()
    return ''.join(ans)

print(convert2Binary(102))
