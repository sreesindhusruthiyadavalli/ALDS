class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists) :
        while(len(lists) > 1):
            mergedLists = []
            for i in range(0, len(lists), 2) :
                print(i, len(lists))
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                mergedLists.append(self.mergeTwoLists(l1,l2))
            lists = mergedLists  
        print("sss",lists[0])
        return lists[0]    
            
            
    def mergeTwoLists(self, l1, l2):
        if l1 == None: return l2
        if l2 == None: return l1
        newHead = ListNode(0)
        temp = newHead
        while(l2 !=None and l1 != None):
            print("sss1",l1.val, l2.val)
            if l1.val <= l2.val:
                temp.next = ListNode(l1.val)
                l1= l1.next
            else:
                temp.next = ListNode(l2.val)
                l2 = l2.next
            temp = temp.next
            
        if(l1 != None):
            temp.next = ListNode(l1.val)
            l1 = l1.next
        elif l2 != None:
            temp.next = ListNode(l2.val)
            l2 = l2.next
            
        #newHead = newHead.next    
        # tempIter = newHead
        # while(tempIter != None):        
        #     print(tempIter.val)  
        #     tempIter = tempIter.next
        return newHead.next

lists = [[1,4,5],[1,3,4],[2,6]]
pass_lists = []
node11 = ListNode(1)
#node12 = 
#node13 = ListNode(5)
node11.next = ListNode(4)
node11.next.next = ListNode(5)
#print(node11.val, node11.next.val, node11.next.next.val)
#pass_lists.append([node11, node11.next, node11.next.next])
pass_lists.append(node11)
node21 = ListNode(1)
node21.next = ListNode(3)
node21.next.next = ListNode(4)
#pass_lists.append([node21, node21.next, node21.next.next])
pass_lists.append(node21)
node31 = ListNode(2)
node31.next = ListNode(6)
#pass_lists.append([node31, node31.next])
pass_lists.append(node31)
#print(pass_lists)
sol = Solution()
sol.mergeKLists(pass_lists)
#sol.mergeTwoLists([node11,node11.next, node11.next.next],[node21, node21.next, node21.next.next])
#sol.mergeTwoLists(node11, node21)
