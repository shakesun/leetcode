"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        new_l = ListNode(0)
        dummy = new_l
        while True:
            if l1 is None and l2 is None:
                break

            if l1 is None:
                new_l.next = ListNode(l2.val)
                l2 = l2.next
                new_l = new_l.next
                continue

            if l2 is None:
                new_l.next = ListNode(l1.val)
                new_l = new_l.next
                l1 = l1.next
                continue

            v1 = l1.val
            v2 = l2.val
            if v2 is None or v1 < v2:
                new_l.next = ListNode(v1)
                new_l = new_l.next
                l1 = l1.next
            else:
                new_l.next = ListNode(v2)
                l2 = l2.next
                new_l = new_l.next

        return dummy.next

    # 官方题解，递归，没有新做一个链表出来
    # def mergeTwoLists(self, l1, l2):
    #     if l1 is None:
    #         return l2
    #     elif l2 is None:
    #         return l1
    #     elif l1.val < l2.val:
    #         l1.next = self.mergeTwoLists(l1.next, l2)
    #         return l1
    #     else:
    #         l2.next = self.mergeTwoLists(l1, l2.next)
    #         return l2

    def iter_node(self, head):
        """
        遍历链表
        :param head:
        :return:
        """
        print(head.val)
        # ls1.append(head.val)
        head = head.next
        if head is None:
            return
        self.iter_node(head)

    def add_nodes(self, value, n, pri_node):
        """
        批量增加新的节点
        :param new_node:
        :return:
        """
        if n == len(value):
            return
        cur_val = ListNode(value[n])
        pri_node.next = cur_val

        n += 1
        self.add_nodes(value, n, cur_val)


if __name__ == '__main__':
    S = Solution()

    N = ListNode(1)
    l1 = [3, 5, 7]
    N_1 = ListNode(2)
    l1_1 = [4, 6, 8]
    S.add_nodes(l1, 0, N)
    S.add_nodes(l1_1, 0, N_1)

    S.iter_node(N)
    S.iter_node(N_1)
    N_N = S.mergeTwoLists(N, N_1)
    S.iter_node(N_N)
