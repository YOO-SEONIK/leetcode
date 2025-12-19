# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None

        length = 1
        tail = head

        #노드의 길이 구하기
        while tail.next:
            tail = tail.next
            length +=1
        
        k = k % length

        if k == 0:
            return head

        cur = head
        for i in range(length -k -1):
            cur = cur.next 
        newHead = cur.next #설정한 위치 저장
        cur.next = None #배열의 끝으로 지정
        tail.next = head #마지막 원소를 앞으로 땡김

        return newHead
        