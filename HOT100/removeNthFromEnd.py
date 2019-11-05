"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        org_head = head
        head_for_iter = head
        cnt = 0
        if head.next is None:
            head.val = None
            return
        while True:
            if cnt >= n + 1:
                head = head.next
            cnt += 1
            head_for_iter = head_for_iter.next
            if head_for_iter is None:
                if head == org_head:
                    return org_head.next
                head.next = head.next.next
                break
        return org_head

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
    l1 = [2]
    S.add_nodes(l1, 0, N)
    print("删除前。。。")
    S.iter_node(N)
    New_N = S.removeNthFromEnd(N, 1)
    print("删除后。。。")
    S.iter_node(New_N)
