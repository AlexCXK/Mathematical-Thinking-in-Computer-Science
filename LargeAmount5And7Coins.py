def largeAmount(n):
    ans = list()
    if n < 10:
        return ans

    if (n % 5 == 0) or (n % 7 == 0):
        ans.extend(largeAmount(n - 1))
        return ans
    factor = 7
    while factor < n:
        if ((n - factor) % 5 == 0):

            ans.extend(largeAmount(n - 1))
            return ans
        else:
            factor += 7

    ans.append(n)
    ans.extend(largeAmount(n - 1))
    return ans


a = largeAmount(1000)
print(a)
