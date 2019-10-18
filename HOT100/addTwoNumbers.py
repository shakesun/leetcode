# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret_node = ListNode(0)
        prenode = ret_node
        lastnode = prenode
        val = 0
        while val or l1 or l2:
            val, cur = divmod(val + (l1.val if l1 else 0) + (l2.val if l2 else 0), 10)
            lastnode.next = ListNode(cur)
            lastnode = lastnode.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return prenode.next

def generateList(li):
    """
    一个可以将列表转化为链表的
    :param li:
    :return:
    """
    prenode = ListNode(0)
    lastnode = prenode
    for _ in li:
        lastnode.next = ListNode(_)
        lastnode = lastnode.next

    return prenode.next

def printList(prenode):
    """
    遍历链表
    :param prenode:
    :return:
    """
    while prenode:
        print(prenode.val)
        prenode = prenode.next


if __name__ == '__main__':
    l1 = generateList([1, 5, 8])
    l2 = generateList([9, 1, 2, 9])
    # printList(l1)
    # printList(l2)
    s = Solution()
    sum = s.addTwoNumbers(l1, l2)
    printList(sum)

