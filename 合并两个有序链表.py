#将两个升序链表合并为一个新的 升序 链表并返回。
#新链表是通过拼接给定的两个链表的所有节点组成的
list1 = input().split()
list2 = input().split()
merge_list = sorted([int(i) for i in list1+list2])
print(merge_list)