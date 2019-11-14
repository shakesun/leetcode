"""
写算法可能会用到链表，自定义一个使用
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class LList(object):

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

    def add_nodes(self, value, pri_node, n=0):
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
        self.add_nodes(value, cur_val, n)

    def list_to_llist(self):
        """把列表转换为链表"""
        pass


if __name__ == '__main__':

    Llist1 = ListNode(0)
    LL = LList()
    LL.add_nodes([2, 5], Llist1)
    LL.iter_node(Llist1)
