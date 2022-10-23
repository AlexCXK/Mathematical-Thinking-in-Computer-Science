# Develop a Python method change(amount) that for any integer amount in the range from 24 to 1000
# returns a list consisting of numbers 5 and 7 only, such that their sum is equal to amount. For
# example, change(28) may return [7, 7, 7, 7], while change(49) may return [7, 7, 7, 7, 7, 7, 7] or
# [5, 5, 5, 5, 5, 5, 5, 7, 7] or [7, 5, 5, 5, 5, 5, 5, 5, 7].
# To solve this quiz, implement the method change(amount) on your machine, test it on several inputs,
# and then paste your code in the field below and press the submit quiz button.
# Your submission should contain the change method only (in particular, make sure to remove all print
# statements).    #
# def change(amount):
#     solutions = list()
#     factor = 0
#     while factor < amount:
#         difference = amount - factor
#         if (amount - factor) % 7 == 0:
#             solution = list()
#             for a in range(0, (amount - factor) // 7):
#                 solution.append(7)
#             if factor != 0:
#                 for b in range(0,factor//5):
#                     solution.append(5)
#             solutions.append(solution)
#         factor += 5
#     return solutions
#
# print(change(49))
def change(amount):
    assert 24 <= amount <= 1000
    basecases = {24:[5,5,7,7],
                 25:[5]*5,
                 26:[7]*3+[5],
                 27:[5]*4+[7],
                 28:[7]*4}
    return basecases[amount] if amount in basecases else [5] + change (amount - 5)
print(change(49))
