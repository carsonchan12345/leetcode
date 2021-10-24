/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode res = new ListNode();
        ListNode respointer= res;
        ListNode pointer1 = l1;
        ListNode pointer2 = l2;
        if (l1== null && l2==null)
            return l1;
        while(pointer1!=null && pointer2!=null)
        {
            if (pointer1.val > pointer2.val)
            {
                respointer.val = pointer2.val;
                pointer2=pointer2.next;
            }
            else
            {
                respointer.val = pointer1.val;
                pointer1=pointer1.next;
            }
            respointer.next=new ListNode();
            respointer=respointer.next;}


        while(pointer1==null || pointer2==null)

        {



            if (pointer1 == null)
            {
                respointer.val=pointer2.val;
                pointer2=pointer2.next;

            }
            else
            {
                respointer.val=pointer1.val;
                pointer1=pointer1.next;
            }
            if (pointer1 == null && pointer2 == null)
                break;
            respointer.next=new ListNode();
            respointer=respointer.next;
        }

        return res;
    }
}