from 链表.单链表 import LinkNodeList, LinkNode


def merge(l1, l2):
    l3 = LinkNodeList()
    cur = LinkNode()
    l3.head = cur

    cur1 = l1.head
    cur2 = l2.head

    while cur1 and cur2:

        if cur1.data <= cur2.data:
            cur.next = cur1
            cur1 = cur1.next
        else:
            cur.next = cur2
            cur2 = cur2.next
        cur = cur.next
    cur.next = cur1 if cur1 else cur2
    return l3


if __name__ == '__main__':
    ll1 = [1, 3, 6, 8, 9]
    l1 = LinkNodeList()
    l1.create_link(ll1)

    ll2 = [2, 3, 5, 7, 8]
    l2 = LinkNodeList()
    l2.create_link(ll2)

    l3 = merge(l1, l2)

    l3.print_link_node()
