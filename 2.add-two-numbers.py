#
# @lc app=leetcode.cn id=2 lang=python3
# @lcpr version=30204
#
# [2] 两数相加
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0) # 哑节点
        current = dummy     # 当前节点
        carry = 0           # 进位

        while l1 or l2 or carry:
            # 取值
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            # 计算当前位置值
            total = x + y +carry
            # 计算进位
            carry = total // 10
            # 取当值
            digit = total % 10
            # 更新节点
            current.next = ListNode(digit)
            current = current.next
            # 移位
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next



# @lc code=end



#
# @lcpr case=start
# [2,4,3]\n[5,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n[0]\n
# @lcpr case=end

# @lcpr case=start
# [9,9,9,9,9,9,9]\n[9,9,9,9]\n
# @lcpr case=end

#

