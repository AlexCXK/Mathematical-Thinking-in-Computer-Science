def can_be_extended_to_solution(perm):
    i = len(perm) - 1
    # print(perm)
    for j in range(i):
        # print("i=",i,"j=",j,"perm["+str(i)+"]=" ,perm[i],"perm["+str(j)+"]=", perm[j])
        if i - j == abs(perm[i] - perm[j]):
            return False
    return True
count = 0
def extend(perm, n):
    global count
    if len(perm) == n:
        print(perm)
        count =count +1
        # exit()

    for k in range(n):
        if k not in perm:
            perm.append(k)

            if can_be_extended_to_solution(perm):
                extend(perm, n)

            perm.pop()
extend(perm = [], n = 8)
print(count)