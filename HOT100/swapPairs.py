"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""
from leetcode.DataStructure.LList import LList
import copy

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    # TODO 这里有问题，需要经一步解决
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return head
        first_point = head
        new_head = None
        cnt = 0
        while first_point is not None:
            second_point = first_point.next
            if cnt == 0:
                new_head = second_point
                cnt += 1
            if second_point is None:
                break
            first_point.next = first_point.next.next
            second_point.next = first_point
            first_point = first_point.next

        # 尝试用不新建链表的方式去实现
        return new_head


if __name__ == '__main__':
    S = Solution()
    Llist1 = ListNode(1)
    # Llist2 = ListNode(1)
    LL = LList()
    LL.add_nodes([2, 3, 4], Llist1)
    LL.iter_node(Llist1)
    swap_Llist1 = S.swapPairs(Llist1)
    print("--分割线--")
    LL.iter_node(swap_Llist1)
