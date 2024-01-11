# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution(object):
#
#     def __init__(self):
#         self.addTwoNumbers(l1, l2)
#
#     def addTwoNumbers(self, l1, l2):
#
#         reversed_one = [x for x in reversed(l1)]
#         reversed_two = [x for x in reversed(l2)]
#
#         rtype = []
#
#         for x in reversed_one:
#             for y in reversed_two:
#                 rtype.append(x + y)
#
#         print(rtype)
#
#
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """

# # rtype = [(reversed_two[y] + x) for x in reversed_one if reversed_two[y] + x < 10]

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

reversed_one = [x for x in reversed(l1)]
reversed_two = [x for x in reversed(l2)]
rtype = []
index_position = 0
remainder = 0

# for x in reversed_one:
#     ip_r2 = reversed_two[index_position]  # Short Hand
#     remainder_calc = ((ip_r2 + x) % 10)  # Shorthand - check if remainder
#     equation = ip_r2 + x
#     if remainder_calc == 0:  # If no Remainder
#         if equation + remainder >= 10:
#             rtype.append(remainder_calc)
#             remainder = 1
#         else:
#             if remainder == 1:
#                 rtype.append(equation + remainder)
#                 remainder = 0
#             else:
#                 rtype.append(equation)
#     else:  # If Remainder
#         rtype.append(remainder_calc)
#         remainder = 1
#
#     index_position += 1

for x in reversed_one:
    ip_r2 = reversed_two[index_position]
    remainder_calc = (((ip_r2 + x) + remainder) % 10)
    equation = ip_r2 + x

    if remainder > 0:
        if equation + remainder < 10:
            rtype.append(equation + remainder)
            remainder = 0
        else:
            rtype.append(remainder_calc)
            remainder = 1
    else:
        if equation >= 10:
            rtype.append(remainder_calc)
            remainder = 1
        else:
            rtype.append(equation)
            remainder = 0

    index_position += 1
print(rtype)
