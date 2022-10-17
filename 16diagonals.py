class PrintColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_solution(perm, size):
    output = "----" * size + "-\n"
    for k, v in enumerate(perm):
        output += "| "
        if v == 2:
            output += PrintColors.OKBLUE + "/ " + PrintColors.ENDC
        elif v == 1:
            output += PrintColors.OKBLUE + "\\ " + PrintColors.ENDC
        else:
            output += "  "

        # End of line
        if (k + 1) % size == 0:
            output += "|\n"
            output += "----" * size + "-\n"

    print(output + "\n")


# Check for /
def check_for_du(perm, i, size):
    # Check cell on the left
    if (i % size) != 0 and perm[i - 1] == 1:
        return False

    if len(perm) > size:
        # Check upper cell
        if perm[i - size] == 1:
            return False

        # Check upper-right cell
        if ((i + 1) % size) != 0 and perm[i - size + 1] == 2:
            return False

    return True


# Check for \
def check_for_ud(perm, i, size):
    # Check cell on the left
    if (i % size) != 0 and perm[i - 1] == 2:
        return False

    if len(perm) > size:
        # Check upper cell
        if perm[i - size] == 2:
            return False

        # Check upper-left cell
        if i % size != 0 and perm[i - size - 1] == 1:
            return False

    return True


def can_be_extended_to_a_solution(perm, size):
    if len(perm) == 1:
        return True

    #  Get the last item
    i = len(perm) - 1

    # 2 - /, 1 - \, 0 - empty
    if perm[i] == 2:
        return check_for_du(perm, i, size)
    elif perm[i] == 1:
        return check_for_ud(perm, i, size)
    else:
        return True


def extend(perm, size, n):
    #  If perm is full then return
    if len(perm) == size ** 2:
        if perm.count(1) + perm.count(2) >= n:
            print_solution(perm, size)
        return

    # Try to add a number to permutation
    for k in range(2, -1, -1):
        # Check if perm already contains this number
        perm.append(k)

        # Check if extend is possible
        if can_be_extended_to_a_solution(perm, size):
            extend(perm, size, n)

        perm.pop()


extend(perm=[], size=5, n=16)
