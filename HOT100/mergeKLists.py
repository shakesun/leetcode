"""
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
"""
from leetcode.DataStructure.LList import LList
import queue

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    # def mergeKLists(self, lists):
    #     """
    #     超时了的垃圾。。。
    #     :type lists: List[ListNode]
    #     :rtype: ListNode
    #     """
    #     dummy_node = ListNode(-1)
    #     increase_node = dummy_node
    #     # 时间复杂度应该是 O(len(l1)+...+len(ln))
    #     while True:
    #         min_v = None
    #         min_v_cnt = -1
    #         all_v = []
    #         for n, list in enumerate(lists):
    #             if not list:
    #                 all_v.append(list)
    #                 continue
    #             v = list.val
    #             all_v.append(v)
    #             if min_v is None or v <= min_v:
    #                 min_v = v
    #                 min_v_cnt = n
    #
    #         if min_v_cnt == -1:
    #             break
    #         # 增加节点
    #         increase_node.next = ListNode(min_v)
    #         increase_node = increase_node.next
    #         # 更新取出初始节点的
    #         lists[min_v_cnt] = lists[min_v_cnt].next
    #
    #     return dummy_node.next

    # def mergeKLists(self, lists):
    #     """
    #     优先队列实现
    #     :param lists:
    #     :return:
    #     """
    #     head = point = ListNode(0)
    #     pq = queue.PriorityQueue()
    #     for _ in lists:
    #         if _:
    #             pq.put((_.val, _))
    #
    #     while not pq.empty():
    #         v, node = pq.get()
    #         point.next = ListNode(v)
    #         point = point.next
    #         node = node.next
    #         if node:
    #             pq.put(node.val, node)
    #     return head.next

    def mergeKLists(self, lists):
        """
        暴力排序
        :param lists:
        :return:
        """
        head = point = ListNode(0)

        all_v = []
        for node in lists:
            # if node:
            while node:
                all_v.append(node.val)
                node = node.next
        all_v.sort()

        for v in all_v:
            point.next = ListNode(v)
            point = point.next

        return head.next


if __name__ == '__main__':
    S = Solution()
    Llist1 = ListNode(0)
    Llist2 = ListNode(1)
    LL = LList()
    LL.add_nodes([2, 5], Llist1)

    merged = S.mergeKLists([Llist1, Llist2])
    LL.iter_node(merged)
